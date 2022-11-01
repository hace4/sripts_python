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
db = Database("C:\\Users\\shmel\\OneDrive\\Рабочий стол\\sripts_python\\Shadiwal\\Database.db")

main_button = ['Расписание сегодня', 'Доп функции', 'Расписание на завтра', 'Расписание Звонков']

@dp.message_handler(commands='start')
async def start(message: types.Message):
    if not db.user_exist(message.from_user.id):
        db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, 'Введите Ф.И')
        @dp.message_handler()
        async def bot_read(message: types.Message):
            db.set_nickname(message.from_user.id, message.text)
            print(message.from_user.id)
            print(message.from_user.first_name)
            print(message.from_user.last_name)
            print(message.from_user.username)
            await bot.send_message(message.from_user.id, 'Напишите /start')

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(*main_button)

        await message.answer("Нужная инфа ", reply_markup=keyboard)

@dp.message_handler(Text(equals='Назад'))
async def start(message: types.Message):

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(*main_button)

    await message.answer("Нужная инфа ", reply_markup=keyboard)

@dp.message_handler(Text(equals='Доп функции'))
async def lol(message: types.Message):
    dop_buttons = ['Назад', 'Переводчик на английский']
    keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=False, one_time_keyboard=True)
    keyboard1.add(*dop_buttons)

    await message.answer("Вот немного приколюх", reply_markup=keyboard1)



@dp.message_handler(Text(equals='Переводчик на английский'))
async def trans(msg: types.Message):
    await msg.answer('Отправте текст на перевод конец текста обозначте точкой запятой' + '\n' + ' затем через проьел введите абривеатуру языка с которого переводите' + '\n' + 'затем точка запятая пробел и язык на который переводите: ')

    @dp.message_handler()
    async def trans(msg: types.Message):
            stroke = msg.text
            list_word = list(stroke.split('; '))
            msg.text = txt_translate(list_word[0], list_word[1], list_word[-1])
            await bot.send_message(msg.from_user.id, msg.text)
        

@dp.message_handler(Text(equals='Расписание на завтра'))
async def Plan2(msg: types.Message):     
        await msg.answer(Time_manage.next_day(db.get_nick_name(msg.from_user.id)))
        Time_manage.plan_2 = []


@dp.message_handler(Text(equals='Расписание Звонков'))
async def Plan2(msg: types.Message):     
        await msg.answer('''
Начало       конец       перемена
09:00:00    09:45:00     10 минут
09:55:00    10:40:00     20 минут
11:00:00    11:45:00     20 минут
12:05:00    12:50:00     10 минут
13:00:00    13:45:00     20 минут
14:05:00    14:50:00     20 минут
15:10:00    15:55:00     10 минут
16:05:00    16:50:00     10 минут
                    ''')
        

@dp.message_handler(Text(equals='Расписание сегодня'))
async def Plan(msg: types.Message): 
        await msg.answer(Time_manage.main(db.get_nick_name(msg.from_user.id)))
        Time_manage.plan = []

if __name__ == '__main__':
    executor.start_polling(dp)
    aioschedule.every(0.1).seconds.do(Plan)
    while True:
        aioschedule.run_pending()