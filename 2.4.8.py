from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math
import time

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.ID, "book")
    price = browser.find_element(By.ID, "price")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), ("$100")))
    button.click()

    submit = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)

    x = browser.find_element(By.ID, "input_value")
    x1 = int(x.text)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(calc(x1))

    submit.click()

finally:
    time.sleep(30)
    browser.quit()