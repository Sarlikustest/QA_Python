
import time
#импортирую сам вебдрайвер
from selenium import webdriver
#импортирую класс By который ищет элемент на странице
from selenium.webdriver.common.by import By


#иницилизирую драйвер браузера
driver = webdriver.Chrome()






driver.get('https://erikdark.github.io/Qa_autotest_03/')

try:
    input_phone = driver.find_element(By.NAME, "phone")

    input_phone.send_keys('hhfh')

    time.sleep(1)

    input_address = driver.find_element(By.NAME, "address" )

    input_address.send_keys('hhfh')



    time.sleep(5)




    btn = driver.find_element(By.TAG_NAME, "button")

    if btn.click():
        print("OK")
    else:
        print("error!")

    time.sleep(5)
except Exception as ex:
    print(ex)





driver.quit()