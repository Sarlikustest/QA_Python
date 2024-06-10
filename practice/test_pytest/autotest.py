import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
def test_case1():
    try:
        driver = webdriver.Chrome()
        driver.get('https://erikdark.github.io/Qa_autotests_reg_form_pop_up/')
        login_btn = driver.find_element(By.ID, 'openModalButton')
        login_btn.click()

        wait = WebDriverWait(driver,10)

        login = wait.until(EC.presence_of_element_located((By.ID, 'username')))
        login.send_keys('testuser')

        password = wait.until(EC.presence_of_element_located((By.ID, 'password')))
        password.send_keys('password123')
        

        btn = driver.find_element(By.CSS_SELECTOR,'[type="submit"]')
        # btn = driver.find_element(By.TAG_NAME,'button') - по тегу кнопка он не ищет, так как сначала он находит кнопку выше по коду, которая открывает модальное окно

        btn.click()
        

        # hidden_element = wait.until(EC.invisibility_of_element((By.ID, 'username')))

        

        
        

    finally:
        time.sleep(5)
        driver.quit()


# def test_case2():
#     try:
#         driver = webdriver.Chrome()
#         driver.get('https://erikdark.github.io/Qa_autotests_reg_form_pop_up/')
#         login_btn = driver.find_element(By.ID, 'openModalButton')
#         login_btn.click()

#         wait = WebDriverWait(driver,10)

#         login = wait.until(EC.presence_of_element_located((By.ID, 'username')))
#         login.send_keys('')

#         password = wait.until(EC.presence_of_element_located((By.ID, 'password')))
#         password.send_keys('password123')


#         btn = driver.find_element(By.CSS_SELECTOR,'[type="submit"]')

#         btn.click()

#         hidden_element = wait.until(EC.invisibility_of_element((By.ID, 'username')))
#         if hidden_element:
#             print ('test passed')

        
        

#     finally:
#         time.sleep(5)
#         driver.quit()

# def test_case3():
#     try:
#         driver = webdriver.Chrome()
#         driver.get('https://erikdark.github.io/Qa_autotests_reg_form_pop_up/')
#         login_btn = driver.find_element(By.ID, 'openModalButton')
#         login_btn.click()

#         wait = WebDriverWait(driver,10)

#         login = wait.until(EC.presence_of_element_located((By.ID, 'username')))
#         login.send_keys('testuser')

#         password = wait.until(EC.presence_of_element_located((By.ID, 'password')))
#         password.send_keys('')


#         btn = driver.find_element(By.CSS_SELECTOR,'[type="submit"]')

#         btn.click()

#         hidden_element = wait.until(EC.invisibility_of_element((By.ID, 'username')))
#         if hidden_element:
#             print ('test passed')

        
        

#     finally:
#         time.sleep(5)
#         driver.quit()

# def test_case4():
#     try:
#         driver = webdriver.Chrome()
#         driver.get('https://erikdark.github.io/Qa_autotests_reg_form_pop_up/')
#         login_btn = driver.find_element(By.ID, 'openModalButton')
#         login_btn.click()

#         wait = WebDriverWait(driver,10)

#         login = wait.until(EC.presence_of_element_located((By.ID, 'username')))
#         login.send_keys('ghh')

#         password = wait.until(EC.presence_of_element_located((By.ID, 'password')))
#         password.send_keys('hggg')


#         btn = driver.find_element(By.CSS_SELECTOR,'[type="submit"]')

#         btn.click()

#         hidden_element = wait.until(EC.invisibility_of_element((By.ID, 'username')))
#         if hidden_element:
#             print ('test passed')

        
        

#     finally:
#         time.sleep(5)
#         driver.quit()