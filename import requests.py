import os
import requests
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv('API_KEY')


BASE_URL = 'https://api.giphy.com/v1/gifs/search'


def search_gifs(search_term, limit=25):
    params = {
        'api_key': API_KEY,
        'q': search_term,
        'limit': limit
    }

    response = requests.get(BASE_URL, params=params)

    data = response.json()

    gif_urls = [gif['images']['original']['url'] for gif in data['data']]
    return gif_urls


if __name__ == '__main__':
    search_term = input("Please enter a search word")
    gif_urls = search_gifs(search_term)

    for gif_url in gif_urls:
        print(gif_url)
