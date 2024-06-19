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
    driver.quit()

def test_registration(driver):

    # test_data = ['Ivan', 'ivan@peter.ru', '123']

    driver.get('https://erikdark.github.io/zachet_selenium_01/index.html')

    log_btn = driver.find_element(By.LINK_TEXT, 'Профиль').click()

   

    log_out_btn = driver.find_element(By.TAG_NAME, 'button').click()

    success_text = driver.find_element(By.TAG_NAME, 'p')
    success_text = success_text.text
    assert success_text == 'Пользователь вышел из системы'