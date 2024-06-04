import time
#импортирую сам вебдрайвер
from selenium import webdriver
#импортирую класс By который ищет элемент на странице
from selenium.webdriver.common.by import By


#иницилизирую драйвер браузера
driver = webdriver.Chrome()






# через get мы говорим браузеру что обращаемся к странице
driver.get('https://easysmarthub.ru/blog/')
time.sleep(2)
#с помощью команды find_element(и класса By внутри ) мы ишем нужный элемент на странце сайта, в качестве аргумента мы передаем класс поиска By и значение которое ищем.
input_one = driver.find_element(By.LINK_TEXT,'Что такое базы данных?')

time.sleep(2)

input_one.click()

time.sleep(5)
try:
    input_two = driver.find_element(By.LINK_TEXT,'Эрик Спичак')

    time.sleep(2)

    input_two.click()

    time.sleep(5)
except Exception as ex:
    print('такой ссылки нет')
    print(ex)

finally:
    driver.quit()