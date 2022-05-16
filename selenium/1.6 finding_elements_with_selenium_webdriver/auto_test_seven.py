from selenium import webdriver
import time
import os

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element_by_name('lastname')
    first_name.send_keys('Ilon')
    last_name = browser.find_element_by_name('firstname')
    last_name.send_keys('Mask')
    email = browser.find_element_by_name('email')
    email.send_keys('mail')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "begin.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element_by_css_selector("[type='file']")
    element.send_keys(file_path)

    browser.find_element_by_css_selector('button.btn').click()

finally:
    time.sleep(10)
    browser.quit()