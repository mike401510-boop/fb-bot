import os
import asyncio
import random
import string
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiohttp import web

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

def generate_random_comments(count=4, length=3) -> list:
    letters = string.ascii_lowercase + "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    emojis = ["🔥", "👍", "❤️", "👏", "🙌", "💯", "😀"]

    comments = []
    for _ in range(count - 1):
        rand_str = ''.join(random.choice(letters) for _ in range(length))
        comments.append(rand_str)

    comments.append(random.choice(emojis))
    return comments

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer("Бот работает!")

# Заглушка для Render, чтобы он видел открытый порт
async def handle(request):
    return web.Response(text="Bot is running!")

async def main():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.getenv("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
