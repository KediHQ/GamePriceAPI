import requests
from bs4 import BeautifulSoup

class SteamScraper:
    def __init__(self):
        self.base_url = "https://store.steampowered.com/search/?term="

    def get_game_info(self, game_name):
        search_url = self.base_url + game_name.replace(" ", "+")

        response = requests.get(search_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        game_info = []

        search_results = soup.find_all(class_='search_result_row ds_collapse_flag')

        for result in search_results:
            game = {}
            game['name'] = result.find(class_='title').text
            game['image'] = result.find('img')['src']
            price = result.find(class_='discount_final_price')
            if price is None:
                game['price'] = "Not available"
            else:
                game['price'] = price.text
            game_info.append(game)

        return game_info