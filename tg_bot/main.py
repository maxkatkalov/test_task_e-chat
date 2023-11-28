import os
import asyncio
import logging

from aiogram import Bot, Dispatcher, types
import dotenv


dotenv.load_dotenv()

logging.basicConfig(level=logging.INFO)
bot = Bot(token=os.environ.get("BOT_TOKEN"))
dp = Dispatcher()


@dp.message()
async def send_message_to_api(message: types.Message):
    print(f"New message found: {message.text}")


if __name__ == '__main__':
    asyncio.run(dp.start_polling(bot))
