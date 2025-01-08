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



# Step 6: Like button count
like_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="postContainer"]/div[1]/div[1]/span[1]'))
)
like_button.click()
print("Like button clicked successfully 6.")
time.sleep(5)


# Step 7: Comment button interaction
comment_open_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="postContainer"]/div[1]/div[1]/span[3]'))
)
comment_open_button.click()
print("comment open button 7.")
# driver.save_screenshot(f"comment_error_{int(time.time())}.png") 
time.sleep(5)


## Step 8: typing comment
driver.find_element(By.CLASS_NAME,'comment-input').send_keys("hi")
print("comment_hi 8")
# driver.save_screenshot(f"comment_error_{int(time.time())}.png") 
time.sleep(3)


## Step 9: post_comment_send
post_comment_send=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.CLASS_NAME,'submit-comment-button'))
)
post_comment_send.click()
print("comment send succesfully 9")
time.sleep(5)


## Step 10: close_comment
close_comment=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'/html/body/div/div/div[1]/button'))
)
close_comment.click()
print("close comment 10")
time.sleep(5)


## Step 11: seve button
seve_button=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="postContainer"]/div[1]/div[1]/span[4]'))
)
seve_button.click()
print("seve button 11")
time.sleep(5)


# Step 12: Discover navigated page
discover_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,'/html/body/aside/nav/ul[1]/li[2]/a/span[2]'))
)
discover_button.click()
print("discover avigated successfully 12.")
time.sleep(5)


# Step 13:search-bar
driver.find_element(By.XPATH, '//*[@id="search-bar"]').send_keys("#back")
print("search-bar 13")
time.sleep(5)



# Step 14:image_button
image_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="results-container"]/div/div/img'))
)
image_button.click()
print("immage_button 14.")
time.sleep(5)

# Step 15: Navigate back
driver.back()
print("Navigated back successfully 15.")
time.sleep(5)


# Step 16:discover_button
discover_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,'/html/body/aside/nav/ul[1]/li[2]/a/span[2]'))
)
discover_button.click()
print("discover avigated successfully 16.")
time.sleep(5)



#  Step 17:search-bar
driver.find_element(By.XPATH, '//*[@id="search-bar"]').send_keys("ThMizh")
print("search-bar 17")
time.sleep(5)



# Step 18: home navigated page
home_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,'/html/body/aside/nav/ul[1]/li[1]/a/span[2]'))
)
home_button.click()
print("Comment button clicked successfully 18.")
time.sleep(5)



# Step 19:profile_button
profile_button=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="postContainer"]/div[1]/div[2]/a'))
)
profile_button.click()
print("profile_button 19")
time.sleep(5)



# Step 20:follow_button
follow_button=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="action-button"]/li[1]/button'))
)
follow_button.click()
print("follow_button 20")
time.sleep(5)



# Step 21:post_image_button
post_image_button=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="posts-grid"]/div/img'))
)
post_image_button.click()
print("post_image_button 21")
time.sleep(5)



# Step 22: Navigate back
driver.back()
print("Navigated back successfully 22.")
time.sleep(5)



# Step 23: Navigate back
driver.back()
print("Navigated back successfully 23.")
time.sleep(3)



# Step 24: home navigated page
home_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,'/html/body/aside/nav/ul[1]/li[1]/a/span[2]'))
)
home_button.click()
print("Comment button clicked successfully 24.")
time.sleep(3)



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


edit_profile=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="edit-profile-btn"]'))
)
edit_profile.click()
print("edit_profile 29")
time.sleep(3)


# # Step 30:cancel_edit_btn
cancel_edit_btn=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.ID,'cancel-edit-btn'))
)
cancel_edit_btn.click()
print("cancel_edit_btn 29")
time.sleep(3)

# Step 31:edit_profile
edit_profile=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="edit-profile-btn"]'))
)
edit_profile.click()
print("edit_profile 31")
time.sleep(3)


# Step 32:edit_profile-cance
edit_profile_cance=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.ID,'cancel-edit-btn'))
)
edit_profile_cance.click()
print("edit_profile-cance 32")
time.sleep(3)



# Step 33: upload navigated page
upload=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.CLASS_NAME,'nav-label'))
)
upload.click()
print("upload 33")
time.sleep(3)

# # Step 33:caption and hashtags Enter
# driver.find_element(By.ID, 'caption').send_keys("back")
# driver.find_element(By.ID, 'hashtags').send_keys("back")
# print("caption and hashtags Enter 33")
# time.sleep(3)


# # Step 34:postButton
# postButton=WebDriverWait(driver,10).until(
#     EC.element_to_be_clickable((By.ID,'postButton'))
# )
# postButton.click()
# print("postButton 34")
# time.sleep(3)


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



# # Step 10: Navigate forward
# driver.forward()
# print("Navigated forward successfully.")
# time.sleep(5)




