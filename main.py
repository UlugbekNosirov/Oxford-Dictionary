import logging

from aiogram import Bot, Dispatcher, executor, types
from ocfordlookup import getDefinition
from googletrans import Translator

translater = Translator()

API_TOKEN = '5270649322:AAGOJHi5Eh3lZTOOvhexPAgDrMIwVbgRSRs'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi I'm Translator!\nYou can send me any message😊.\n"
                        "You can get it's English description and pronunciation✅\n"
                        "📞 - Contact : +998903083823\n"
                        "🧑‍💻- Developer: Ulug`bek Nosirov\n"
                        "🧑‍🏫- Teacher: Sariq Dev [Anvar Narzullayev]\n")


@dp.message_handler()
async def trans_lang(message: types.Message):
    lang = translater.detect(message.text).lang
    if len(message.text.split()) > 2:
        dest = 'uz' if lang == 'en' else 'en'
        await message.reply(translater.translate(message.text, dest).text)
    else:
        if lang == 'en':
            word_id = message.text
        else:
            word_id = translater.translate(message.text, dest='en').text
        lookup = getDefinition(word_id)
        if lookup:
            await message.reply(f"Word: {word_id} \nDefinitions: \n{lookup['definitions']}")
            if lookup.get('audio'):
                await message.reply_audio(lookup['audio'])
        else:
            await message.answer("Bunday so`z topilmadi🙅‍♂️")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)