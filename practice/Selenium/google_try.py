import time
#импортирую сам вебдрайвер
from selenium import webdriver
#импортирую класс By который ищет элемент на странице
from selenium.webdriver.common.by import By


#иницилизирую драйвер браузера
driver = webdriver.Chrome()






# через get мы говорим браузеру что обращаемся к странице
driver.get('https://www.google.com/')
time.sleep(2)
#с помощью команды find_element(и класса By внутри ) мы ишем нужный элемент на странце сайта, в качестве аргумента мы передаем класс поиска By и значение которое ищем.
input_one = driver.find_element(By.ID,'APjFqb')


#с помощью send_keys(мы записываем данные в поле)
input_one.send_keys('Александр Абрамов')
time.sleep(5)

btn = driver.find_element(By.NAME,'btnK')
#с помощью click() мы кликаем по кнопке
btn.click()
time.sleep(5)


# использовать метод time.sleep - очень плохо



driver.quit()