from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
import time

driver = webdriver.Chrome()  # Use your browser driver

# Navigate to the login page
driver.get("https://example.com/login")  # Replace with the actual URL

# Wait for the login button and click it
login_button_submit = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='login']"))
)
login_button_submit.click()
print("Log in button clicked successfully.")
time.sleep(8)

# Enter login credentials
driver.find_element(By.XPATH, "//*[@id='Login-Email']").send_keys("tamilllppp@gmail.com")
driver.find_element(By.XPATH, "//*[@id='Login-password']").send_keys("Siva@134567890")
time.sleep(2)

# Click the login button again after entering credentials
login_button_submit = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='login']"))
)
login_button_submit.click()
print("Log in submitted successfully.")
time.sleep(5)

# Click the like button on the page
like_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='heart-qjh0Ho8Oxh4U24N9GK9l']"))
)
like_button.click()
print("Like button clicked successfully.")
time.sleep(5)

# View likes
view_like_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='showlike-qjh0Ho8Oxh4U24N9GK9l']"))
)
view_like_button.click()
print("View likes button clicked.")
time.sleep(5)

# Handle alert (if present)
try:
    alert = driver.switch_to.alert
    alert.dismiss()
    print("Alert dismissed.")
except NoAlertPresentException:
    print("No alert present.")

# Navigate back
driver.back()
time.sleep(3)

# Click the comment button
comment_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='comment-qjh0Ho8Oxh4U24N9GK9l']"))
)
comment_button.click()
print("Comment button clicked.")
time.sleep(5)

# Quit the driver
driver.quit()
print("Driver quit successfully.")
