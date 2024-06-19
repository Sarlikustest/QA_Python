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


    driver.get('https://erikdark.github.io/zachet_selenium_01/index.html')

    log_btn = driver.find_element(By.LINK_TEXT, 'Таблица данных').click()

    collumns = driver.find_elements(By.TAG_NAME, 'td')
    for i in collumns:
        i = i.text
    print(i)

    first_column = driver.find_element(By.CSS_SELECTOR, 'th[onclick="sortTable(0)"]').click()
    
    first_success_text = driver.find_element(By.TAG_NAME, 'p')
    first_success_text = first_success_text.text
    assert first_success_text == 'Таблица отсортирована по столбцу 1'

    second_column = driver.find_element(By.CSS_SELECTOR, 'th[onclick="sortTable(1)"]').click()
    
    second_success_text = driver.find_element(By.TAG_NAME, 'p')
    second_success_text = second_success_text.text
    assert second_success_text == 'Таблица отсортирована по столбцу 2'

    third_column = driver.find_element(By.CSS_SELECTOR, 'th[onclick="sortTable(2)"]').click()
    
    third_success_text = driver.find_element(By.TAG_NAME, 'p')
    third_success_text = third_success_text.text
    assert third_success_text == 'Таблица отсортирована по столбцу 3'