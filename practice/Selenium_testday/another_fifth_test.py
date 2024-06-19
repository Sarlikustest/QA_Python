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

    table = driver.find_element(By.ID, 'data-table')
    rows = table.find_elements(By.TAG_NAME, 'tr')
    first_col = [row.find_elements(By.TAG_NAME, 'td')[0].text for row in rows[1:]]
    first_col.reverse()

    table = driver.find_element(By.ID, 'data-table')
    rows = table.find_elements(By.TAG_NAME, 'tr')
    second_col = [row.find_elements(By.TAG_NAME, 'td')[1].text for row in rows[1:]]
    second_col.sort()
    second_col.reverse()

    table = driver.find_element(By.ID, 'data-table')
    rows = table.find_elements(By.TAG_NAME, 'tr')
    third_col = [row.find_elements(By.TAG_NAME, 'td')[2].text for row in rows[1:]]
    third_col.sort()
    third_col.reverse()


   
    first_column = driver.find_element(By.CSS_SELECTOR, 'th[onclick="sortTable(0)"]').click()

    table = driver.find_element(By.ID, 'data-table')
    rows = table.find_elements(By.TAG_NAME, 'tr')
    first_sorted_col = [row.find_elements(By.TAG_NAME, 'td')[0].text for row in rows[1:]]

    assert first_sorted_col == first_col, "Что-то не так" 
    

    second_column = driver.find_element(By.CSS_SELECTOR, 'th[onclick="sortTable(1)"]').click()

    table = driver.find_element(By.ID, 'data-table')
    rows = table.find_elements(By.TAG_NAME, 'tr')
    second_sorted_col = [row.find_elements(By.TAG_NAME, 'td')[1].text for row in rows[1:]]

    assert second_sorted_col == second_col, "Что-то не так" 

  


    third_column = driver.find_element(By.CSS_SELECTOR, 'th[onclick="sortTable(2)"]').click()

    table = driver.find_element(By.ID, 'data-table')
    rows = table.find_elements(By.TAG_NAME, 'tr')
    third_sorted_col = [row.find_elements(By.TAG_NAME, 'td')[2].text for row in rows[1:]]

    assert third_sorted_col == third_col, "Что-то не так" 
