import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoAlertPresentException



# Step 1: Launch the browser
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.Edge()



# Step 2: Navigate to the site and maximize the window
driver.get("https://web.whatsapp.com/")
driver.maximize_window()
print("Navigated to the website 2.")
time.sleep(50)


request_demo_link = driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[5]/div/div/div/div[2]')
request_demo_link.click()
time.sleep(40)//*[@id="pane-side"]/div[1]/div/div/div[5]/div/div/div/div[2]/div[1]/div[1]/div/div/span