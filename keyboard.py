#!/usr/bin/env python
# -*- coding: utf-8 -*-
from aiogram import types

class Button:
    def __init__(self) -> None:
        pass

    def start_btn(self):
        btn_start = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
        btn_start.add("🇰🇿 Қазақша", "🇷🇺 Русская")

        return btn_start

    def menu_kz(self, check: bool):
        menukz = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
        if check:
            menukz.add("❌ Stop") 
            menukz.add("📈 Биржа")
            menukz.add("💰 Арбитраж")
            menukz.add("🗣 Техникалық көмек")
        else:
            menukz.add("📈  Биржа", "💰  Арбитраж")
            menukz.add("🗣 Техникалық көмек")
            
        return menukz
    
    def menu_ru(self, check: bool):
        menuru = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
        
        if check:
            menuru.add("❌  Stop") 
            menuru.add("📈 Биржа")
            menuru.add("💰 Арбитраж")
            menuru.add("🗣 Техническая поддержка")
        else:
            menuru.add("📈  Биржа", "💰  Арбитраж")
            menuru.add("🗣 Техническая поддержка")
        
        return menuru
    

    def arbi(self):
        arbi = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
        
        arbi.add("❌ Stop")

        return

    def admin(self):
        admin = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
        
        admin.add("👤 User-ді қосу")
        admin.add("👤 User-ді жою")
        admin.add("📝 Топтық хабарлама")
        
        return admin

