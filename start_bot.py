import Inettel_insta_bot
from Inettel_insta_bot import InettelInstaBot
#Данные для авторизации
<<<<<<< HEAD
username='username'
password='password'

=======
username='user.name'
password='password'
>>>>>>> c8ded6925494d959a752715b4e6c115347bb50cf
#Запуск бота
if __name__ == '__main__':
    instabot=InettelInstaBot(username,password)
    instabot.login()
    instabot.get_like()
