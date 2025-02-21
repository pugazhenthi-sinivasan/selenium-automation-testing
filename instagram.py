import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

start = time.time()
driver.get("https://www.instagram.com/")
driver.maximize_window()
time.sleep(5)

end = time.time()
load_time = end - start
print(f"Load Time: {load_time} seconds")

# Open log file once
with open("log.txt", "a") as log_file:
    log_file.write(f"Load Time: {load_time} seconds\n")

# Enter login details
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[1]/div/label/input').send_keys("mistaketamil@gmail.com")
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[2]/div/label/input').send_keys("mistake123@")
print("Entered login credentials")

with open("log.txt", "a") as log_file:
    log_file.write("Entered login credentials.\n")

time.sleep(5)

# Click login button
login_button_ = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]')
login_button_.click()
print("Clicked login button")

with open("log.txt", "a") as log_file:
    log_file.write("Clicked login button.\n")

time.sleep(5)

# Navigate to home page
home_button = driver.find_element(By.PARTIAL_LINK_TEXT, 'Home')
home_button.click()
print("Navigated to Home page")

with open("log.txt", "a") as log_file:
    log_file.write("Navigated to Home page.\n")

time.sleep(10)

# Navigate to search
search = driver.find_element(By.PARTIAL_LINK_TEXT, 'Search')
search.click()
print("Navigated to Search")

with open("log.txt", "a") as log_file:
    log_file.write("Navigated to Search.\n")  # Corrected duplicate log entry

time.sleep(8)


driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input').send_keys("song")

with open("log.txt", "a") as log_file:
    log_file.write("type of tax.\n") 
    time.sleep(5)



click_search = driver.find_element(By.XPATH,'//a[1]//div[1]//div[1]//div[1]//div[2]//div[1]//div[1]//span[1]//span[1]')
click_search.click()
time.sleep(5)


# Scroll down
driver.execute_script("window.scrollTo(0, 1000)")
time.sleep(5)

# Close browser
driver.quit()
