
import re
import time
#импортирую сам вебдрайвер
from selenium import webdriver
#импортирую класс By который ищет элемент на странице
from selenium.webdriver.common.by import By


#иницилизирую драйвер браузера
driver = webdriver.Chrome()






    # через get мы говорим браузеру что обращаемся к странице
driver.get('https://erikdark.github.io/Qa_autotests_05/')

time.sleep(2)
    

answer = driver.find_element(By.ID,'challenge')
new_list = answer.text
new_list = new_list.replace("?","")
true_list = new_list.split(' ')
the_last_list = []
for i in true_list:
    if i.isdigit():
        the_last_list.append(i)
for j in the_last_list:
    j = int(j)
print(the_last_list)
print(type(the_last_list[0]))
print(type(the_last_list[1]))
#sum_of_numbers = sum(the_last_list)

# field_answer = driver.find_element(By.ID, "answer")
# field_answer.send_keys(sum_of_numbers)
# time.sleep(5)




    



driver.quit()