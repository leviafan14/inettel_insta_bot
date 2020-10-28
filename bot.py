from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from data import username, password
import time
import random

username='inettel.provider'
password='8845svmIns'
browser = webdriver.Chrome('D:/my files/develop/InstaBot/chromedriver/chromedriver')
#авторизация
def login(username, password):
    try:
        browser.get('https://www.instagram.com')
        time.sleep(random.randrange(3, 5))
        #Ввод логина
        username_input = browser.find_element_by_name('username')
        username_input.clear()
        username_input.send_keys(username)
        time.sleep(2)
        #Ввод пароля
        password_input = browser.find_element_by_name('password')
        password_input.clear()
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        time.sleep(10)
        element = browser.find_element_by_class_name('sqdOP')
        element.click()
        time.sleep(3)
        element = browser.find_element_by_class_name('aOOlW.HoLwm')
        element.click()
        time.sleep(3)
        storis()
        #browser.close()
        #browser.quit()
    except Exception as e:
        print(e)
        #browser.close()
        #browser.quit()
        
#Просмотр сторис
def storis():
    try:
        storis= browser.find_element_by_class_name('Ckrof')
        storis.click()
    except Exception as e:
        print(e)
        
login(username, password)
