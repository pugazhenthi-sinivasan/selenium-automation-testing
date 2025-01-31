import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver. Chrome()

driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(5)


driver.find_element(By.ID, 'user-name').send_keys("standard_user")
driver.find_element(By.ID, 'password').send_keys("secret_sauce")
print("Entered login credentials")
time.sleep(4)




login_button_=driver.find_element(By.ID,'login-button')
login_button_.click()
print("login_button")
time.sleep(5)