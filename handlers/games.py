from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


games_router = Router()


@games_router.message(Command("startgame"))
async def start_game(message: Message):
    await message.answer("Игры всё ещё недоступны, но уже находятся в разработке!")
