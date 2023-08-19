from aiogram import Bot,Dispatcher, executor, types
import logging,os
from dotenv import load_dotenv

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

logging = logging.INFO


@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    await message.answer(f"Hello {message.from_user.first_name}")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
