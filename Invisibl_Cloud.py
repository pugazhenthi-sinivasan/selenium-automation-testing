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

# Step 2: Navigate to the website and maximize the window
driver.get("https://invisibl.io/")
driver.maximize_window()
end = time.time()  # End time

# Calculate and log the load time
load_time = end - start
with open("log.txt", "a") as log_file:
    log_file.write(f"Website Load Time: {load_time:.2f} seconds\n")
    log_file.write("Navigated to Invisibl.io successfully.\n")

print(f"Load Time: {load_time:.2f} seconds")
time.sleep(5)

# Step 3: Click on "Explore Products"
explore_products_button = driver.find_element(By.XPATH, '/html/body/div[2]/section[1]/div[2]/div/div/section[2]/div/div/div/div[3]/div/div/a/span')
explore_products_button.click()
time.sleep(5)

# Step 4: Click on "Request Demo"
request_demo_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Request Demo')
request_demo_link.click()
time.sleep(5)
print("1")
# Step 5: Enter name in the form
First_Name = driver.find_element(By.ID, 'form-field-name')
First_Name.send_keys("Pugal")
time.sleep(6)
print("2")

Last_Name = driver.find_element(By.XPATH, '//*[@id="form-field-field_7513d3a"]')
Last_Name.send_keys("Pugal")
time.sleep(20)
print("3")

# Company_Name = driver.find_element(By.ID, 'form-field-field_8e900c3')
# Company_Name.send_keys("Pugal")
# time.sleep(6)
# print("4")


# Work_Email= driver.find_element(By.ID, 'form-field-email')
# Work_Email.send_keys("Pugal")
# time.sleep(4)
# print("5")


# Phone_Number= driver.find_element(By.XPATH, '//*[@id="form-field-field_2b0e85a"]')
# Phone_Number.send_keys("12345678989")
# time.sleep(4)
# print("7")

# Message=driver.find_element(By.ID,'form-field-message')
# Message.send_keys("Pugal")
# time.sleep(10)
# print("8")

n=driver.find_element(By.XPATH,'//*[@id="popup-form"]/div/div/div/div[3]/div/form/div/div[7]/button')
n.click()
time.sleep(5)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(5)
# Close the browser
driver.quit()  