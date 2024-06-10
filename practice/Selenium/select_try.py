
import time
#импортирую сам вебдрайвер
from selenium import webdriver
#импортирую класс By который ищет элемент на странице
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    #иницилизирую драйвер браузера
    driver = webdriver.Chrome()


        # через get мы говорим браузеру что обращаемся к странице
    driver.get('https://erikdark.github.io/QA_autotests_09/')
    time.sleep(2)

    find = driver.find_element(By.CSS_SELECTOR, "#challenge")
    find_text = find.text
    clear_text = find_text.replace("?","")
    split_text = clear_text.split(' ')
    print(split_text)
    a = int(split_text[2])
    b = int(split_text[4])
    total = a+b
    total = str(total)
    print(total)
   
  
    select = Select(driver.find_element(By.TAG_NAME, 'select'))
    new = select.select_by_value(total)
    

    btn = driver.find_element(By.ID, "submitBtn")
    btn.click()

    time.sleep(20)

    text_try = driver.find_element(By.ID, "message")
    text_try = text_try.text
    if text_try == "You guessed it! Well done!":
        print('OK')

  
except Exception as ex:
    print(ex)


driver.quit()