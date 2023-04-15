import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')

WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))
WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.ID, "book"))).click()
y = (calc(browser.find_element(By.ID, 'input_value').text))
browser.find_element(By.ID, 'answer').send_keys(y)
browser.find_element(By.ID, 'solve').click()

print(browser.switch_to.alert.text.split(':')[-1])

browser.quit()
