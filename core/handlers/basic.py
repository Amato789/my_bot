from aiogram import Bot
from core.config import ADMIN_ID
from aiogram.types import Message
from core.utils.currency import send_request_currency_nbu
from core.utils.weather import send_request_get_weather


async def get_currency_exchange_nbu(message: Message, bot: Bot):
    currency = send_request_currency_nbu()
    await message.answer(f"Курс НБУ на {currency['date']}:\r\n"
                         f"USD = {currency['USD']}\r\n"
                         f"EUR = {currency['EUR']}")


async def get_weather(message: Message, bot: Bot):
    weather = send_request_get_weather()
    await message.answer(f"Погода на {weather['date']}:\r\n"
                         f"Город: {weather['place_id']}\r\n"
                         f"Температура: {weather['temperature']}\r\n"
                         f"Summary: {weather['summary']}\r\n")
