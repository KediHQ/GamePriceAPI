import requests
from bs4 import BeautifulSoup

class EpicScraper:
    def __init__(self):
        self.base_url = "https://epicgamesdb.info/browse?keywords="

    def get_game_info(self, game_name):
        url = self.base_url + game_name.replace(" ", "%20").lower()

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        games_info = []

        for offer_card in soup.find_all('a', class_='offer-card'):
            game_info = {}
            game_info['name'] = offer_card.find('h5', class_='offer-card-title').text.strip()
            game_info['image'] = offer_card.find('img', class_='offer-image-tall')['src']
            game_info['price'] = offer_card.find('div', class_='current-price').text.strip()
            games_info.append(game_info)

        return games_info