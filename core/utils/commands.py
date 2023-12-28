from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command="currency_nbu",
            description="Поточний курс валют"
        ),
        BotCommand(
            command="currency_bank",
            description="Поточний курс міжбанк"
        ),
        BotCommand(
            command="currency_market",
            description="Поточний курс"
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
