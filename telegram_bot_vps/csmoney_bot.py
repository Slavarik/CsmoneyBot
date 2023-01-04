import json
from aiogram.utils.markdown import hbold, hlink
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from main import collect_data
import time
import sqlite3

API_Token = "5814281280:AAEznuAMmf0FZe3olCqBSn8DaSXymQKqess"
bot = Bot(token=API_Token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_buttons = ['🔪 Ножи', '🧤 Перчатки', '🔫 Снайперские винтовки', '👊 Пистолеты', '🦅 Пистолеты-Пулемёты', '🤖 Штурмовые Винтовки', '🩸 Дробовики', '☠ Пулемёты']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(
        id INTEGER
    )""")

    connect.commit()

    #check id
    people_id = message.chat.id
    cursor.execute(f"SELECT id FROM login_id WHERE id = {people_id}")
    data = cursor.fetchone()
    print(data)
    if data is None:
        user_id = [message.chat.id]
        cursor.execute("INSERT INTO login_id VALUES(?);", user_id)
        connect.commit()
    else:
        message.answer(message.chat.id, 'Такой пользователь уже существует')


    await message.answer('Выбеирте категорию', reply_markup=keyboard)


@dp.message_handler(Text(equals='🔪 Ножи'))
async def get_discount_knives(message: types.Message):
    await message.answer('Пожалуйста подождите...')

    collect_data(weapon_type=2)

    with open('result.json', encoding='utf-8') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("name"), item.get("3d"))}\n' \
               f'{hbold("Цена: ")}${item.get("computed")}🔥' \
               f'{hbold("Скидка: ")}{item.get("discount") * 100}%\n'

        if index % 20 == 0:
            time.sleep(5)

        await message.answer(card)


@dp.message_handler(Text(equals='🔫 Снайперские винтовки'))
async def get_discount_rifles(message: types.Message):
    await message.answer('Пожалуйста подождите...')

    collect_data(weapon_type=4)

    with open('result.json', encoding='utf-8') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("name"), item.get("3d"))}\n' \
               f'{hbold("Цена: ")}${item.get("computed")}🔥' \
               f'{hbold("Скидка: ")}{item.get("discount") * 100}%\n'

        if index % 20 == 0:
            time.sleep(5)

        await message.answer(card)


@dp.message_handler(Text(equals='🧤 Перчатки'))
async def get_discount_gloves(message: types.Message):
    await message.answer('Пожалуйста подождите...')

    collect_data(weapon_type=13)

    with open('result.json', encoding='utf-8') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("name"), item.get("3d"))}\n' \
               f'{hbold("Цена: ")}${item.get("computed")}🔥' \
               f'{hbold("Скидка: ")}{item.get("discount") * 100}%\n'

        if index % 20 == 0:
            time.sleep(5)

        await message.answer(card)

@dp.message_handler(Text(equals='👊 Пистолеты'))
async def get_discount_rifles(message: types.Message):
    await message.answer('Пожалуйста подождите...')

    collect_data(weapon_type=5)

    with open('result.json', encoding='utf-8') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("name"), item.get("3d"))}\n' \
               f'{hbold("Цена: ")}${item.get("computed")}🔥' \
               f'{hbold("Скидка: ")}{item.get("discount") * 100}%\n'

        if index % 20 == 0:
            time.sleep(5)

        await message.answer(card)

@dp.message_handler(Text(equals='🦅 Пистолеты-Пулемёты'))
async def get_discount_rifles(message: types.Message):
    await message.answer('Пожалуйста подождите...')

    collect_data(weapon_type=6)

    with open('result.json', encoding='utf-8') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("name"), item.get("3d"))}\n' \
               f'{hbold("Цена: ")}${item.get("computed")}🔥' \
               f'{hbold("Скидка: ")}{item.get("discount") * 100}%\n'

        if index % 20 == 0:
            time.sleep(5)

        await message.answer(card)

@dp.message_handler(Text(equals='🤖 Штурмовые Винтовки'))
async def get_discount_rifles(message: types.Message):
    await message.answer('Пожалуйста подождите...')

    collect_data(weapon_type=3)

    with open('result.json', encoding='utf-8') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("name"), item.get("3d"))}\n' \
               f'{hbold("Цена: ")}${item.get("computed")}🔥' \
               f'{hbold("Скидка: ")}{item.get("discount") * 100}%\n'

        if index % 20 == 0:
            time.sleep(5)

        await message.answer(card)

@dp.message_handler(Text(equals='🩸 Дробовики'))
async def get_discount_rifles(message: types.Message):
    await message.answer('Пожалуйста подождите...')

    collect_data(weapon_type=7)

    with open('result.json', encoding='utf-8') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("name"), item.get("3d"))}\n' \
               f'{hbold("Цена: ")}${item.get("computed")}🔥' \
               f'{hbold("Скидка: ")}{item.get("discount") * 100}%\n'

        if index % 20 == 0:
            time.sleep(5)

        await message.answer(card)

@dp.message_handler(Text(equals='☠ Пулемёты'))
async def get_discount_rifles(message: types.Message):
    await message.answer('Пожалуйста подождите...')

    collect_data(weapon_type=8)

    with open('result.json', encoding='utf-8') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("name"), item.get("3d"))}\n' \
               f'{hbold("Цена: ")}${item.get("computed")}🔥' \
               f'{hbold("Скидка: ")}{item.get("discount") * 100}%\n'

        if index % 20 == 0:
            time.sleep(5)

        await message.answer(card)

def main():
    executor.start_polling(dp)


if __name__ == '__main__':
    main()
