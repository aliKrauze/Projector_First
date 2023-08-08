from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
import os
import asyncio
from gif_search_copy import search_gifs

load_dotenv()
bot = Bot(os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def search_start(message: types.Message):
    await message.answer("""Hello, I'm a GIF searcher! Please, enter
                        a search word""")


@dp.message_handler()
async def user_word(message: types.Message):
    search_word = message.text

    gif_urls = search_gifs(search_word)

    for gif_url in gif_urls:
        await message.answer(gif_url)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
