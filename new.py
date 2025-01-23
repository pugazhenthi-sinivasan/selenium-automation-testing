import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
# Step 2: Navigate to the site and maximize the window
driver.get("https://rhythmix-music.netlify.app/")
driver.maximize_window()
print("Navigated to the website 2.")
time.sleep(2)
# Step 3: Click on login button
login_button_submit = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'sign-in-btn'))
)
login_button_submit.click()
print("Login button clicked successfully 3.")
time.sleep(10)