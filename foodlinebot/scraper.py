from bs4 import BeautifulSoup
from abc import ABC, abstractmethod
import requests


class Food(ABC):
    def __init__(self, area, category):
        self.area = area
        self.category = category
 
    @abstractmethod
    def scrape(self):
        pass


class IFoodie(Food):
    def scrape(self):
        # response = requests.get("https://ifoodie.tw/explore/list/" + self.category + "?opening=true&sortby=popular&place=current")
        response = requests.get("https://ifoodie.tw/explore/" + self.area + "/list/" + self.category + "?opening=true&sortby=popular")
        soup = BeautifulSoup(response.content, "html.parser")
        cards = soup.find_all('div', {'class': 'jsx-3292609844 restaurant-info'}, limit=5)
 
        content = ""
        for card in cards:
            title = card.find("a", {"class": "jsx-3292609844 title-text"}).getText()
            stars = card.find("div", {"class": "jsx-1207467136 text"}).getText()
            count = card.find("a", {"class": "jsx-3292609844 review-count"}).getText()
            address = card.find("div", {"class": "jsx-3292609844 address-row"}).getText()

            content += "{0}\n{1}, {2}顆星\n{3}\n\n".format(title, count[1:-1], stars, address)
 
        return content