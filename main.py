import asyncio

from aiogram import Bot, Dispatcher


async def start_bot(bot: Bot):
    await bot.send_message(111, text="Bot started!")


async def stop_bot(bot: Bot):
    await bot.send_message(111, text="Bot stoped!")


async def start():
    bot = Bot(token='token', parse_mode='HTML')
    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
