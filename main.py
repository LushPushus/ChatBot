import asyncio
import os
from os import getenv
from pathlib import Path
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from aiohttp import web
from handlers.routes import router

load_dotenv()
TOKEN = "8691809880:AAFoxraKjZ1F1kqWGB9apajR4i8JPq_GEh4"

dp = Dispatcher()
dp.include_router(router)

# Специальная функция-заглушка для Render
async def handle(request):
    return web.Response(text="Бот запущен и работает!")

async def main():
    bot = Bot(token=TOKEN)
    
    # Запускаем бота в фоновом режиме
    asyncio.create_task(dp.start_polling(bot))
    print("Ботик работает")

    # Настраиваем веб-сервер для прохождения проверки Render
    app = web.Application()
    app.router.add_get('/', handle)
    
    runner = web.AppRunner(app)
    await runner.setup()
    
    # Получаем порт, который выделил Render (по умолчанию 10000)
    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    
    print(f"Запуск веб-сервера на порту {port}...")
    await site.start()
    
    # Бесконечное ожидание, чтобы скрипт не завершался
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
