from flask import Flask, request, jsonify

from scraper.steam_scraper import SteamScraper
from scraper.epic_scraper import EpicScraper
from scraper.gog_scraper import GogScraper

app = Flask(__name__)

@app.route('/game', methods=['GET'])
def get_game():
    game_name = request.args.get('name')
    if not game_name:
        return jsonify({'error': 'Missing game name'}), 400

    steam_scraper = SteamScraper()
    epic_scraper = EpicScraper()
    gog_scraper = GogScraper()

    steam_game = steam_scraper.get_game_info(game_name)
    epic_game = epic_scraper.get_game_info(game_name)
    gog_game = gog_scraper.get_game_info(game_name)

    if not steam_game and not epic_game and not gog_game:
        return jsonify({'error': 'Game not found'}), 404

    return jsonify({
        'steam': steam_game,
        'epic': epic_game,
        'gog': gog_game
    })

if __name__ == '__main__':
    app.run(debug=True)