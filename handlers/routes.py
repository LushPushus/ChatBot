from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from html import escape

OWNER_ID = 8379711632

router = Router()

#интеграция тгп эмодзи
EMOJI_1 = '<tg-emoji emoji-id="5211207549654703604">⚠️</tg-emoji>'
EMOJI_3 = '<tg-emoji emoji-id="5253501591561999154">🌟</tg-emoji>'
EMOJI_4 = '<tg-emoji emoji-id="5801031770577056696">🤩</tg-emoji>'
EMOJI_5 = '<tg-emoji emoji-id="5769357000949375342">🤩</tg-emoji>'
EMOJI_6 = '<tg-emoji emoji-id="5803158835950527182">🤩</tg-emoji>'
EMOJI_7 = ''
EMOJI_8 = ''

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
    await message.answer(f"{EMOJI_1} Команды:\n/start -- Запустить бота\n/help -- Список команд\n/about -- Про бота\n/owner -- Проверка на то, являешься ли ты моим создателем\n/game -- Игры (в разработке)\n/contact -- Связь с создателем",
        parse_mode="HTML")

@router.message(Command("about"))
async def about(message: Message):
    await message.answer(
        f"Данный бот является ботом тестом для данного <a href='https://t.me/PressureRUcommunityChat'>-> чата</a>\n"
        f"<blockquote>Твои Данные:</blockquote>"
        f"<blockquote>Твоё имя: {message.from_user.first_name}</blockquote>"
        f"<blockquote>Твой айди: {message.from_user.id}</blockquote>"
        f""
        f"<blockquote>Есть ли у тебя премиум: {message.from_user.is_premium}</blockquote>",
        parse_mode="HTML",
        disable_web_page_preview=True
    )

@router.message(Command("owner"))
async def owner(message: Message):
    if message.from_user.id == OWNER_ID:
        await message.answer("Да, ты мой владелец", parse_mode="HTML")
    else:
        await message.answer(f"{EMOJI_1}Нет, ты не мой владелец", parse_mode="HTML")

@router.message(Command("game"))
async def game(message: Message):
    await message.answer(f"{EMOJI_3}Игры пока что не доступны, но они в разработке!", reply_markup=get_main_inline_keyboard2(), parse_mode="HTML")

@router.message(Command("contact"))
async def contact(message: Message):
    await message.answer(f"{EMOJI_1}Для связи с создателем бота, пожалуйста, напишите ему в личные сообщения либо через бота чата.", reply_markup=get_main_inline_keyboard2(), parse_mode="HTML")

