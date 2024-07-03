#Создайте файл 5_hw.py в нем выполняйте все задания
# 1. Создайте функцию которая
# a. переходит на страницу https://www.saucedemo.com/
# b. находит элементы:
#       i. текстовое поле username
#       ii. текстовое поле password
#       iii. кнопку submit
# c. Создайте условие, если элементы найдены - вывести в консоль текст “Элементы найдены”

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.CSS_SELECTOR, '#user-name')
password = driver.find_element(By.CSS_SELECTOR, '#password')
submit = driver.find_element(By.CSS_SELECTOR, '#login-button')
if username is None and password is None and submit is None:
    print('Элементы не найдены')
else:
   print('Элементы найдены')



