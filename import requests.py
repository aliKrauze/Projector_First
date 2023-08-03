import requests


def search_image(query):
    api_key = 'Key'
    endpoint = 'https://api.giphy.com/v1/gifs/search'
    req_params = {
        'api_key': api_key,
        'q': query,
        'limit': 25
    }

    try:
        resp = requests.get(endpoint, params=req_params)
        resp.raise_for_status()
        data = resp.json()
        gif_links = [gif['images']['original']['url'] for gif in data['data']]
        return gif_links
    except requests.exceptions.RequestException as e:
        print(f"Error ocured {e}")
        return None


if __name__ == "__main__":
    search_word = input("Please, enter the search word for GIFs: ")
    gif_links = search_image(search_word)

    if gif_links:
        print("GIF links:")
        for link in gif_links:
            print(link)
    else:
        print("Sorry, no GIFs found.")
