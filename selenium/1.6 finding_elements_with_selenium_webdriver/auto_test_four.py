from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    box_element = browser.find_element_by_id('treasure')
    box_number = calc(box_element.get_attribute('valuex'))

    code = browser.find_element_by_id('answer')
    code.send_keys(box_number)

    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()

    radiobutton = browser.find_element_by_id('robotsRule')
    radiobutton.click()

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(15)
    browser.quit()
