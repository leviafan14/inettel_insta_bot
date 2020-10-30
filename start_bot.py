import Inettel_insta_bot
from Inettel_insta_bot import InettelInstaBot
#Данные для авторизации
username='inettel.provider'
password='8845svmIns'
#Запуск бота
if __name__ == '__main__':
    while True:
        instabot=InettelInstaBot(username,password)
        instabot.login()
        instabot.get_like()
        time.sleep(random.randrange(10800,21600))
