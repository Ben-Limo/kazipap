# -*- coding: utf-8 -*-
import os
import json 
import traceback
import logging
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "443890184:AAHRfrEeWzD_6yTnx8CBqHgcJ6sp2iyqt6M"
PORT = int(os.environ.get('PORT', '5000'))
updater = Updater(TOKEN)


def start(bot, update):
    keyboard = [[InlineKeyboardButton("learn about Ben", callback_data='learn')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
    			'Hi there.\n\n\n' +
       			'I am Kibe the personal assistant of Ben limo, a freelance I.T consultant.\n' +
       			'Want to learn about Ben....\n' +
       			'simply click below.', 
       			reply_markup=reply_markup)


def button(bot, update):
    if update.callback_query.data == "learn":
        bot.editMessageText(chat_id=update.callback_query.message.chat.id, message_id=update.callback_query.message.message_id, text="I can tell you a bunch of stuff about Ben. Hit me with what interests you")
        bot.editMessageReplyMarkup(
				chat_id=update.callback_query.message.chat.id, 
				message_id=update.callback_query.message.message_id, 
				reply_markup=telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton("Education", callback_data="education"),
															 telegram.InlineKeyboardButton("Internships", callback_data="intern")]]))

    if update.callback_query.data == "education": 
    	bot.editMessageText(chat_id=update.callback_query.message.chat.id, message_id=update.callback_query.message.message_id, text=
	    	'He was always a visionary with a deep passion in the advancement of technology and making life more simple and exciting. \n\n' +
			'And when he heard from a guest speaker pursuing Computer Science during his final year in high school. He knew exactly what he wanted to do')
    	bot.editMessageReplyMarkup(
				chat_id=update.callback_query.message.chat.id, 
				message_id=update.callback_query.message.message_id, 
				reply_markup=telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton("Degree", callback_data="degree"),telegram.InlineKeyboardButton("Certification", callback_data="cert")],[telegram.InlineKeyboardButton("Mathematics", callback_data="math")]
				]))

    if update.callback_query.data == "degree":
    	bot.editMessageText(chat_id=update.callback_query.message.chat.id, message_id=update.callback_query.message.message_id, text=
			'A young and focused Ben Limo, joined Multimedia University (nairobi) in the year 2012 to pursue a Bachelors Degree in Mathematics and Computer Science.\n' +
			'He graduated with a Second class honors (lower division) in the year 2016.')  	
    	bot.editMessageReplyMarkup(
				chat_id=update.callback_query.message.chat.id, 
				message_id=update.callback_query.message.message_id,
				reply_markup=telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton("Back", callback_data="back")]]))

    if update.callback_query.data == "back":
    	bot.editMessageText(chat_id=update.callback_query.message.chat.id, message_id=update.callback_query.message.message_id, text=
	    	'He was always a visionary with a deep passion in the advancement of technology and making life more simple and exciting. \n\n' +
			'And when he heard from a guest speaker pursuing Computer Science during his final year in high school. He knew exactly what he wanted to do')
    	bot.editMessageReplyMarkup(
				chat_id=update.callback_query.message.chat.id, 
				message_id=update.callback_query.message.message_id, 
				reply_markup=telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton("Degree", callback_data="degree"),telegram.InlineKeyboardButton("Certification", callback_data="cert")],[telegram.InlineKeyboardButton("Mathematics", callback_data="math")]
				]))

    if update.callback_query.data == "cert":
    	bot.editMessageText(chat_id=update.callback_query.message.chat.id, message_id=update.callback_query.message.message_id, text=
	    	'Inorder to ready himself for the competitive I.T sphere and reinvent himself as an indisposible asset for corporations, he has done all the vital certificaions. \n\n' +
			'That is to say:- \n' +
			'1. Cisco-CCNA certifaction. \n' +
			'2. ICDL Microsoft Office suite certifaction.')
    	bot.editMessageReplyMarkup(
				chat_id=update.callback_query.message.chat.id, 
				message_id=update.callback_query.message.message_id,
				reply_markup=telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton("message me", url='t.me/Tuweobot')],[telegram.InlineKeyboardButton("Back", callback_data="education")]
					]))

    if update.callback_query.data == "math":
    	bot.editMessageText(chat_id=update.callback_query.message.chat.id, message_id=update.callback_query.message.message_id, text=
    		'Since childhood Ben had a innate knack for Math, achieving straight As in both KCPE and KCSE. So it did not come as a surprise when in his 3rd year at the O-levels he went ahead to major in Pure mathematics. \n\n' +
			'He has always had a secret passion for numbers and intends to enroll for Masters in september of 2018.')
    	bot.editMessageReplyMarkup(
				chat_id=update.callback_query.message.chat.id, 
				message_id=update.callback_query.message.message_id,
				reply_markup=telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton("Learn more", callback_data="more")]
					]))

    if update.callback_query.data == "more":
	   	bot.editMessageText(chat_id=update.callback_query.message.chat.id, message_id=update.callback_query.message.message_id, text=
	   		'It may sound hillarious but its quiet true. Burried deep in his soul he has this unsatisfiable desire to lecture University student. Maybe at a later life, in the footsteps of his mother who is a teacher.')
	   	bot.editMessageReplyMarkup(
					chat_id=update.callback_query.message.chat.id, 
					message_id=update.callback_query.message.message_id,
					reply_markup=telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton("message me", url='t.me/Tuweobot')],[telegram.InlineKeyboardButton("Back", callback_data="education")]]))

    if update.callback_query.data == "intern":
	   	bot.editMessageText(chat_id=update.callback_query.message.chat.id, message_id=update.callback_query.message.message_id, text=
	   		'Aha... This will give you a glimpse into the experience that he has gunnered from all the major Telecommunication and I.T companies in the country.')
	   	bot.editMessageReplyMarkup(
					chat_id=update.callback_query.message.chat.id, 
					message_id=update.callback_query.message.message_id,
					reply_markup=telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton("Kenic", callback_data="kenic")],[telegram.InlineKeyboardButton("Safaricom", callback_data="saf"),telegram.InlineKeyboardButton("ICTA", callback_data="icta")],[telegram.InlineKeyboardButton("Telkom Kenya", callback_data="telkom")]
				]))

def main():
    # Create the Updater and pass it your bot's token.
    TOKEN = "443890184:AAHRfrEeWzD_6yTnx8CBqHgcJ6sp2iyqt6M"
    PORT = int(os.environ.get('PORT', '8443'))
    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
    updater.bot.set_webhook("https://kazipap.herokuapp.com/" + TOKEN)

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()