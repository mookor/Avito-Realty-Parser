import re
from dataclasses import dataclass

@dataclass
class Content:
    title: str
    price: str
    params: str
    adress: str
    description: str

    def __str__(self) -> str:
        title_str = f'{self.title}\n\n'
        price_str = f'Цена: {self.price}\n'
        params_str = f'Условия: {self.params}\n'
        adress_str = f'Адрес: {self.adress}\n'
        description_str = f'Описание: {self.description}\n'

        return title_str + price_str + params_str + adress_str + description_str


class Content_bag:
    def __init__(self, title, price, params, adress, description) -> None:
        self.title = title
        self.price = price
        self.params = params
        self.adress = adress
        self.description = description

    def split_adress_text(self, text):
        text_with_space_after = re.sub(r'(\d)([a-zA-Zа-яА-Я])', r'\1 \2', text)
        
        result = re.sub(r'([a-zA-Zа-яА-Я])(\d)', r'\1 \2', text_with_space_after)
    
        return result
    
    def __getitem__(self, index):
        content = Content(self.title[index].text, self.price[index].text, self.params[index].text, self.split_adress_text(self.adress[index].text), self.description[index].text)
        return content
    
    def __len__(self):
        return len(self.title)