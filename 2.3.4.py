from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.ID, "input_value")
    x1 = int(x.text)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(calc(x1))

    submit = browser.find_element(By.TAG_NAME, "button")
    submit.click()

finally:
    time.sleep(30)
    browser.quit()