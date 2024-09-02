import requests
import bs4
from time import sleep
import random
from content import Content_bag

class Parser:

    def __init__(self, url, attempts = 5):
        self.url = url

        self.user_agents = [
                                            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
                                            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991"
                                            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7"
                                        ]
        self.headers = {"User-Agent": random.choice(self.user_agents)}
        self.attempts = attempts

    def get_html(self, url):
        response = requests.get(url, headers=self.headers)

        return response.text
    

    def get_content(self, url):
        attempts = 0
        while attempts < self.attempts:
            html = self.get_html(url)

            soup = bs4.BeautifulSoup(html, 'html.parser')
            
            title = 'iva-item-titleStep-pdebR'
            price = 'iva-item-priceStep-uq2CQ'
            params = 'iva-item-autoParamsStep-WzfS8'
            adress = 'geo-root-zPwRk'
            description = 'iva-item-descriptionStep-C0ty1'

            title_soup = soup.find_all('div', {'class': title})
            price_soup = soup.find_all('div', {'class': price})
            params_soup = soup.find_all('div', {'class': params})
            adress_soup = soup.find_all('div', {'class': adress})
            description_soup = soup.find_all('div', {'class': description})
            
            if len(title_soup) == 0:
                attempts += 1
                sleep(1)
                continue
            
            return Content_bag(title_soup, price_soup, params_soup, adress_soup, description_soup)
            
