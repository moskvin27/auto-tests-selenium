from selenium import webdriver
import time

''' для начала тестирования достаточно запустить скрипт, в нем содержатся обе ссылки на два сайта, автотестирование выполняется последовательно,
    никаких дополнительных манипуляций не требуется '''

# тестируем первый сайт http://suninjuly.github.io/registration1.html
try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element_by_css_selector('.first_block .form-group.first_class .form-control.first')
    first_name.send_keys('Ilon')

    second_name = browser.find_element_by_css_selector('.first_block .form-group.second_class .form-control.second')
    second_name.send_keys('Mask')

    email = browser.find_element_by_css_selector('.first_block .form-group.third_class .form-control.third')
    email.send_keys('email')

    time.sleep(3)
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# тестируем второй сайт http://suninjuly.github.io/registration2.html
try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element_by_css_selector('.first_block .form-group.first_class .form-control.first')
    first_name.send_keys('Ilon')

    second_name = browser.find_element_by_css_selector('.first_block .form-group.second_class .form-control.second')
    second_name.send_keys('Mask')

    email = browser.find_element_by_css_selector('.first_block .form-group.third_class .form-control.third')
    email.send_keys('email')

    time.sleep(3)
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()