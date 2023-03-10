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
db = Database()

class FormaData(StatesGroup):
    calc = State()
    

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
    await message.reply('Бастартылды.', reply_markup=btn.menu_kz(db.check(message.from_user.id)))


@dp.message_handler(state=FormaData.calc)
async def calcHandler(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['usdt'] = int(message.text)

    
    db.insertDB(message.from_user.id, data['usdt'])
    await bot.send_message(
        message.from_user.id,
        text="Сіздің сұранысыңыз арбитражға 👌🏻 сәтті қабылданды. Сұраныс ⚙️ Өңделу үстінде.",
        reply_markup=btn.menu_kz(db.check(message.from_user.id))
    )    
    
    await state.finish()
