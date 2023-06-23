"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
from imlo import wordcheck
from transliterate import to_cyrillic, to_latin



from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5825136192:AAFli03LYm8w2gKQJIC0rVyH_j43RQ2da5Q'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Imlo botga xush kelibsiz")
@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Bo'tni ishga tushurish uchun start buyrug'uni yuboring")


@dp.message_handler()
async def checkimlo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    word1 = message.text
    words = word1.split(' ')
    for word in words:
        result = wordcheck(word)
        javob = lambda word: to_cyrillic(word) if word.isascii() else to_latin(word)
        if result['availabe']:
            response = f"✅{javob(word.capitalize())}"
        else:
            response = f"❌{javob(word.capitalize())}\n"
            for text in result['matches']:
                response += f"✅{javob(text.capitalize())}\n"
        await message.reply(response)
   


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)