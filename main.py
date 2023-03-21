import asyncio
import logging
import dataset
import emoji

from random import randint

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN="" # your token here

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Привет. Зажжем сегодня? 💋 Пиши /chat")

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.answer("Меня зовут Маришка, я люблю общаться. Пиши /chat, чтобы развлечься 🙈🔥")

@dp.message_handler(commands=['chat'])
async def send_welcome(message: types.Message):
    await message.answer(dataset.random_horny() + " " + emoji.random_emoji())


@dp.message_handler()
async def reply(message: types.Message):
    a = randint(0, 1)
    if a == 0:
        await message.answer("Я бы обнялаа тебя " + str(randint(0, 1000)) + " раз " + emoji.random_emoji())
    else:
        await message.answer(dataset.random_love() + " " + emoji.random_emoji())
    b = randint(0, 10)
    if b == 5:
        await asyncio.sleep(0.5)
        await message.answer("Может развлечемся? 😘 Пиши /chat")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)