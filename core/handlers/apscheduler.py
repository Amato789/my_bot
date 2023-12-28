from aiogram import Bot
from core.config import ADMIN_ID


async def send_message_currency(bot: Bot):
    await bot.send_message(ADMIN_ID, f"Поточний курс валют: ___ ")
