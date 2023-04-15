import math
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get('https://suninjuly.github.io/math.html')

x_element = browser.find_element(By.CSS_SELECTOR, '#input_value.nowrap')
x = x_element.text
y = calc(x)
inp = browser.find_element(By.ID, 'answer')
inp.send_keys(y)
but = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
but.click()
rob = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
rob.click()
btn = browser.find_element(By.CLASS_NAME, 'btn')
btn.click()

sleep(15)
browser.quit()
