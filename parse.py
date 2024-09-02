import requests
import bs4
import re
def split_adress_text(text):
    text_with_space_after = re.sub(r'(\d)([a-zA-Zа-яА-Я])', r'\1 \2', text)
    
    # Теперь добавляем пробел перед цифрой, если перед ней идет буква
    result = re.sub(r'([a-zA-Zа-яА-Я])(\d)', r'\1 \2', text_with_space_after)
    
    return result

url = 'https://www.avito.ru/novosibirsk/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?context=H4sIAAAAAAAA_0q0MrSqLraysFJKK8rPDUhMT1WyLrYyNLNSKk5NLErOcMsvyg3PTElPLVGyrgUEAAD__xf8iH4tAAAA&f=ASgBAQICAkSSA8gQ8AeQUgFAzAgkklmQWQ&s=104'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

response = requests.get(url, headers=headers)

soup = bs4.BeautifulSoup(response.text, 'html.parser')

title = 'iva-item-titleStep-pdebR'
price = 'iva-item-priceStep-uq2CQ'
params = 'iva-item-autoParamsStep-WzfS8'
adress = 'geo-root-zPwRk'
description = 'iva-item-descriptionStep-C0ty1'

attributes_list = [title, price, params, adress, description]

title_soup = soup.find_all('div', {'class': title})
price_soup = soup.find_all('div', {'class': price})
params_soup = soup.find_all('div', {'class': params})
adress_soup = soup.find_all('div', {'class': adress})
description_soup = soup.find_all('div', {'class': description})

for title, price, params, adress, description in zip(title_soup, price_soup, params_soup, adress_soup, description_soup):
    adress_text = split_adress_text(adress.text)
    
    print(title.text, price.text, params.text, adress_text, description.text)
    print('-------------------')
x = 1 
