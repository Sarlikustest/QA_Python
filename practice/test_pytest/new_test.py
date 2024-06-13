import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

try:
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)

    driver.get('https://selenium1py.pythonanywhere.com/ru/')

    offer_btn = driver.find_element(By.LINK_TEXT, 'Предложения')
    offer_btn.click()

    all_btns = driver.find_elements(By.CLASS_NAME, 'btn-block')
    # time.sleep(1)
    # j = 0
    for i in all_btns:
        i.click()
        wait
    # while j < 4:
    #     print(all_btns[j].text)
    #     all_btns[j].click()
    #     time.sleep(8)
    #     j = j+1

    # btn = driver.find_element(By.CLASS_NAME, 'btn-block')
    # btn.click()
    # for button in driver.find_elements(By.CLASS_NAME, 'btn-block'):
    #     button.click()



finally:
    time.sleep(5)
    driver.quit()