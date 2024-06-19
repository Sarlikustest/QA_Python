import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    time.sleep(5)
    # time.sleep(5)
    driver.quit()

def test_registration(driver):
    test_data = ['Ivan', 'ivan@peter.ru', '123']

    driver.get('https://erikdark.github.io/zachet_selenium_01/index.html')

    reg_href = driver.find_element(By.LINK_TEXT, 'Регистрация').click()

    # for i in range(len(test_data)):
    #     log_btns = driver.find_elements(By.TAG_NAME, 'label')
    #     log_btns[i].send_keys(test_data[i])
    name = driver.find_element(By.ID, 'name')
    name.send_keys(test_data[0])

    email = driver.find_element(By.ID, 'email')
    email.send_keys(test_data[1])

    password = driver.find_element(By.ID, 'password')
    password.send_keys(test_data[2])

    reg_btn = driver.find_element(By.TAG_NAME, 'button').click()

    success_text = driver.find_element(By.TAG_NAME, 'p')
    success_text = success_text.text
    assert success_text == 'Пользователь зарегистрирован'

    