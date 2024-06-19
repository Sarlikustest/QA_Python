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

def test_case(driver):


    driver = webdriver.Chrome()

    first_list = []
    names = []
    ages = []
    cities = []


    driver.get('https://erikdark.github.io/zachet_selenium_01/index.html')

    log_btn = driver.find_element(By.LINK_TEXT, 'Таблица данных').click()



    collumns = driver.find_elements(By.CSS_SELECTOR, 'td')
    for i in collumns:
        i = i.text
        first_list.append(i)
    print(first_list)



    list_of_names = [first_list[0], first_list[3], first_list[6]]
    list_of_names.reverse()
    list_of_ages = [first_list[1], first_list[4], first_list[7]]
    list_of_ages.reverse()
    list_of_cities = [first_list[2], first_list[5], first_list[8]]
    list_of_cities.reverse()

    def test_first():

        first_column = driver.find_element(By.CSS_SELECTOR, 'th[onclick="sortTable(0)"]').click()

        list = driver.find_elements(By.CSS_SELECTOR, 'td')
        for i in list:
            i = i.text
            names.append(i)


        sorted_list_of_names = [names[0], names[3], names[6]]

        if sorted_list_of_names == list_of_names:
            success_message = driver.find_element(By.ID, 'sort-message')
            success_message = success_message.text
            assert success_message == 'Таблица отсортирована по столбцу 1'

    def test_second():

        second_column = driver.find_element(By.CSS_SELECTOR, 'th[onclick="sortTable(1)"]').click()

        list = driver.find_elements(By.CSS_SELECTOR, 'td')
        for i in list:
            i = i.text
            ages.append(i)
        

        sorted_list_of_ages = [ages[1], ages[4], ages[7]]

        if sorted_list_of_ages == list_of_ages:
            success_message = driver.find_element(By.ID, 'sort-message')
            success_message = success_message.text
            assert success_message == 'Таблица отсортирована по столбцу 2'

    def test_third():

        third_column = driver.find_element(By.CSS_SELECTOR, 'th[onclick="sortTable(2)"]').click()  

        list = driver.find_elements(By.CSS_SELECTOR, 'td')
        for i in list:
            i = i.text
            cities.append(i)
    
        sorted_list_of_cities = [cities[1], cities[4], cities[7]]

        if sorted_list_of_cities == list_of_cities:
            success_message = driver.find_element(By.ID, 'sort-message')
            success_message = success_message.text
            assert success_message == 'Таблица отсортирована по столбцу 3'