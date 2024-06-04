import time
#импортирую сам вебдрайвер
from selenium import webdriver
#импортирую класс By который ищет элемент на странице
from selenium.webdriver.common.by import By


#иницилизирую драйвер браузера
driver = webdriver.Chrome()






driver.get('https://erikdark.github.io/Qa_autotest_03/')

input_name = driver.find_element(By.NAME, "firstName" )

input_name.send_keys('hhfh')

time.sleep(1)

input_lastname = driver.find_element(By.NAME, "lastName" )

input_lastname.send_keys('hhfh')

time.sleep(1)

input_email = driver.find_element(By.NAME, "email" )

try:
    input_email.send_keys('hhfhmfil.ru')
except:
    input_email.send_keys('hhfhm@fil.ru')

time.sleep(1)

input_phone = driver.find_element(By.NAME, "phone")

input_phone.send_keys('hhfh')

time.sleep(1)

input_address = driver.find_element(By.NAME, "address" )

input_address.send_keys('hhfh')

time.sleep(5)




btn = driver.find_element(By.TAG_NAME, "button")

btn.click()

time.sleep(5)

find_text = driver.find_element(By.TAG_NAME, "h2")
welcome_text = find_text.text

assert"Поздравляю, вы прошли первый уровень." == welcome_text 

# или второй вариант
# if welcome_text == "Поздравляю, вы прошли первый уровень.":
#     print('Test passed!')



driver.quit()