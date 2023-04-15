import math
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/get_attribute.html')

try:
    x_element = browser.find_element(By.ID, 'treasure')
    x = x_element.get_attribute('valuex')
    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.XPATH, '//button[@class="btn btn-default"]').click()

except:
    print('Error')
finally:
    sleep(15)
    browser.quit()
