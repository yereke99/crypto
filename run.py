from load import bot, storage
from main import dp
import aioschedule, async_engine
import asyncio


# Async-Schedule here is working every 5 seconds fo async-engine.
async def scheduler():
    aioschedule.every(5).seconds.do(async_engine.manager)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

async def on_start(dp):
    asyncio.create_task(scheduler())

async def on_stop(dp):
    await bot.close()
    await storage.close()

def main():
    from aiogram import executor
    executor.start_polling(dp, on_startup=on_start, on_shutdown=on_stop)


if __name__ == "__main__":
    main()
