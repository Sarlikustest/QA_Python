import pytest
import time
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# service = Service(executable_path=ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    # driver.get('http://selenium1py.pythonanywhere.com/ru/')
    yield driver
    driver.quit()

def test_case(driver):
    try:
        driver.get('http://selenium1py.pythonanywhere.com/ru/')
        offers_button = driver.find_element(By.LINK_TEXT, 'Предложения').click()
        # buy_books = driver.find_elements(By.CLASS_NAME, 'btn-block')
        for i in range(5):
            if i == 0 or i == 4:
                continue
            else:
                new_btn = driver.find_elements(By.CSS_SELECTOR, "button.btn.btn-primary.btn-block")
                new_btn[i].click()
        bucket_btn = driver.find_element(By.LINK_TEXT, 'Посмотреть корзину').click()
        continue_btn = driver.find_element(By.LINK_TEXT, 'Перейти к оформлению').click()
            
    finally:
        time.sleep(10)
