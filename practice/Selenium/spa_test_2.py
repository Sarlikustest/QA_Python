import time
from selenium import webdriver

from selenium.webdriver.common.by import By
try:

    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get('https://erikdark.github.io/Qa_autotest_15/')

    driver.find_element(By.ID, 'verify').click()


finally:
    time.sleep(5)
    driver.quit()