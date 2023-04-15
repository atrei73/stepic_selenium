import math
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/execute_script.html')

x = browser.find_element(By.CSS_SELECTOR, 'span#input_value.nowrap').text
x = calc(x)

browser.find_element(By.ID, 'answer').send_keys(x)

robot = browser.find_element(By.ID, 'robotCheckbox')
browser.execute_script("return arguments[0].scrollIntoView(true);", robot)
robot.click()
browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]').click()
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()


sleep(15)
browser.quit()
