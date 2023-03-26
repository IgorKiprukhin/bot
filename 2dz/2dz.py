import os.path
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from bs4 import BeautifulSoup
import requests
import random
from config import *

bot = telebot.TeleBot("6019421547:AAE_EyqkbuoaqOyCOCi0v_gYwKvDMYBcujI")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	if message.text == "/start":
		keyboard = InlineKeyboardMarkup()
		keyboard.add(InlineKeyboardButton(text='Овен ♈️', callback_data='aries'),InlineKeyboardButton(text='Телец ♉️', callback_data='taurus'))
		keyboard.add(InlineKeyboardButton(text='Близнецы ♊️', callback_data='gemini'),InlineKeyboardButton(text='Рак ♋️', callback_data='cancer'))
		keyboard.add(InlineKeyboardButton(text='Лев ♌️', callback_data='leo'),InlineKeyboardButton(text='Дева ♍️', callback_data='virgo'))
		keyboard.add(InlineKeyboardButton(text='Весы ♎️', callback_data='libra'),InlineKeyboardButton(text='Скорпион ♏️', callback_data='scorpio'))
		keyboard.add(InlineKeyboardButton(text='Стрелец ♐️', callback_data='sagittarius'),InlineKeyboardButton(text='Козерог ♑️', callback_data='capricorn'))
		keyboard.add(InlineKeyboardButton(text='Водолей ♒️', callback_data='aquarius'),InlineKeyboardButton(text='Рыбы ♓️', callback_data='pisces'))
		bot.send_message(message.from_user.id, text="⚛️ Выберите Ваш знак зодиака:", reply_markup=keyboard)
		f = open(f'{message.from_user.id}.sub', 'w', encoding='utf-8')
		f.write(f'{message.from_user.first_name}\n{message.from_user.last_name}\n{message.from_user.username}\n')
		f.close()



@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
	url = requests.get('https://horo.mail.ru/prediction/'+call.data+'/today/')
	s = BeautifulSoup(url.text, 'html.parser')
	title = s.find("h1", {"class": "hdr__inner"}).getText()
	date = s.find("span", {"class": "link__text"}).getText()
	text = s.find("div", {"class": "article__item_alignment_left"}).getText()
	emoji = ['😎', '🌤', '🌥', '☀️', '⛅️', '🌦', '🌞', '🌻', '🌅', '🌄', '🌇', '🌆']
	content = '<b>'+random.choice(emoji)+' <a href="https://t.me/DHoroBot">'+title+'</a></b>\n\n<b>🗓 '+date+'</b>\n\n💬 '+text+'\n<tg-spoiler><i>🔽 Хорошего дня!!!\nМой ТГ 👉 @The_Kipr</i></tg-spoiler>'
	bot.send_message(call.message.chat.id, content, parse_mode="html", disable_web_page_preview=True)

bot.infinity_polling(interval=0)