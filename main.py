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
        text="Сәлемтсіз бе " % message.from_user.first_name,
        reply_markup=btn.start_btn()
    )

    await bot.send_message(
        message.from_user.id,
        text="Бұл телеграмм платформасында 💰 крипто биржаны бақылайтын уникалды бот. Қазір демо версияда.",
        reply_markup=btn.start_btn()
    )

