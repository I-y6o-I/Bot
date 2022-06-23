from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
import asyncio
from utils.set_bot_commands import set_default_commands

from loader import dp




# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler()
async def bot_echo(message: types.Message):
    await message.answer(f"Эхо без состояния."
                         f"Сообщение:\n"
                         f"{message.text}")
