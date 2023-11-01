import unittest
from src.scraper import steam_scraper, epic_scraper

class TestScraper(unittest.TestCase):

    def test_steam_scraper(self):
        game_name = 'Cyberpunk 2077'
        result = steam_scraper.get_game_info(game_name)
        self.assertIsNotNone(result)
        self.assertEqual(result['name'], game_name)
        self.assertIsInstance(result['price'], float)
        self.assertIsInstance(result['image'], str)

    def test_epic_scraper(self):
        game_name = 'Fortnite'
        result = epic_scraper.get_game_info(game_name)
        self.assertIsNotNone(result)
        self.assertEqual(result['name'], game_name)
        self.assertIsInstance(result['price'], float)
        self.assertIsInstance(result['image'], str)

if __name__ == '__main__':
    unittest.main()