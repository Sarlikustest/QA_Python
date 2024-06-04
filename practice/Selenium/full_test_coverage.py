import time
#импортирую сам вебдрайвер
from selenium import webdriver
#импортирую класс By который ищет элемент на странице
from selenium.webdriver.common.by import By


#иницилизирую драйвер браузера

def test_coverage():

    name = input()

    lastName = input()

    email = input()

    j = 0
    while True:

        for i in email:
            if i == '@':
                j =+ 1
        if j < 1:
            return False


        driver = webdriver.Chrome()






        driver.get('https://erikdark.github.io/Qa_autotest_03/')


        input_name = driver.find_element(By.NAME, "firstName" )

        input_name.send_keys(name)

        time.sleep(1)

        input_lastname = driver.find_element(By.NAME, "lastName" )

        input_lastname.send_keys(lastName)

        time.sleep(1)

        input_email = driver.find_element(By.NAME, "email" )


        input_email.send_keys(email)



        time.sleep(1)



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
        return False

test_coverage()