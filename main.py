import os
import asyncio
# import loguru
from dotenv import load_dotenv, find_dotenv

import colorama
from colorama import Fore

from callbacks import bot_callbacks
from handlers import user_commands
# from scripts import phys_calc as pc

from aiogram import Bot, Dispatcher

colorama.init()


async def main():
    load_dotenv(find_dotenv("utils/token.env"))
    bot = Bot(os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_routers(
        bot_callbacks.router,
        user_commands.router
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    print(Fore.RED + '\t Bot is running!')
    asyncio.run(main())
