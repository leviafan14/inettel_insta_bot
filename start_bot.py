# -*- coding: utf-8 -*-
import Inettel_insta_bot
from Inettel_insta_bot import InettelInstaBot
#Данные для авторизации
username='inettel.provider'
password='8845svmIns'

#Запуск бота
if __name__ == '__main__':
    instabot=InettelInstaBot(username,password)
    instabot.login()
    instabot.storis()
    instabot.get_like()
    #instabot.subscribe()
