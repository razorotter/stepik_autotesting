from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

def calc(x, y):
    return str(x + y)

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "num1")
    x1 = int(x.text)
    y = browser.find_element(By.ID, "num2")
    y1 = int(y.text)
    res = calc(x1, y1)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(res)

    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()