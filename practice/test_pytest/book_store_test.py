import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

def test_case1():
    try:
        driver = webdriver.Firefox()
        wait = WebDriverWait(driver, 10)

        driver.get('https://selenium1py.pythonanywhere.com/ru/')

        offer_btn = driver.find_element(By.LINK_TEXT, 'Предложения')
        offer_btn.click()

        first_book = driver.find_element(By.LINK_TEXT, "The shellcoder's handbook")
        first_book.click()

        first_book_wallet = driver.find_element(By.CLASS_NAME, "btn-add-to-basket")
        first_book_wallet.click()
        return_btn = driver.find_element(By.LINK_TEXT, 'Oscar')
        return_btn.click()

        offer_btn = driver.find_element(By.LINK_TEXT, 'Предложения')
        offer_btn.click()

        second_book = driver.find_element(By.LINK_TEXT, "Hacking Exposed Wireless")
        second_book.click()

        second_book_wallet = driver.find_element(By.CLASS_NAME, "btn-add-to-basket")
        second_book_wallet.click()

        return_btn = driver.find_element(By.LINK_TEXT, 'Oscar')
        return_btn.click()

        offer_btn = driver.find_element(By.LINK_TEXT, 'Предложения')
        offer_btn.click()

        third_book = driver.find_element(By.LINK_TEXT, "Coders at Work")
        third_book.click()

        third_book_wallet = driver.find_element(By.CLASS_NAME, "btn-add-to-basket")
        third_book_wallet.click()

        return_btn = driver.find_element(By.LINK_TEXT, 'Oscar')
        return_btn.click()

        offer_btn = driver.find_element(By.LINK_TEXT, 'Предложения')
        offer_btn.click()

        fourth_book = driver.find_element(By.LINK_TEXT, "Visual Guide to Lock ...")
        fourth_book.click()

        fourth_book_wallet = driver.find_element(By.CLASS_NAME, "btn-add-to-basket")
        fourth_book_wallet.click()

        wallet_btn = driver.find_element(By.LINK_TEXT, "Посмотреть корзину").click()

        wallet = driver.find_element(By.LINK_TEXT, "Перейти к оформлению").click()

        email = driver.find_element(By.NAME, 'username').send_keys('papa@mail.ru')
        password = driver.find_element(By.NAME, 'password').send_keys('12345')
        regist_btn = driver.find_element(By.CLASS_NAME, 'btn-primary').click()

        name = driver.find_element(By.NAME, 'first_name').send_keys('Peter')
        last_name = driver.find_element(By.NAME, 'last_name').send_keys('Petrovich')
        line1 = driver.find_element(By.NAME, 'line1').send_keys('Санкт_Петерсбург')
        line4 = driver.find_element(By.NAME, 'line4').send_keys('Санкт_Петерсбург')
        postcode = driver.find_element(By.NAME, 'postcode').send_keys('1001')
        # country = Select(driver.find_element(By.TAG_NAME, 'select'))
        # country.select_by_value('RU')
        continue_btn = driver.find_element(By.CLASS_NAME, 'btn-primary').click()
        continue_btn1 = driver.find_element(By.CLASS_NAME, 'btn-lg').click()
        continue_btn1 = driver.find_element(By.CLASS_NAME, 'btn-block').click()

    
        




    finally:
        time.sleep(5)
        driver.quit()