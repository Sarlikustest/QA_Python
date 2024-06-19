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

    log_btn = driver.find_element(By.LINK_TEXT, 'Динамический контент').click()

    create_btn = driver.find_element(By.ID, 'add-element').click()

    # if_exist = driver.find_element(By.TAG_NAME, 'p')
    
    exist_text = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.ID, 'content-area'), 'Новый элемент'))
    assert exist_text == True
    creation_text = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.ID, 'content-area'), 'Элемент добавлен'))
    assert creation_text == True

