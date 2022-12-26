#!/usr/bin/env python
# -*- coding: utf-8 -*-
from aiogram import types

class Button:
    def __init__(self) -> None:
        pass

    def start_btn(self):
        btn_start = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)

        btn_start.add("🇰🇿 Қазақ", "🇷🇺 Русская")

        return btn_start

