import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoAlertPresentException



# Step 1: Launch the browser
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.Edge()



# Step 2: Navigate to the site and maximize the window
driver.get("https://dmedia1.netlify.app/index.html")
driver.maximize_window()
print("Navigated to the website 2.")
time.sleep(1)




# Step 3: Click on login button
login_button_submit = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="signupForm"]/div[7]/p/a'))
)
login_button_submit.click()
print("Login button clicked successfully 3.")
time.sleep(1)





# Step 4: Enter login 
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("pugalpugazh@gmail.com")
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Pugal@1234")
print("Entered login credentials 4.")
time.sleep(1)





# Step 5: Submit login 
login_button_submit=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="submitSignIn"]'))
)
login_button_submit.click()
print("log in submitted succesfully 5")
time.sleep(1)





# Step 6: Like button count
like_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="postContainer"]/div[1]/div[1]/span[1]'))
)
like_button.click()
print("Like button clicked successfully 6.")
time.sleep(1)





# Step 7: Comment button interaction
comment_open_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="postContainer"]/div[1]/div[1]/span[3]'))
)
comment_open_button.click()
print("comment open button 7.")
# driver.save_screenshot(f"comment_error_{int(time.time())}.png") 
time.sleep(5)




## Step 8: typing comment
driver.find_element(By.XPATH,'/html/body/div/div/textarea').send_keys("hi")
print("comment_hi 8")
# driver.save_screenshot(f"comment_error_{int(time.time())}.png") 
time.sleep(5)




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


# Step 19:profile_button
profile_button=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="postContainer"]/div[1]/div[2]/a'))
)
profile_button.click()
print("profile_button 12")
time.sleep(6)




# Step 20:follow_button
follow_button=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="action-button"]/li[1]/button'))
)
follow_button.click()
print("follow_button 13")
time.sleep(6)


# Step 21:post_image_button
post_image_button=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="posts-grid"]/div/img'))
)
post_image_button.click()
print("post_image_button 14")
time.sleep(6)




# Step 22: Navigate back
driver.back()
print("Navigated back successfully 15.")
time.sleep(6)




# Step 23:Click messageButton
message_button=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.ID,'messageButton'))
)
message_button.click()
print("Click messageButton 16")
time.sleep(6)

# driver.find_element(By.ID, 'messageInput').send_keys("today nice day")


# Step 24:send messageButton
send_message_button=driver.find_element(By.ID,'sendMessageButton')
send_message_button.click()
print("send message Button 17")
time.sleep(6)






# Step 12: Discover navigated page
discover_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,'/html/body/aside/nav/ul[1]/li[2]/a/span[2]'))
)
discover_button.click()
print("discover avigated successfully 18.")
time.sleep(6)


# Step 13:search-bar
driver.find_element(By.XPATH, '//*[@id="search-bar"]').send_keys("#back")
print("search-bar 19")
time.sleep(6)


# Step 14:image_button
image_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="results-container"]/div/div/img'))
)
image_button.click()
print("Click image_button 20.")
time.sleep(6)


# Step 15: Navigate back
driver.back()
print("Navigated back successfully 21.")
time.sleep(6)


# Step 16:discover_button
discover_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,'/html/body/aside/nav/ul[1]/li[2]/a/span[2]'))
)
discover_button.click()
print("discover avigated successfully 22.")
time.sleep(6)


#  Step 17:search-bar
driver.find_element(By.XPATH, '//*[@id="search-bar"]').send_keys("ThMizh")
print("search-bar 23")
time.sleep(6)






#uplond page img
click_uplond_button =driver.find_element(By.XPATH,'/html/body/aside/nav/ul[1]/li[4]/a/span[2]')
click_uplond_button.click()
print("uplond_ Navigate")
time.sleep(4)


file=driver.find_element(By.XPATH,'//*[@id="file"]')
file.send_keys(r"C:\PUGAL_FSSA\selenium-automation-testing\selenium.png")
print("uplond")
time.sleep(4)


file=driver.find_element(By.ID,'caption')
file.send_keys("Tamil Nadu is the southernmost state of India")
file=driver.find_element(By.ID,'hashtags')
file.send_keys("Tamil Nadu is the southernmost state of India")

click_saved_img =driver.find_element(By.ID,'postButton')
click_saved_img.click()
print("postButton")
time.sleep(6)

# seved_button=driver.switch_to.alert
# print("switch")
# seved_button.accept()
# time.sleep(5)


#saved button
click_saved_button =driver.find_element(By.XPATH,'/html/body/aside/nav/ul[1]/li[5]/a/span[2]')
click_saved_button.click()
print("click_uplond_button 25")
time.sleep(6)



click_saved_img =driver.find_element(By.XPATH,'//*[@id="saved-posts"]/div[1]/img')
click_saved_img.click()
print("click_saved_img 26")
time.sleep(6)


click_ansaved_img =driver.find_element(By.XPATH,'//*[@id="post-details"]/div[3]/div[6]/span[4]')
click_ansaved_img.click()
print("click_ansaved_img 27")
time.sleep(6)

driver.refresh()
driver.back()
time.sleep(5)



# Step 26:my_profile
my_profile=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'/html/body/aside/nav/ul[2]/li[1]/a/span[2]'))
)
my_profile.click()
print("my_profile 28")
time.sleep(4)



# Step 27:edit_profile
edit_profile=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="edit-profile-btn"]'))
)
edit_profile.click()
print("edit_profile 29")
time.sleep(5)


# Step 28:New name, username, and bio. Enter
username_field = driver.find_element(By.ID, "edit-name")
username_field.clear()  #Name Clear 
username_field.send_keys("pugal")  # Replace with the desired username
username_field = driver.find_element(By.ID, "edit-username")
username_field.clear()  #username Clear 
username_field.send_keys("pugal") 
username_field = driver.find_element(By.ID, "edit-bio")
username_field.clear()  # Clear bio
username_field.send_keys("hi") 
print("New name, username, and bio. Enter 30")
time.sleep(6)


# Step 29:save_profile_btn
save_profile_btn=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.ID,'save-profile-btn'))
)
save_profile_btn.click()
print("save_profile_btn 31")
time.sleep(4)

seved_button=driver.switch_to.alert
print("switch")
seved_button.accept()
time.sleep(5)



# Step 30:edit_profile 
edit_profile=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="edit-profile-btn"]'))
)
edit_profile.click()
print("edit_profile 32")
time.sleep(3)


# # Step 31:cancel_edit_btn
cancel_edit_btn=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.ID,'cancel-edit-btn'))
)
cancel_edit_btn.click()
print("cancel_edit_btn 33")
time.sleep(4)


# Step 33: upload navigated page
upload=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.CLASS_NAME,'nav-label'))
)
upload.click()
print("upload 34")
time.sleep(3)

# Step 35: save_button navigated page
save_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME,'nav-label'))
)
save_button.click()
print("save_button navigated page 35.")
time.sleep(5)



# Step 36:logout_button navigated page
logout_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="signOut"]/span[2]'))
)
logout_button.click()
print("logout_button navigated page 36.")
time.sleep(6)




# Step 36:Driver closed 
driver.quit()
print("Driver closed 37.")








