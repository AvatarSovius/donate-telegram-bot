#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Basic example for a bot that uses inline keyboards.
# This program is dedicated to the public domain under the CC0 license.
"""
import logging
import random

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

import settings

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def create_form(bot, update, user_data):
    check_numbers = random.randint(1000, 100000)
    link = "https://w.qiwi.com/payment/form/99?currency=RUB&amountInteger=50&extra['account']={}&extra['comment']={}".format(
        settings.QIWI_NUMBER, check_numbers)


def start(bot, update):
    keyboard = [[InlineKeyboardButton("100",
                                      url="https://qiwi.com/payment/form/99?extra['account']=79991112233&amountInteger=100&amountFraction=0&extra['comment']=Donations&currency=643".format(
                                          settings.QIWI_NUMBER)),
                 InlineKeyboardButton("200",
                                      url="https://qiwi.com/payment/form/99?extra['account']=79991112233&amountInteger=200&amountFraction=0&extra['comment']=Donations&currency=643".format(
                                          settings.QIWI_NUMBER)),
                 InlineKeyboardButton("500",
                                      url="https://qiwi.com/payment/form/99?extra['account']=79991112233&amountInteger=500&amountFraction=0&extra['comment']=Donations&currency=643".format(
                                          settings.QIWI_NUMBER))],

                [InlineKeyboardButton("Другая сумма", url="https://qiwi.com/payment/form/99?extra['account']=79991112233&amountInteger=&amountFraction=0&extra['comment']=Donations&currency=643")]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Сколько вы хотите задонатить?', reply_markup=reply_markup)




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
