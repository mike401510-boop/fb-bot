import asyncio
import random
import string
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

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

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
                                                        
                                                            text = (
                                                                        f"🔔 **Новый пост!**\n\n"
                                                                                f"🔗 **Ссылка:** {post_url}\n\n"
                                                                                        f"💡 **Случайные варианты комментариев (3–4 шт):**\n"
                                                            )
                                                                for i, c in enumerate(comment_options, 1):
                                                                        text += f"{i}. `{c}`\n"
                                                                                
                                                                                    text += "\n*(Нажмите на текст комментария, чтобы скопировать его)*"

                                                                                        keyboard = InlineKeyboardMarkup(inline_keyboard=[
                                                                                                    [InlineKeyboardButton(text="📱 Открыть пост в Facebook", url=post_url)]
                                                                                        ])

                                                                                            await bot.send_message(
                                                                                                        chat_id=YOUR_TELEGRAM_CHAT_ID,
                                                                                                                text=text,
                                                                                                                        parse_mode="Markdown",
                                                                                                                                reply_markup=keyboard
                                                                                            )

                                                                                            @dp.message(Command("start"))
                                                                                            async def start_handler(message: types.Message):
                                                                                                await message.answer("Бот запущен! Отправьте /test для получения примеров комментариев.")

                                                                                                @dp.message(Command("test"))
                                                                                                async def test_handler(message: types.Message):
                                                                                                    await send_post_notification("https://facebook.com")

                                                                                                    async def main():
                                                                                                        await dp.start_polling(bot)

                                                                                                        if __name__ == "__main__":
                                                                                                            asyncio.run(main())

                                                                                        ]
                                               
