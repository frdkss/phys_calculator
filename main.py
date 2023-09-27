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
                           parse_mode='html', disable_web_page_preview=True, reply_markup=mk.menu)


@dp.callback_query_handler(text='back')
async def menu(call):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await call.message.answer('Выберете нужную формулу', reply_markup=mk.menu)


@dp.callback_query_handler(text='formulas')
async def formulas(call):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await call.message.answer('Выберете нужную формулу', reply_markup=mk.formulas_list)


@dp.callback_query_handler(text='culon_law')
async def culon_law(call, message):
    await call.message.answer(f'{pc.culon_law(message)}')

executor.start_polling(dp, loop=True, skip_updates=True)
