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
time.sleep(10)



# Step 6: Like button count
like_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="postContainer"]/div[1]/div[1]/span[1]'))
)
like_button.click()
print("Like button clicked successfully 6.")
time.sleep(5)


# Step 7: Discover navigated page
discover_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,'/html/body/aside/nav/ul[1]/li[2]/a/span[2]'))
)
discover_button.click()
print("discover avigated successfully 7.")
time.sleep(5)


# Step 8: home navigated page
home_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,'/html/body/aside/nav/ul[1]/li[1]/a/span[2]'))
)
home_button.click()
print("Comment button clicked successfully 8.")
time.sleep(5)


# Step 9: Comment button interaction
comment_open_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="postContainer"]/div[1]/div[1]/span[3]'))
)
comment_open_button.click()
print("comment open button 9.")
# driver.save_screenshot(f"comment_error_{int(time.time())}.png") 
time.sleep(5)


## Step 10: typing comment
driver.find_element(By.CLASS_NAME,'comment-input').send_keys("hi")
print("comment 10")
# driver.save_screenshot(f"comment_error_{int(time.time())}.png") 
time.sleep(3)


## Step 11: post_comment_send
post_comment_send=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.CLASS_NAME,'submit-comment-button'))
)
post_comment_send.click()
print("comment send succesfully 11")
time.sleep(5)


## Step 12: close_comment
close_comment=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'/html/body/div/div/div[1]/button'))
)
close_comment.click()
print("close comment 12")
time.sleep(5)


## Step 13: seve button
seve_button=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="postContainer"]/div[1]/div[1]/span[4]'))
)
seve_button.click()
print("seve button 13")
time.sleep(5)


# Step 14:profile_button
profile_button=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="postContainer"]/div[1]/div[2]/a'))
)
profile_button.click()
print("profile_button 14")
time.sleep(10)

# Step 15:follow_button
follow_button=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="action-button"]/li[1]/button'))
)
follow_button.click()
print("follow_button 15")
time.sleep(10)


# Step 16:post_image_button
post_image_button=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="posts-grid"]/div/img'))
)
post_image_button.click()
print("post_image_button 16")
time.sleep(10)


# Step 17: Navigate back
driver.back()
print("Navigated back successfully 17.")
time.sleep(5)


# Step 18: Navigate back
driver.back()
print("Navigated back successfully 18.")
time.sleep(5)




# Step 19: discove Navigate 
discover_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,'/html/body/aside/nav/ul[1]/li[2]/a/span[2]'))
)
discover_button.click()
print("discover avigated successfully 19.")
time.sleep(5)


# Step 20:search-bar
driver.find_element(By.XPATH, '//*[@id="search-bar"]').send_keys("#back")
print("search-bar 20")
time.sleep(5)



# Step 21:image_button
image_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="results-container"]/div/div/img'))
)
image_button.click()
print("immage_button 21.")
time.sleep(5)



# Step 22: Navigate back
driver.back()
print("Navigated back successfully 22.")
time.sleep(5)



# Step 23: home navigated page
home_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,'/html/body/aside/nav/ul[1]/li[1]/a/span[2]'))
)
home_button.click()
print("Comment button clicked successfully 23.")
time.sleep(5)


# Step 24:my_profile
my_profile=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'/html/body/aside/nav/ul[2]/li[1]/a/span[2]'))
)
my_profile.click()
print("my_profile 24")
time.sleep(10)

# Step 25:edit_profile
edit_profile=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="edit-profile-btn"]'))
)
edit_profile.click()
print("edit_profile 25")
time.sleep(10)

# Step 26:edit_profile-cance
edit_profile_cance=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.ID,'cancel-edit-btn'))
)
edit_profile_cance.click()
print("edit_profile-cance 27")
time.sleep(10)


# Step 20:Driver closed 
driver.quit()
print("Driver closed 27.")



# # Step 10: Navigate forward
# driver.forward()
# print("Navigated forward successfully.")
# time.sleep(5)




