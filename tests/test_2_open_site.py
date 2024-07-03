from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/")

# поиск элемента
icon = driver.find_element(By.CSS_SELECTOR, 'header > a > img')
if icon is None:
    print('Элемент не найден')
else:
   print('Элемент найден')
#find_element() - это метод селениума с помощью которого мы можем
#искать обьект на сайте
#первым элементом передаем тип поиска
#вторым элементом мы передаем тип локатора, который будем искать

#если элемент не найден - это баг
#запускаем программу и ждем долго
