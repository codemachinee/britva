from http.server import BaseHTTPRequestHandler
import telebot
import os
#from telebot import types
from apscheduler.schedulers.background import BackgroundScheduler
#from datetime import datetime
#from random import *

token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)


class handler(BaseHTTPRequestHandler):

    def video_otchet_admina():
        bot.send_message('@mytest_two', 'НАПОМИНАНИЕ: видео отчет Админа')


    def video_otchet_barberov():
        bot.send_message('@mytest_two', 'НАПОМИНАНИЕ: видео отчет Барберов')


    def otchet_admina_o_zakrytii():
        bot.send_message('@mytest_two', 'НАПОМИНАНИЕ: отчет Админа о закрытии смены')


    @bot.message_handler(commands=['status'])
    def status(message):
        bot.send_message(message.chat.id, 'бот запущен, все работает.')


    if __name__ == '__main__':
        scheduler = BackgroundScheduler()
        scheduler.add_job(video_otchet_admina, "cron", day_of_week='mon-sun', hour=7)
        scheduler.add_job(video_otchet_barberov, "cron", day_of_week='mon-sun', hour=19)
        scheduler.add_job(otchet_admina_o_zakrytii, "cron", day_of_week='mon-sun', hour=19, minute=10)
        scheduler.start()


    bot.polling()
