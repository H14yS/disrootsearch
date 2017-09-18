#!/usr/bin/env python
#Copyright 2017 deerf, this code is under GPLv3
import telebot, time, urllib, emoji
from telebot import types

def long_url(text):
    text = urllib.parse.quote_plus(text)
    long_url = 'https://search.disroot.org/search?q='+ text
    return long_url

bot = telebot.TeleBot('TOKEN')

@bot.inline_handler(func=lambda m: True)
def query_text(inline_query):
    try:
        print(str(inline_query.from_user.id) + ' ' + inline_query.query)
        l_url = types.InlineQueryResultArticle('long_url', 'Long url', types.InputTextMessageContent(emoji.emojize(':mag: searching...\n',use_aliases=True)+long_url(inline_query.query)),description=emoji.emojize(':mag: Search anythings: inline_query.query',use_aliases=True))
        bot.answer_inline_query(inline_query.id, [l_url])
    except Exception:
         print('Erro: ' + inline_query.query)
         pass

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome!\n')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    info = (
        'please, talk to me!\nTwitter: realdeerf\n'
        'Telegram: @entjt\n'
        'Website: http://freddyz.xyz\n'
        'Blog: http://blog.freddyz.xyz\n'
        'Source code: https://github.com/freddyxs/disrootsearch')
    bot.reply_to(message, info)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    url = long_url(message.text)
    bot.reply_to(message, 'Long url:\n'+ url, disable_web_page_preview=True)

try: 
    bot.polling(none_stop=True)
except urllib.error.HTTPError:
    time.sleep(10)
while True:
    time.sleep(20)
