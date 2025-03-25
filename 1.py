import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Step 1: Launch the browser
driver = webdriver.Chrome()

# Step 2: Navigate to the site and maximize the window
driver.get("https://link-upp.netlify.app/")
driver.maximize_window()
print("Navigated to the website.")

# Step 3: Click on login button
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "login"))
)
login_button.click()
print("Login button clicked successfully.")

# Step 4: Enter login credentials
email_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "Login-Email"))
)
password_field = driver.find_element(By.ID, "Login-password")

email_field.send_keys("pugalpugazh@gmail.com")
password_field.send_keys("Pugazhe123@$")
print("Entered login credentials.")

# Step 5: Submit login
login_button.click()  # No need to find it again
print("Login button clicked successfully.")

# Step 6: Like button count
like_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "heart-FJDTwwb4Ep1sSybVnFmu"))
)
like_button.click()
print("Like button clicked successfully.")

# Step 7: Wait for the comment element
comment_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".comment-4a005SDyOWuheGHRq8jW"))
)

# Step 8: Extract CSS ::before content using JavaScript
script = """
return window.getComputedStyle(
    document.querySelector('.comment-4a005SDyOWuheGHRq8jW'), '::before'
).getPropertyValue('content');
"""

try:
    before_content = driver.execute_script(script)
    if before_content:
        print(f"::before content: {before_content.strip('\"')}")
    else:
        print("::before content is empty or not available.")
except Exception as e:
    print(f"Error executing JavaScript: {e}")

# Close browser
driver.quit()
