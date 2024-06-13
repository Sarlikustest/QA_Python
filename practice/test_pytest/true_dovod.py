import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_dovod():
    driver = webdriver.Chrome()

    driver.get('https://erikdark.github.io/dovod_repo_QA_form/')
   

    first_list = ['admin123', 'password123', 'bd_dovod', 'localhost']


    for i in range(len(first_list)):
        element = driver.find_elements(By.TAG_NAME, 'input')
        element[i].send_keys(first_list[i])
    
    btn = driver.find_element(By.TAG_NAME, 'button').click()

    alert = driver.switch_to.alert
    alert.accept()

    for i in range(len(first_list)):
        element = driver.find_elements(By.TAG_NAME, 'input')
        element[i].clear()

    for i in range(len(first_list)):
        element = driver.find_elements(By.TAG_NAME, 'input')
        element[i].send_keys(first_list[i][::-1])

    btn = driver.find_element(By.TAG_NAME, 'button').click()

    time.sleep(10)

    driver.quit()