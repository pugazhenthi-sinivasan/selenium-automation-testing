import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoAlertPresentException

# Step 1: Launch the browser
driver = webdriver.Chrome()

# Step 2: Navigate to the site and maximize the window
driver.get("https://dmedia1.netlify.app/index.html")
driver.maximize_window()
print("Navigated to the website 2.")
time.sleep(2)


# Step 3: Click on login button
login_button_submit = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="signupForm"]/div[7]/p/a'))
)
login_button_submit.click()
print("Login button clicked successfully 3.")



# Step 4: Enter login 
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("pugalpugazh@gmail.com")
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Pugal@1234")
print("Entered login credentials 4.")



# Step 5: Submit login 
login_button_submit=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="submitSignIn"]'))
)
login_button_submit.click()
print("log in submitted succesfully 5")
time.sleep(5)


# Step 25:my_profile
my_profile=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'/html/body/aside/nav/ul[2]/li[1]/a/span[2]'))
)
my_profile.click()
print("my_profile 25")
time.sleep(3)



# Step 26:edit_profile
edit_profile=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="edit-profile-btn"]'))
)
edit_profile.click()
print("edit_profile 26")
time.sleep(3)


# Step 27:New name, username, and bio. Enter
username_field = driver.find_element(By.ID, "edit-name")
username_field.clear()  #Name Clear 
username_field.send_keys("pugazh")  # Replace with the desired username
username_field = driver.find_element(By.ID, "edit-username")
username_field.clear()  #username Clear 
username_field.send_keys("@pugazh") 
username_field = driver.find_element(By.ID, "edit-bio")
username_field.clear()  # Clear bio
username_field.send_keys("pugazh") 
print("New name, username, and bio. Enter 27")
time.sleep(5)


# Step 28:save_profile_btn
save_profile_btn=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.ID,'save-profile-btn'))
)
save_profile_btn.click()
print("save_profile_btn 28")
time.sleep(3)

seve_button=driver.switch_to.alert
print("switch")
seve_button.accept()
time.sleep(5)


# Step 30:edit_profile
edit_profiles=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.ID,'edit-profile-btn'))
)
edit_profiles.click()
print("edit_profile 30")
time.sleep(3)


# Step 31:edit_profile-cance
edit_profile_cance=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.ID,'cancel-edit-btn'))
)
edit_profile_cance.click()
print("edit_profile-cance 31")
time.sleep(3)



# Step 32: upload navigated page
upload=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.CLASS_NAME,'nav-label'))
)
upload.click()
print("upload 32")
time.sleep(3)

# Step 33:caption and hashtags Enter
driver.find_element(By.ID, 'caption').send_keys("back")
driver.find_element(By.ID, 'hashtags').send_keys("back")
print("caption and hashtags Enter 33")
time.sleep(3)


# Step 34:postButton
postButton=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.ID,'postButton'))
)
postButton.click()
print("postButton 34")
time.sleep(3)


# Step 35: home navigated page
home_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,'/html/body/aside/nav/ul[1]/li[1]/a/span[2]'))
)
home_button.click()
print("Comment button clicked successfully 35.")
time.sleep(3)

# Step 36:Driver closed 
driver.quit()
print("Driver closed 36.")