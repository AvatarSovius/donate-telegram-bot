#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Basic example for a bot that uses inline keyboards.
# This program is dedicated to the public domain under the CC0 license.
"""
import logging
import config

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


text = '''
☘️ Поддержите нас

Ваша поддержка позволит активно добавлять новые возможности, улучшать стабильность канала и оплачивать сервера.
Так же вы можете совершить ваши пожретвования криптовалютой:

ETH - 0x19739D5B00E19E3D47676F3c8edc68b1230eb940
BTC - 1343yMRidF9YH7WqqkD4JAKsimVc1V47Cg

С уважением, команда ParlamentCLUB 🎈
'''

keyboard = [[InlineKeyboardButton(" 100₽ ",
                                      url=config.LINK),
                 InlineKeyboardButton(" 250₽ ",
                                      url=config.LINK),
                 InlineKeyboardButton(" 500₽ ",
                                      url=config.LINK)],

                [InlineKeyboardButton(" Другая сумма ",
                                      url=config.LINK)]]

reply_markup = InlineKeyboardMarkup(keyboard)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=text, reply_markup=reply_markup)


def help(bot, update):
    update.message.reply_text("Use /start to test this bot.")

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def post(bot, update):
    bot.send_message(chat_id="@parlament_club7", text=text, reply_markup = reply_markup)

def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(config.TOKEN)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_error_handler(error)
    updater.dispatcher.add_handler(CommandHandler('post', post))
    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
