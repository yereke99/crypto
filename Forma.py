from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types.message import Message
from load import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
import logging
from keyboard import*
from database import Database
import datetime

btn = Button()

class FormaData(StatesGroup):
    fio = State()
    iin = State()
    phone = State()

@dp.message_handler(state='*', commands='Бас тарту🙌🏻')
@dp.message_handler(Text(equals='Бас тарту🙌🏻', ignore_case=True), state='*')
async def cancell_handler(message: types.Message, state: FSMContext):
    """
    :param message: Бастартылды
    :param state: Тоқтату
    :return: finish

    """
    
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Бас тарту!')
    await state.finish()
    await message.reply('Бастартылды.', reply_markup=btn.btn_driver())

