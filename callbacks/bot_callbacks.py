from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards import inline

router = Router()


@router.callback_query(F.data == 'back')
async def back_to_menu(call: CallbackQuery):
    await call.message.edit_text('menu', reply_markup=inline.menu)


@router.callback_query(F.data == 'formulas')
async def formulas(call: CallbackQuery):
    await call.message.edit_text('formula1', reply_markup=inline.formulas_list)
