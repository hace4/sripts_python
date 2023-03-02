from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.reply_keyboard import ReplyKeyboardMarkup
import logging
from aiogram.dispatcher.filters import Text
from config import Token

bot = Bot(token=Token)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands='spam')
async def send_welcome(message: types.Message):
   await message.answer(open("templates\\index.html", 'r'), parse_mode=types.ParseMode.HTML)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
