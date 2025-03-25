from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Navigate to a webpage
    driver.get("https://www.orangehrm.com/")  # Replace with your URL
    driver.maximize_window()
    time.sleep(10)

    # Try to find and click a non-existent button (for demonstration)
    button = driver.find_element(By.XPATH,'//*[@id="Form_submitForm_action_request"]')  # Will raise an exception
    button.click()

except Exception as e:
    # Catch and handle any exception (like NoSuchElementException)
    print(f"An error occurred: {e}")
    
else:
    # Code to run if no exception occurs (successful click)
    print("Button clicked successfully!")

finally:
    # Code that will run no matter what (closing the browser)
    time.sleep(3)  # Wait for a few seconds to observe the result
    print("Closing the browser.")
    driver.quit()
