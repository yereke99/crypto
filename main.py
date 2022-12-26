#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aiogram.dispatcher.filters import Text
from load import bot, dp
from aiogram import types
from text import*
from Forma import*

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    print(message.from_user.id)

    await bot.send_message(
        message.from_user.id,
        text=start_text,
        reply_markup=btn.start_btn()
    )

