
import re
import time
#импортирую сам вебдрайвер
from selenium import webdriver
#импортирую класс By который ищет элемент на странице
from selenium.webdriver.common.by import By

try:
    #иницилизирую драйвер браузера
    driver = webdriver.Chrome()






        # через get мы говорим браузеру что обращаемся к странице
    driver.get('https://erikdark.github.io/Qa_autotest_07/')


        
    missed_number = driver.find_element(By.CSS_SELECTOR, "#numberImage")

    a = missed_number.get_attribute("data-b")
    a = a[3:]
    a = int(a)


    first_number = driver.find_element(By.CSS_SELECTOR, "#challenge")
    true_number = first_number.text
    true_number = true_number.split(' ')

    at_least = int(true_number[2])
    true_sum = a + at_least


    form = driver.find_element(By.CSS_SELECTOR, "#answer")
    form.send_keys(true_sum)

    time.sleep(5)

    btn = driver.find_element(By.CSS_SELECTOR, "#submitBtn")
    btn.click()
except Exception as ex:
    print(ex)


driver.quit()