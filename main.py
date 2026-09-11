from os import getenv
import asyncio
from aiogram import Bot, Dispatcher
from pathlib import Path
from dotenv import load_dotenv
from handlers.routes import router

load_dotenv()
TOKEN = "8691809880:AAFoxraKjZ1F1kqWGB9apajR4i8JPq_GEh4"

dp = Dispatcher()
dp.include_router(router)

async def main():
    bot = Bot(token=TOKEN)

    print("Ботик работает")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())