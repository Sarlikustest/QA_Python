import time
#импортирую сам вебдрайвер
from selenium import webdriver
#импортирую класс By который ищет элемент на странице
from selenium.webdriver.common.by import By


#иницилизирую драйвер браузера
driver = webdriver.Chrome()






# через get мы говорим браузеру что обращаемся к странице
driver.get('https://erikdark.github.io/Qa_autotest_02/')

#с помощью команды find_element(и класса By внутри ) мы ишем нужный элемент на странце сайта, в качестве аргумента мы передаем класс поиска By и значение которое ищем.
inputs = driver.find_elements(By.CSS_SELECTOR, "input")
for i in inputs:
    i.send_keys('text')
    

btn = driver.find_element(By.ID,'submitBtn')
#с помощью click() мы кликаем по кнопке
time.sleep(1)
btn.click()
# использовать метод time.sleep - очень плохо

time.sleep(5)

driver.quit()