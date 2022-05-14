from selenium import webdriver
import time
import math

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_css_selector('button.btn').click()
    browser.switch_to.window(browser.window_handles[1])

    num = browser.find_element_by_id('input_value').text
    num_input = str(math.log(abs(12 * math.sin(int(num)))))
    answer = browser.find_element_by_id('answer')
    answer.send_keys(num_input)

    browser.find_element_by_css_selector('button.btn').click()
    
finally:
    time.sleep(10)
    browser.quit()