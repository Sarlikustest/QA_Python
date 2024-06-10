import time
#импортирую сам вебдрайвер
from selenium import webdriver
#импортирую класс By который ищет элемент на странице
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import re




#иницилизирую драйвер браузера
driver = webdriver.Chrome()




try:
    driver.get('https://erikdark.github.io/QA_autotests_14/')
    time.sleep(3)
   
    btn = driver.find_element(By.ID,'verify').click()
    message = driver.find_element(By.ID,'verify_message')
    assert 'Verification successful!' in message.text
   
   




finally:
    time.sleep(5)
    driver.quit()
