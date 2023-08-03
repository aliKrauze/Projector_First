
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
import requests

bot_token = 'Token'
bot = Bot(token=bot_token)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Hi! I'm a GIF search bot. Please enter an emotion")

def search_gifs(search_word):
    api_key = 'Key'
    endpoint = 'http://api.giphy.com/v1/gifs/search'
    params = {
        'api_key': api_key,
        'q': search_word,
        'limit': 25
    }
    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        data = response.json()
        gif_links = [gif['images']['original']['url'] for gif in data['data']]
        return gif_links
    except requests.exceptions.RequestException as e:
        print(f'Error fetching GIFs:{e}')
        return []
    
async def gif_search(message: types.Message):
    search_word = message.text
    gifs = search_gifs(search_word)
    if gifs:
       gif_text = "\n".join(gifs)
       reply_text = f'Here are your GIFs: \n{gif_text}'
       await message.reply(reply_text)
    else:
        await message.reply("No GIFs found")

dp.register_message_handler(start, commands="start")
dp.register_message_handler(gif_search, content_types=types.ContentTypes.TEXT)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)

