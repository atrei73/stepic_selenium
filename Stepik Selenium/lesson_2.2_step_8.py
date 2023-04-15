import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')

current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'test.txt')  # добавляем к этому пути имя файла
dict = {'firstname': 'xx', 'lastname': 'xxxx', 'email': 'xx@xxxx.com', 'file': file_path}
for i, j in dict.items():
    browser.find_element(By.NAME, i).send_keys(j)

browser.find_element(By.CLASS_NAME, 'btn').click()

sleep(15)
browser.quit()
