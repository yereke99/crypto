import asyncio
from database import Database
from load import bot, Dispatcher
from pybit import usdt_perpetual
from config import*

session_unauth = usdt_perpetual.HTTP(
    endpoint="https://api-testnet.bybit.com"
)


r = session_unauth.public_trading_records(
        symbol="BTCUSDT",
        limit=10
)

db = Database()

async def manager():
    await bot.send_message(
        admin_id,
        text=r,
    )