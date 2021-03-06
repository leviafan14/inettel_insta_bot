# -*- coding: utf-8 -*-
import Inettel_insta_bot
from Inettel_insta_bot import InettelInstaBot
#Данные для авторизации
username = ''
password = ''

# Запуск бота
if __name__ == '__main__':
    instabot=InettelInstaBot(username,password)
    instabot.login()
    instabot.get_like()
    instabot.storis()
    #instabot.subscribe()
