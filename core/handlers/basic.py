from aiogram import Bot
from core.config import ADMIN_ID
from aiogram.types import Message
from core.utils.currency import send_request_currency_nbu


async def get_currency_exchange_nbu(message: Message, bot: Bot):
    currency = send_request_currency_nbu()
    await message.answer(f"Курс НБУ на {currency['date']}:\r\n"
                         f"USD = {currency['USD']}\r\n"
                         f"EUR = {currency['EUR']}")


async def get_currency_exchange_bank(message: Message, bot: Bot):
    await message.answer(f"Поточний курс валют міжбанк: ___")


async def get_currency_exchange(message: Message, bot: Bot):
    await message.answer(f"Поточний курс валют: ___")
