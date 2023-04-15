from time import sleep
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/alert_accept.html')

browser.find_element(By.CLASS_NAME, 'btn').click()

browser.switch_to.alert.accept()

x = calc(browser.find_element(By.ID, 'input_value').text)

browser.find_element(By.ID, 'answer').send_keys(x)

browser.find_element(By.CLASS_NAME, 'btn').click()

print(browser.switch_to.alert.text.split(':')[-1])
browser.quit()
