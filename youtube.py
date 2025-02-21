import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create or open a log file
with open("log.txt", "w") as log_file:
    log_file.write("Log File - Selenium Automation\n")
    log_file.write("====================================\n")

# Step 1: Launch the browser
driver = webdriver.Chrome()
start = time.time()  # Start time

# Step 2: Navigate to YouTube and maximize the window
driver.get("https://www.youtube.com/")
driver.maximize_window()
end = time.time()  # End time

# Calculate and log the load time
load_time = end - start
with open("log.txt", "a") as log_file:
    log_file.write(f"Website Load Time: {load_time} seconds\n")
    log_file.write("Navigated to YouTube successfully.\n")

print(f"Load Time: {load_time} seconds")
time.sleep(4)

# Step 3: Enter search text
search_box = driver.find_element(By.XPATH, '//*[@id="center"]/yt-searchbox/div[1]/form/input')
search_box.send_keys("Mr Beast")
print("Opened YouTube and entered search text.")
with open("log.txt", "a") as log_file:
    log_file.write("Entered 'Mr Beast' in the search box.\n")

time.sleep(1)

# Step 4: Click search button
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/ytd-app[1]/div[1]/div[2]/ytd-masthead[1]/div[4]/div[2]/yt-searchbox[1]/button[1]/yt-icon[1]/span[1]/div[1]'))
)
search_button.click()
print("Search submitted successfully.")
with open("log.txt", "a") as log_file:
    log_file.write("Search button clicked.\n")

time.sleep(5)

# Step 5: Click on the first video
video = driver.find_element(By.XPATH, '//*[@id="video-title"]/yt-formatted-string')
video.click()
print("Clicked on the video.")
with open("log.txt", "a") as log_file:
    log_file.write("Clicked on the first video.\n")

time.sleep(6)

# Step 6: Click Subscribe
subscribe_button = driver.find_element(By.XPATH, '//*[@id="subscribe-button-shape"]/button/yt-touch-feedback-shape/div/div[2]')
subscribe_button.click()
print("Subscribed to the channel.")
with open("log.txt", "a") as log_file:
    log_file.write("Clicked on Subscribe button.\n")

time.sleep(5)

# Step 7: Click 'Sign In' if required
try:
    sign_in_button = driver.find_element(By.XPATH, '//*[@id="button"]/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]')
    sign_in_button.click()
    print("Clicked on Sign In.")
    with open("log.txt", "a") as log_file:
        log_file.write("Clicked on Sign In button.\n")
    time.sleep(5)
except:
    print("Sign In button not found, skipping...")
    with open("log.txt", "a") as log_file:
        log_file.write("Sign In button not found.\n")

# Step 8: Navigate back twice
driver.back()
time.sleep(5)

driver.back()
time.sleep(5)

print("Navigation completed.")
with open("log.txt", "a") as log_file:
    log_file.write("Navigation back completed.\n")

# Close the browser
driver.quit()
print("Browser closed.")
with open("log.txt", "a") as log_file:
    log_file.write("Browser closed.\n")

