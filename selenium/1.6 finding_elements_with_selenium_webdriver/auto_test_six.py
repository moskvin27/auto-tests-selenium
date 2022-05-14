from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = 'http://SunInJuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)
    browser.execute_script("window.scrollBy(0, 100);")

    num = browser.find_element_by_id('input_value').text
    num_calc = calc(num)
    answer = browser.find_element_by_css_selector('.form-control')
    answer.send_keys(num_calc)


    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element_by_id('robotsRule')
    radiobutton.click()

    browser.find_element_by_css_selector('button.btn').click()

finally:
    time.sleep(10)
    browser.quit()


