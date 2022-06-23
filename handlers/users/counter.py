import aiohttp
import json
from aiogram import types
from aiogram.dispatcher.filters import Command
from loader import dp


@dp.message_handler(Command('lowprice'))
async def lowprice(message: types.Message):

    querystring = {"query": "new york", "locale": "en_US", "currency": "USD"}

    headers = {
        "X-RapidAPI-Key": "659ab1311amsh9e469c9c82a15bep1c78d0jsn31bd6e9fbc3d",
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com",
    }

    async with aiohttp.ClientSession() as session:
        async with session.get('https://hotels4.p.rapidapi.com/locations/v2/search', headers=headers,
                               params=querystring) as response:
            html = await response.text()
            print('[' + html + ']')
            asd = json.loads(html)
            print(asd)
            print(type(asd))

        await message.answer(html[:15])
