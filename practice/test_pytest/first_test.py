from selenium import webdriver

from selenium.webdriver.common.by import By



def test_case1():
    try:
        driver = webdriver.Chrome()
        driver.get('https://erikdark.github.io/PyTest_01_reg_form/')

        name = driver.find_element(By.ID, 'username')
        name.send_keys('PETER')

        name = driver.find_element(By.ID, 'email')
        name.send_keys('gfgf@hfhhf.ru')

        name = driver.find_element(By.ID, 'password')
        name.send_keys('12345')

        btn = driver.find_element(By.TAG_NAME, 'button')
        btn.click()

        text = driver.find_element(By.ID, 'success-message')
        text = text.text

        assert text == 'Вы успешно зарегистрированы!'

    finally:
        driver.quit()


def test_case2():
    try:
        driver = webdriver.Chrome()
        driver.get('https://erikdark.github.io/PyTest_01_reg_form/')

        name = driver.find_element(By.ID, 'username')
        name.send_keys('PETER')

        name = driver.find_element(By.ID, 'email')
        name.send_keys('gfgfhfhhf.ru')

        name = driver.find_element(By.ID, 'password')
        name.send_keys('12345')

        btn = driver.find_element(By.TAG_NAME, 'button')
        btn.click()

        text = driver.find_element(By.ID, 'success-message')
        text = text.text

        assert text == 'Вы успешно зарегистрированы!', 'Неправильно заполнена форма'

    finally:
        driver.quit()
