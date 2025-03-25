# Selenium Webdriver with Python tutorial 6 | Elements and Locators in Selenium WebDriver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#  load time performance
start = time.time()
end = time.time()
# Calculate the load time
load_time = end - start
print(f"Load Time: {load_time} seconds")

driver.maximize_window()
print("Navigated to the website")
time.sleep(2)



driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123")
print("Entered login credentials")
time.sleep(4)


#4 to 5 lines
# login_button_submit = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'))
# )
# login_button_submit.click()
# print("Login button clicked successfully 3.")
# time.sleep(5)



login_button_=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
login_button_.click()
print("login_button")
time.sleep(5)