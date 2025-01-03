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
try:
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "username")))
    driver.find_element(By.ID, "username").send_keys("Sivakuma")
    print("Entered Username.")

    driver.find_element(By.ID, "Email").send_keys("tami@gmail.com")
    print("Entered Email Address.")

    driver.find_element(By.ID, "password").send_keys("Siva@134567890")
    print("Entered Password.")

    driver.find_element(By.ID, "CPass").send_keys("Siva@134567890")
    print("Entered Confirm Password.")
except Exception as e:
    print(f"Error interacting with the form: {e}")

# Step 3: Click the Submit button
try:
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit"))
    )
    submit_button.click()
    print("Sign-up form submitted successfully.")
except Exception as e:
    print(f"Error clicking the submit button: {e}")

# Step 4: Wait for a while to observe the behavior (if needed)
time.sleep(10)

driver.find_element(By.XPATH,"//*[@id='Login-Email']").send_keys("tami@gmail.com")
driver.find_element(By.XPATH,"//*[@id='Login-password']").send_keys("Siva@134567890")
time.sleep(10)

# Step 5: Close the browser
driver.quit()
print("Browser closed.")
