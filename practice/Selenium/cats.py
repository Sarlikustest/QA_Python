import time
#импортирую сам вебдрайвер
from selenium import webdriver
#импортирую класс By который ищет элемент на странице
from selenium.webdriver.common.by import By


#иницилизирую драйвер браузера
driver = webdriver.Chrome()






# через get мы говорим браузеру что обращаемся к странице
driver.get('https://erikdark.github.io/Qa_autotest_01/')
time.sleep(2)
#с помощью команды find_element(и класса By внутри ) мы ишем нужный элемент на странце сайта, в качестве аргумента мы передаем класс поиска By и значение которое ищем.
input_one = driver.find_element(By.ID,'inputField')


#с помощью send_keys(мы записываем данные в поле)
input_one.send_keys('Александр Абрамов')
time.sleep(5)

btn = driver.find_elements(By.CLASS_NAME,'btn')
#с помощью click() мы кликаем по кнопке


if len(btn) == 8:
    print(len(btn))
    print('da')
else:
    print('wrong number')

# использовать метод time.sleep - очень плохо



driver.quit()