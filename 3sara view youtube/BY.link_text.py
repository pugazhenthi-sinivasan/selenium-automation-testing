from selenium import webdriver
from selenium.webdriver.common.by import By
import time



driver =webdriver.Chrome()
driver.get("https://www.orangehrm.com/")
driver.maximize_window()

driver.find_element(By.ID,"Form_submitForm_EmailHomePage").send_keys("pugal")
time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT,"Contact Sales").click()
time.sleep(2)