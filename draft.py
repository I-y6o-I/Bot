import aiohttp
import asyncio


async def main():
    session = aiohttp.ClientSession()

    querystring = {"query": "new york", "locale": "en_US", "currency": "USD"}

    headers = {
        "X-RapidAPI-Key": "659ab1311amsh9e469c9c82a15bep1c78d0jsn31bd6e9fbc3d",
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com",
    }
    async with session.get('https://hotels4.p.rapidapi.com/locations/v2/search', headers=headers,
                           params=querystring) as response:
        print("Status:", response.status)
        print("Content-type:", response.headers['content-type'])

        html = await response.text()
        print("Body:", html, "...")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
