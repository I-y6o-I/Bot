from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.builtin import CommandStart
import asyncio

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")



