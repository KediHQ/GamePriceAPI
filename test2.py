from bs4 import BeautifulSoup
import requests

url = "https://www.gog.com/en/games?query=cyberpunk"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

products = soup.find_all('a', class_='product-tile product-tile--grid')

for product in products:
    product_title = soup.find('product-title', {'class': 'small', 'selenium-id': 'productTitle'})
    game_name = product_title.find_all('span')[1].text.strip()
    print(f"Game Name: {game_name}")

    image_urls = [source['srcset'] for source in product.find_all('source')]
    print(f"Image URLs: {image_urls}")

    price = product.find('span', class_='final-value').text.strip()
    print(f"Price: {price}")

    print("\n---\n")