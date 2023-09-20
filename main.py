import os
from dotenv import load_dotenv, find_dotenv

from scripts import markups as mk
from scripts import phys_calc as pc

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

load_dotenv(find_dotenv("utils/token.env"))

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)


# start
@dp.message_handler(commands='start')
async def start(message):
    await bot.send_message(message.chat.id,
                           f'Приветствую, <b><a href="https://t.me/{message.from_user.username}">{message.from_user.first_name}</a></b>!',
                           parse_mode='html', disable_web_page_preview=True)
    await bot.send_message(message.chat.id, 'Выбери любую формулу из списка', reply_markup=mk.formula_list)


executor.start_polling(dp, loop=True, skip_updates=True)
