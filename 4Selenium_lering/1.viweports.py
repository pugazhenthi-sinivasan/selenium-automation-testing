# Selenium webdriver with Python tutorial 10 | Viewports in selenium webdriver
import time
from selenium import webdriver

viewports = [(1024, 768), (768, 1024), (375, 667), (414, 896)]

driver = webdriver.Chrome()
driver.get('https://chatgpt.com/')

driver.maximize_window()
time.sleep(3)

driver.maximize_window()
time.sleep(3)


try:
    for width, height in viewports:
        driver.set_window_size(width, height)
        time.sleep(4)

finally:
    driver.close()
