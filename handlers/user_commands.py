from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from keyboards import inline

router = Router()


@router.message(CommandStart)
async def start(message: Message):
    await message.answer('qq', reply_markup=inline.menu)
