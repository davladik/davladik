from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from loader import *


bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler()
async def get_message(message):
    print(await bot.get_updates())


executor.start_polling(dp)