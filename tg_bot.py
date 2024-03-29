from config import Token

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.reply_keyboard import ReplyKeyboardMarkup

from aiogram.dispatcher.filters import Text

from db import Database

from translation import txt_translate

import Time_manage
import aioschedule, time

bot = Bot(token=Token)
dp = Dispatcher(bot)
db = Database("database.db")

main_button = ['Расписание сегодня', 'Расписание на завтра', 'Расписание Звонков']

@dp.message_handler(commands='start')
async def start(message: types.Message):
    if not db.user_exist(message.from_user.id):
        db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, 'Введите Профиль')
        @dp.message_handler()
        async def bot_read(message: types.Message):
            db.set_nickname(message.from_user.id, message.text)
            await bot.send_message(message.from_user.id, 'Напишите /start')

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(*main_button)

        await message.answer("Нужная инфа ", reply_markup=keyboard)


@dp.message_handler(Text(equals='Расписание на завтра'))
async def Plan2(msg: types.Message):     
        await msg.answer(Time_manage.next_day(db.get_nick_name(msg.from_user.id)))
        Time_manage.plan_2 = []


@dp.message_handler(Text(equals='Расписание Звонков'))
async def Plan2(msg: types.Message):     
        await msg.answer('''
Начало       конец       перемена
08:30:00    09:15:00     10 минут
09:25:00    10:10:00     20 минут
10:30:00    11:15:00     15 минут
11:35:00    12:20:00     15 минут
12:35:00    13:20:00     20 минут
13:40:00    14:25:00     15 минут
14:40:00    15:25:00     10 минут
                    ''')
        

@dp.message_handler(Text(equals='Расписание сегодня'))
async def Plan(msg: types.Message): 
        await msg.answer(Time_manage.main(db.get_nick_name(msg.from_user.id)))
        Time_manage.plan = []

if __name__ == '__main__':  
    print('bot-start')
    executor.start_polling(dp)
