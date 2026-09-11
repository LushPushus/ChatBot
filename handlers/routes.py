from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

OWNER_ID = 8379711632

router = Router()

def get_main_inline_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Перейти в чат", url="https://t.me/PressureRUcommunityChat")],
            [InlineKeyboardButton(text="Перейти в канал", url="https://t.me/PressureNewsRoblox")],
        ]
    )

    return keyboard

def get_main_inline_keyboard2():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Дополнительная помощь через бота чата", url="https://t.me/Urbanshadestakesbot")],
            [InlineKeyboardButton(text="Чат с создателем", url="https://t.me/LushPushus")],
        ]
    )

    return keyboard

@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет!\nНапиши /help для помощи",
                         reply_markup=get_main_inline_keyboard())

@router.message(Command("help"))
async def help(message: Message):
    await message.answer("Команды:\n/start -- Запустить бота\n/help -- Список команд\n/about -- Про бота\n/owner -- Проверка на то, являешься ли ты моим создателем\n /game -- Игры (в разработке)\n /contact -- Связь с создателем",)

@router.message(Command("about"))
async def about(message: Message):
    await message.answer(
        f"Данный бот является ботом тестом для данного <a href='https://t.me'>-> чата</a>\n"
        f"<blockquote>Твои Данные:</blockquote>"
        f"<blockquote>Твоё имя: {message.from_user.first_name}</blockquote>"
        f"<blockquote>Твой айди: {message.from_user.id}</blockquote>"
        f"<blockquote>Есть ли у тебя премиум: {message.from_user.is_premium}</blockquote>",
        parse_mode="HTML",
        disable_web_page_preview=True
    )


@router.message(Command("owner"))
async def owner(message: Message):
    if message.from_user.id == OWNER_ID:
        await message.answer("Да, ты мой владелец")
    else:
        await message.answer("Нет, ты не мой владелец")

@router.message(Command("game"))
async def game(message: Message):
    await message.answer("Игры пока что не доступны, но они в разработке!", reply_markup=get_main_inline_keyboard2())

@router.message(Command("contact"))
async def contact(message: Message):
    await message.answer("Для связи с создателем бота, пожалуйста, напишите ему в личные сообщения либо через бота чата.", reply_markup=get_main_inline_keyboard2())

