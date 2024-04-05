from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("test1")

    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("test2")

    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("test3")

    cur_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(cur_dir, 'file.txt')
    attach = browser.find_element(By.ID, "file")
    attach.send_keys(file_path)

    submit = browser.find_element(By.TAG_NAME, "button")
    submit.click()

finally:
    time.sleep(30)
    browser.quit()