from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Step 1: Launch the browser
driver = webdriver.Chrome()
driver.get("https://link-upp.netlify.app/")  # Replace with the path to your HTML file or hosted URL
driver.maximize_window()
print("Browser launched and page opened successfully.")

click_air=WebDriverWait(driver,10).until(
      EC.element_to_be_clickable((By.XPATH,"//*[@id='form']/div[5]/span/span/a"))
)
click_air.click()
print("this is invalid email showing succesfully")


# Step 2: Wait until the username field is visible and interact with the form

