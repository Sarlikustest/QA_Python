import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_dovod():
    driver = webdriver.Chrome()

    driver.get('https://erikdark.github.io/dovod_repo_QA_form/')
    # login = driver.find_element(By.ID, 'login').send_keys('admin123')
    # password = driver.find_element(By.ID, 'password').send_keys('password123')
    # database = driver.find_element(By.ID, 'database').send_keys('bd_dovod')
    # host = driver.find_element(By.ID, 'host').send_keys('localhost')
    # btn = driver.find_element(By.TAG_NAME, 'button').click()
    # alert = driver.switch_to.alert
    # alert.accept()
    # login = driver.find_element(By.ID, 'login').clear()
    # login = driver.find_element(By.ID, 'login').send_keys('321nimda')

    # password = driver.find_element(By.ID, 'password').clear()
    # password = driver.find_element(By.ID, 'password').send_keys('321drowssap')

    # database = driver.find_element(By.ID, 'database').clear()
    # database = driver.find_element(By.ID, 'database').send_keys('dovod_db')

    # host = driver.find_element(By.ID, 'host').clear()
    # host = driver.find_element(By.ID, 'host').send_keys('tsohlacol')
    # btn = driver.find_element(By.TAG_NAME, 'button').click()

    # time.sleep(10)
    # driver.quit()

    first_list = ['admin123', 'password123', 'bd_dovod', 'localhost']
    reverse_list = ['321nimda', '321drowssap', 'dovod_db', 'tsohlacol']

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

    # for i in range(len(reverse_list)):
    #     element = driver.find_elements(By.TAG_NAME, 'input')
    #     element[i].send_keys(reverse_list[i])
    btn = driver.find_element(By.TAG_NAME, 'button').click()

       

    time.sleep(10)
