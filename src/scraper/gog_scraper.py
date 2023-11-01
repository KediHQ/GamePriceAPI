from bs4 import BeautifulSoup
import requests

class GogScraper:
    def __init__(self):
        self.base_url = "https://www.gog.com/en/games?query="

    def get_game_info(self, game_name):
        search_url = self.base_url + game_name.replace(" ", "+")

        response = requests.get(search_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        game_info = []

        products = soup.find_all('a', class_='product-tile product-tile--grid')

        for product in products:
            game = {}
            product_title = product.find('product-title', {'class': 'small', 'selenium-id': 'productTitle'})
            spans = product_title.find_all('span')
            if len(spans) >= 2:
                game['name'] = spans[1].text.strip()
            else:
                game['name'] = "Not available"
    
            image_urls = [source['srcset'] for source in product.find_all('source')]
            game['image'] = image_urls
    
            price = product.find('span', class_='final-value')
            if price is None:
                game['price'] = "Not available"
            else:
                game['price'] = price.text.strip()
    
            game_info.append(game)
    
        return game_info