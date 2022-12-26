from aiogram import executor
from load import bot, storage
from main import dp


async def on_stop(dp):
    await bot.close()
    await storage.close()


if __name__ == "__main__":
    executor.start_polling(dp, on_shutdown=on_stop)
