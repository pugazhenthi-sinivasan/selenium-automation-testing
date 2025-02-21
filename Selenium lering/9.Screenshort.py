from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.orangehrm.com/")
driver.maximize_window()


driver.save_screenshot("seve.png")

# Take a screenshot and save it to the desired directory with a file name
driver.save_screenshot(r"C:\Users\PugazhenthiSinivasan\Pictures\Saved Pictures\screenshot.png")

# Optionally, wait a bit before closing
time.sleep(3)

# Close the browser
driver.quit()
