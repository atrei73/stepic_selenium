from selenium.webdriver.support.ui import Select
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://suninjuly.github.io/selects1.html')


num1 = int(browser.find_element(By.ID, 'num1').text)
num2 = int(browser.find_element(By.ID, 'num2').text)
s = str(num1 + num2)
select = Select(browser.find_element(By.TAG_NAME, 'select'))
select.select_by_value(s).click()
browser.find_element(By.CSS_SELECTOR, 'button.btn-default').click()

sleep(15)
browser.quit()
