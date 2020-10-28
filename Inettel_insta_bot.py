# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import random
from bs4 import BeautifulSoup
import requests

username='inettel.provider'
password='8845svmIns'

class InettelInstaBot():
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.browser=webdriver.Chrome('D:/my files/develop/InstaBot/chromedriver/chromedriver')

    #Закрытие браузера
    def close_browser(self):
        self.browser.close()
        self.browser.quit()

    #Авторизация
    def login(self):
        try:
            browser = self.browser
            browser.get('https://www.instagram.com')
            time.sleep(random.randrange(3, 5))
            #Ввод логина
            username_input = browser.find_element_by_name('username')
            username_input.clear()
            username_input.send_keys(self.username)
            time.sleep(2)
            #Ввод пароля
            password_input = browser.find_element_by_name('password')
            password_input.clear()
            password_input.send_keys(self.password)
            password_input.send_keys(Keys.ENTER)
            time.sleep(10)
            #Подтверждение закрытия окон после авторизации
            try:
                element = browser.find_element_by_class_name('sqdOP')
                element.click()
                time.sleep(3)
            except Exception as e:
                print('Окно не обнаружено ', e)
            try:
                element = browser.find_element_by_class_name('aOOlW.HoLwm')
                element.click()
                time.sleep(3)
            except Exception as e:
                print('Окно не обнаружено ', e)
        except Exception as main_auth_except:
            print(main_auth_except)
        
    #Просмотр сторис
    def storis(self):
        time.sleep(3)
        try:
            browser = self.browser
            browser.get('https://www.instagram.com')
            storis=browser.find_element_by_class_name('Ckrof')
            storis.click()
            time.sleep(200)
            self.close_browser()
        except Exception as storis_exception:
            print(storis_exception)
            self.close_browser()

    #Получаем ссылки на посты и ставим лайк
    def scroll_page(self):
        #Получаем ссылки на указанное количество постов
        browser = self.browser
        browser.get('https://www.instagram.com')
        urls_set=set()
        count=0
        body = browser.find_element_by_tag_name('body')
        #Здесь указано количество ссылок на посты, которые н нужно посмотреть
        for i in range(0,8):
            #эмитация на нажатие кнопки Page down для прокрутки страницы
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(3)
            hrefs = browser.find_elements_by_tag_name('a')
            try:
                #Проверяем является ли полученная ссылка записью пользователя,
                #Если является, то добавляем её во множество
                urls_set = {i.get_attribute('href') for i in hrefs if "/p/" in i.get_attribute('href')}
                count+=1
                print(count)
            except Exception as e:
                print('error ', e)
            time.sleep(3)
        #Проверяем полученные ссылки на посты, если лайка нет, то ставим его
        print('len:',len(urls_set))
        for url in urls_set:
            try:
                browser.get(url)
                time.sleep(3)
                svg=browser.find_elements_by_tag_name('svg')
                print(url)
                for s in svg:
                    fill=s.get_attribute('fill')
                    label=s.get_attribute('aria-label')
                    #Проверка, лайка нет, то бот его ставит
                    if fill=='#262626' and label=='Нравится':
                         print(label)
                         time.sleep(3)
                         like_button =browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
                         break
                         time.sleep(3)
                    #Если лайк есть, то бот выходит из цикла svg
                    elif fill=='#ed4956' and label=='Не нравится':
                        print(label)
                        break
                    else:
                        pass
                time.sleep(random.randrange(3))
            except Exception as ex:
                print(ex)
        self.storis()
instabot=InettelInstaBot(username,password)
instabot.login()
instabot.scroll_page()
