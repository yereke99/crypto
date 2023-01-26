import asyncio
from database import Database
from load import bot, Dispatcher
from pybit import usdt_perpetual
from config import*
from by import Trader
from text import*
import random
from coins import*

trader = Trader()
db = Database()
coin = Coin()


async def manager():
    for i in db.fetch():
        for c in coin.get_coin():
            await bot.send_message(
                i,
                text=f'💰 Арбитраж пайдасы {c} ➡️ {coin.get_coin().index(c)+1}пайда: {random.random()}'
            )
    