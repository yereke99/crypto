#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aiogram.dispatcher.filters import Text
from load import bot, dp
from aiogram import types
from text import*
from Forma import*
from config import*
from FormaRu import*
from database import*


btn = Button()
forma = FormaData()
db = Database()


@dp.message_handler(commands=['admin'])
async def start_handler(message: types.Message):
    print(message.from_user.id)

    if message.from_user.id == admin_id:
        await bot.send_message(
            message.from_user.id,
            text="Сәлеметсіз бе админ %s"% message.from_user.first_name,
            reply_markup=btn.admin()
        )


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    print(message.from_user.id)

    await bot.send_message(
        message.from_user.id,
        text="Тілді таңдаңыз *%s*" % message.from_user.first_name,
        parse_mode="MarkdownV2",
        reply_markup=btn.start_btn()
    )

@dp.message_handler(Text(equals="🇰🇿 Қазақша"), content_types=['text'])
async def messageHandlerKZ(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        text="Сәлемтсіз бе *%s*" % message.from_user.first_name,
        parse_mode="MarkdownV2"
    )

    await bot.send_message(
        message.from_user.id,
        text="Бұл телеграмм платформасында 💰 крипто биржаны бақылайтын уникалды бот. Қазір демо версияда.",
        reply_markup=btn.menu_kz(db.check(message.from_user.id))
    )

@dp.message_handler(Text(equals="🇷🇺 Русская"), content_types=['text'])
async def messageHandlerRU(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        text="Здравствуйте *%s*" % message.from_user.first_name,
        parse_mode="MarkdownV2"
    )

    await bot.send_message(
        message.from_user.id,
        text="Это уникальный бот, который следит за криптобиржей 💰 на платформе Telegram. Сейчас в демо-версии.",
        reply_markup=btn.menu_ru(db.check(message.from_user.id))
    )


@dp.message_handler(Text(equals="📈 Биржа"), content_types=['text'])
async def messageHandler(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        text="Биржамен API байланыста уақытша қателіктер бар!",
        reply_markup=btn.menu_kz(db.check(message.from_user.id))
    )

   
@dp.message_handler(Text(equals="💰 Арбитраж"), content_types=['text'])
async def messageHandler(message: types.Message):
    await FormaData.calc.set()

    await bot.send_message(
        message.from_user.id,
        text="Сізде қанша USDT бар?",
        reply_markup=types.ReplyKeyboardMarkup(selective=True, resize_keyboard=True).add("Бас тарту🙌🏻")
    )

@dp.message_handler(Text(equals="🗣 Техникалық көмек"), content_types=['text'])
async def messageHandler(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        text="87471850499 📲",
        reply_markup=btn.menu_kz(db.check(message.from_user.id))
    )

@dp.message_handler(Text(equals="📈  Биржа"), content_types=['text'])
async def messageHandler(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        text="Имеются временные ошибки связи API с биржей!",
        reply_markup=btn.menu_ru(db.check(message.from_user.id))
    )

@dp.message_handler(Text(equals="💰  Арбитраж"), content_types=['text'])
async def messageHandler(message: types.Message):
    await FormaDataRU.calc.set()

    await bot.send_message(
        message.from_user.id,
        text="Сколько у вас USDT?",
        reply_markup=types.ReplyKeyboardMarkup(selective=True, resize_keyboard=True).add("Отмена🙌🏻")
    )


@dp.message_handler(Text(equals="🗣 Техническая поддержка"), content_types=['text'])
async def messageHandler(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        text="87471850499 📲",
        reply_markup=btn.menu_ru(db.check(message.from_user.id))
    )

@dp.message_handler(Text(equals="❌ Stop"), content_types=['text'])
async def messageHandler(message: types.Message):
    db.delete(message.from_user.id)
    await bot.send_message(
        message.from_user.id,
        text="Сіздің өтінішіңіз базадан ❌ жойылды.",
        reply_markup=btn.menu_kz(db.check(message.from_user.id))
    )

@dp.message_handler(Text(equals="❌  Stop"), content_types=['text'])
async def messageHandler(message: types.Message):
    db.delete(message.from_user.id)
    await bot.send_message(
        message.from_user.id,
        text="Ваш запрос был ❌ удален из базы данных.",
        reply_markup=btn.menu_ru(db.check(message.from_user.id))
    )
