#тест проходит на старом сайте и падает на новом, как и требуется по заданию
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"

    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, 'input.form-control.first[required]')
    input1.send_keys("test1")

    input2 = browser.find_element(By.CSS_SELECTOR, 'input.form-control.second[required]')
    input2.send_keys("test2")

    input3 = browser.find_element(By.CSS_SELECTOR, 'input.form-control.third[required]')
    input3.send_keys("test3")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()