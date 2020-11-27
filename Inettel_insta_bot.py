# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

#Описание класса бота
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
            
            #Закрытие всплывающих окон после авторизации
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
        fragment_storis=[]
        time.sleep(3)
        try:
            browser = self.browser
            browser.get('https://www.instagram.com')
            time.sleep(3)
            storis=browser.find_element_by_class_name('Ckrof')
            storis.click()
            while True:
                try:
                    time.sleep(2)
                    line_progress=browser.find_element_by_class_name('-Nmqg')
                except Exception as except_progress:
                    print('error progress line', except_progress)
                    break
                try:
                    time.sleep(2)
                    next_storis_button=browser.find_element_by_class_name('coreSpriteRightChevron')
                    time.sleep(1)
                    next_storis_button.click()
                except Exception as ex:
                    print('coreSpriteRightChevron ',ex)        
            self.close_browser()
        except Exception as storis_exception:
            print('storis_exception ',storis_exception)
            time.sleep(random.randrange(3,20))
            self.close_browser()
        return 1


    #Ставим лайк на запись 
    def get_like(self):
        #Получаем ссылки на указанное количество постов
        browser = self.browser
        browser.get('https://www.instagram.com')
        urls_set=set()
        count=1
        body = browser.find_element_by_tag_name('body')
        
        #Здесь указано количество ссылок на посты, которые н нужно посмотреть
        count_posts=random.randrange(9, 12)
        print('Будет просмотрено:', count_posts)
        while len(urls_set)<=count_posts:
            
            #эмитация нажатия кнопки Page down для прокрутки страницы
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(3)
            href = browser.find_element_by_class_name('c-Yi7')
            try:
                #Проверяем является ли полученная ссылка записью пользователя,
                #Если является, то добавляем её во множество
                if "/p/" in href.get_attribute('href'):
                    urls_set.add(href.get_attribute('href'))
                    count+=1
                    print('iteracion: ',count,' len :',len(urls_set))
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
                    #Проверка, если лайка нет, то бот его ставит
                    if fill=='#262626' and label=='Нравится':
                         print('Ставлю лайк')
                         time.sleep(3)
                         like_button =browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
                         break
                         time.sleep(3)
                    #Если лайк есть, то бот выходит из цикла svg
                    elif fill=='#ed4956' and label=='Не нравится':
                        print('Уже есть лайк')
                        break
                    else:
                        pass
                time.sleep(random.randrange(3))
            except Exception as ex:
                print(ex)
 
    
    #Подписываемся на пользователей
    def subscribe(self):
        browser = self.browser
        browser.get('https://www.instagram.com/explore/people/suggested/')
        users_links=set()
        #Отсчет для подписки на пользователей
        count=1
        #Рандомное количество пользователей на которых подпишется бот
        count_new_subscribes=random.randrange(3, 5) 
        time.sleep(5)
        print('Количество новых подписок:', count_new_subscribes)
        
        #Получаем ссылки на аккаунты
        users=browser.find_elements_by_class_name('FPmhX.notranslate.MBL3Z')
        for i in users:
            if count<=count_new_subscribes:
                users_links.add(i.get_attribute('href'))
                count+=1
            else:
                break
        for user_url in users_links:
            browser.get(user_url)
            time.sleep(3)
            #Если профиль закрытый - то его пропускаем и
            #переходим к следующему пользователю
            try:
                browser.find_element_by_class_name('rkEop')
                print('Закрытый аккаунт, его пропускаем')
                continue
            except Exception:
                print('Открытый профиль')
        
            #Получаем кнопку и проверяем, является ли она кнопкой "Подписаться"
            try:
                subscribe_button=browser.find_element_by_class_name('_5f5mN.jIbKX._6VtSN.yZn4P')
                text=subscribe_button.text #Получаем текст кнопки
                if text=='Подписаться':
                    print(text,' - Профиль открыт, аккаунт на нас не подписан')
                    subscribe_button.click()
                    continue
                else:
                    continue
            except Exception as e:
            #Если кнопка не найдена по классу, то возбуждаем исключение
                print('Ошибка. Кнопка Подписаться не найдена ',e)
            
            #Получаем кнопку и проверяем, является ли она кнопкой "Подписаться в ответ"
            try:
                subscribe_button=browser.find_element_by_class_name('_5f5mN.jIbKX._6VtSN.yZn4P')
                text=subscribe_button.text #Получаем текст кнопки
                if text=='Подписаться в ответ':
                    print(text,' - Профиль открыт, аккаунт подписан на нас')
                    subscribe_button.click()
                else:
                    continue
            except Exception as e:
                print('Ошибка. Кнопка Подписаться в ответ не найдена ',e)
                
            #выжидаем случайный период времени перед след. аккаунтом
            time.sleep(random.randrange(3, 5))
        print (users_links)
        browser.get('https://www.instagram.com/explore/people/suggested/')
        return 1
