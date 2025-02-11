#!/usr/bin/python
# -*- coding: utf8 -*-

""" Файл для хранения конфигурации, паролей и т.д """

import telebot
import requests
import psycopg2
import heroku3

HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6)"
           "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87"
           "Safari/537.36"}

##
token = '<token>'
token2 = '<token>'

bot = telebot.TeleBot(token, threaded=True)

# Если есть рекурсионные ошибки вписать: threaded=False
# Многопоточность автоматически включена (при выключении
# бот становится медленней)

s = requests.session()
heroku_conn = heroku3.from_key('<token heroku>')
app = heroku_conn.apps()['https://github.com/Imran95942/telegram-bot-v2']
version = len(app.releases()) / 100

chat_id = "<id>"
user_id = "<id>"
group_id = "<name_group>"

conn = psycopg2.connect(dbname='<dbname>', user='<user>',
                        password='<password>', host='<host>')
