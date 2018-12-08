#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Basic example for a bot that uses inline keyboards.
# This program is dedicated to the public domain under the CC0 license.
"""
import logging
import settings

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(bot, update):
    text = ''' 
Поддержите нас  ☘

Ваше пожертвование позволит активно добавлять новые возможности, улучшать стабильность канала и оплачивать сервера.


Так же вы можете совершить ваши пожретвования криптовалютой:

ETH - 0x19739D5B00E19E3D47676F3c8edc68b1230eb940
BTC - 1343yMRidF9YH7WqqkD4JAKsimVc1V47Cg


С уважением, команда ParlamentCLUB 🎈

'''

    keyboard = [[InlineKeyboardButton(" 100₽ 💰",
                                      url="https://www.donationalerts.ru/r/avatarsovas"),
                 InlineKeyboardButton(" 250₽ ❤",
                                      url="https://www.donationalerts.ru/r/avatarsovas"),
                 InlineKeyboardButton(" 500₽ ☘",
                                      url="https://www.donationalerts.ru/r/avatarsovas")],

                [InlineKeyboardButton("🔥 Другая сумма 🔥",
                                      url="https://www.donationalerts.ru/r/avatarsovas")]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_te1xt(text, reply_markup=reply_markup)


def help(bot, update):
    update.message.reply_text("Use /start to test this bot.")


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(settings.TELEGRAM_TOKEN)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
