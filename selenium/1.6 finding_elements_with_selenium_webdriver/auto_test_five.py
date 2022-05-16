from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    num_one = int(browser.find_element_by_id('num1').text)
    num_two = int(browser.find_element_by_id('num2').text)
    num_sum = str(num_one + num_two)

    num_list = Select(browser.find_element_by_id('dropdown'))
    num_list.select_by_value(num_sum)

    browser.find_element_by_css_selector('button.btn').click()

finally:
    time.sleep(10)
    browser.quit()

