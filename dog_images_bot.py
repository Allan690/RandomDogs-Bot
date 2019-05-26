from telegram.ext import Updater, CommandHandler
import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    image_url = contents['url']
    return image_url


def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)


def main():
    bot_token = os.getenv('BOT_TOKEN')
    print(".......starting bot..........")
    updater = Updater(bot_token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop', bop))
    updater.start_polling()
    print(".........bot started successfully........")
    updater.idle()


if __name__ == '__main__':
    main()
