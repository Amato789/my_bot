import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from core.config import TOKEN, ADMIN_ID
from core.utils.commands import set_commands
from core.handlers.basic import get_currency_exchange_nbu, get_currency_exchange_bank, get_currency_exchange


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(ADMIN_ID, text="Bot started!")


async def stop_bot(bot: Bot):
    await bot.send_message(ADMIN_ID, text="Bot stopped!")


async def start():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] - %(name)s - "
               "(%(filename)s).%(funcName)s%(lineno)d - %(message)s"
    )
    bot = Bot(token=TOKEN, parse_mode='HTML')
    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(get_currency_exchange_nbu, Command(commands='currency_nbu'))
    dp.message.register(get_currency_exchange_bank, Command(commands='currency_bank'))
    dp.message.register(get_currency_exchange, Command(commands='currency_market'))

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
