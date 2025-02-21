import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Launch the browser
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.Edge()

# Step 2: Navigate to the site and maximize the window
driver.get("https://dmedia1.netlify.app/index.html")
driver.maximize_window()
print("Successfully navigated to the website.")
time.sleep(1)

# Step 3: Click on login button
login_button_submit = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="signupForm"]/div[7]/p/a'))
)
login_button_submit.click()
print("Login button clicked successfully.")
time.sleep(1)

# Step 4: Enter login credentials
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("pugalpugazh@gmail.com")
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Pugal@1234")
print("Login credentials entered successfully.")
time.sleep(1)

# Step 5: Submit login
login_button_submit = driver.find_element(By.XPATH, '//*[@id="submitSignIn"]')
login_button_submit.click()
print("Login submitted successfully.")
time.sleep(1)

# Step 6: Like button interaction
like_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="postContainer"]/div[1]/div[1]/span[1]'))
)
like_button.click()
print("Like button clicked successfully.")
time.sleep(1)

# Step 7: Comment button interaction
comment_open_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="postContainer"]/div[1]/div[1]/span[3]'))
)
comment_open_button.click()
print("Comment open button clicked.")
time.sleep(5)

# Step 8: Typing comment
driver.find_element(By.XPATH, '/html/body/div/div/textarea').send_keys("hi")
print("Comment typed: 'hi'.")
time.sleep(5)

# Step 9: Post comment
post_comment_send = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'submit-comment-button'))
)
post_comment_send.click()
print("Comment posted successfully.")
time.sleep(5)

# Step 10: Close comment section
close_comment = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/button'))
)
close_comment.click()
print("Comment section closed.")
time.sleep(5)

# Step 11: Save button interaction
save_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="postContainer"]/div[1]/div[1]/span[4]'))
)
save_button.click()
print("Post saved successfully.")
time.sleep(5)

# Step 12: Navigate to profile
profile_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="postContainer"]/div[1]/div[2]/a'))
)
profile_button.click()
print("Navigated to profile page.")
time.sleep(6)

# Step 13: Follow button interaction
follow_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="action-button"]/li[1]/button'))
)
follow_button.click()
print("Followed the user.")
time.sleep(6)

# Step 14: Post image interaction
post_image_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="posts-grid"]/div/img'))
)
post_image_button.click()
print("Post image clicked.")
time.sleep(6)

# Step 15: Navigate back
driver.back()
print("Navigated back to previous page.")
time.sleep(6)

# Step 16: Click message button
message_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'messageButton'))
)
message_button.click()
print("Message button clicked.")
time.sleep(6)

# Step 17: Send message
driver.find_element(By.ID, 'messageInput').send_keys("today nice day")
send_message_button = driver.find_element(By.ID, 'sendMessageButton')
send_message_button.click()
print("Message sent successfully.")
time.sleep(6)

# Step 18: Navigate to discover page
discover_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/aside/nav/ul[1]/li[2]/a/span[2]'))
)
discover_button.click()
print("Navigated to discover page.")
time.sleep(6)

# Step 19: Use search bar
driver.find_element(By.XPATH, '//*[@id="search-bar"]').send_keys("#back")
print("Searched for hashtag '#back'.")
time.sleep(6)

# Step 20: Click on image from search results
image_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="results-container"]/div/div/img'))
)
image_button.click()
print("Image clicked from search results.")
time.sleep(6)

# Step 21: Navigate back
driver.back()
print("Navigated back to previous page.")
time.sleep(6)

# Step 22: Navigate to discover page again
discover_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/aside/nav/ul[1]/li[2]/a/span[2]'))
)
discover_button.click()
print("Navigated to discover page again.")
time.sleep(6)

# Step 23: Use search bar to search for 'ThMizh'
driver.find_element(By.XPATH, '//*[@id="search-bar"]').send_keys("ThMizh")
print("Searched for 'ThMizh'.")
time.sleep(6)

# Step 24: Navigate to upload page
click_upload_button = driver.find_element(By.XPATH, '/html/body/aside/nav/ul[1]/li[4]/a/span[2]')
click_upload_button.click()
print("Navigated to upload page.")
time.sleep(4)

# Step 25: Upload image
file = driver.find_element(By.XPATH, '//*[@id="file"]')
file.send_keys(r"C:\PUGAL_FSSA\selenium-automation-testing\selenium.png")
print("Image uploaded successfully.")
time.sleep(4)

# Step 26: Add caption and hashtags
file = driver.find_element(By.ID, 'caption')
file.send_keys("Tamil Nadu is the southernmost state of India")
file = driver.find_element(By.ID, 'hashtags')
file.send_keys("#Tamil Nadu is the southernmost state of India")
print("Caption and hashtags added.")
time.sleep(4)


# click_saved_img =driver.find_element(By.ID,'postButton')
# click_saved_img.click()
# print("postButton")
# time.sleep(6)

# seved_button=driver.switch_to.alert
# print("switch")
# seved_button.accept()
# time.sleep(5)


# Step 27: Click saved button
click_saved_button = driver.find_element(By.XPATH, '/html/body/aside/nav/ul[1]/li[5]/a/span[2]')
click_saved_button.click()
print("Navigated to saved posts.")
time.sleep(6)

# Step 28: Click on saved image
click_saved_img = driver.find_element(By.XPATH, '//*[@id="saved-posts"]/div[1]/img')
click_saved_img.click()
print("Clicked on saved image.")
time.sleep(6)

# Step 29: Unsave the image
click_unsaved_img = driver.find_element(By.XPATH, '//*[@id="post-details"]/div[3]/div[6]/span[4]')
click_unsaved_img.click()
print("Image unsaved successfully.")
time.sleep(6)

driver.back()
# Step 30: Refresh and navigate back
driver.refresh()
time.sleep(5)


# Step 31: Navigate to my profile
my_profile = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/aside/nav/ul[2]/li[1]/a/span[2]'))
)
my_profile.click()
print("Navigated to my profile.")
time.sleep(4)

# Step 32: Edit profile
edit_profile = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="edit-profile-btn"]'))
)
edit_profile.click()
print("Navigated to edit profile page.")
time.sleep(5)

# Step 33: Enter new name, username, and bio
username_field = driver.find_element(By.ID, "edit-name")
username_field.clear()
username_field.send_keys("pugal")  # New name
username_field = driver.find_element(By.ID, "edit-username")
username_field.clear()
username_field.send_keys("pugal")  # New username
username_field = driver.find_element(By.ID, "edit-bio")
username_field.clear()
username_field.send_keys("hi")  # New bio
print("New name, username, and bio entered.")
time.sleep(6)

# Step 34: Save profile changes
save_profile_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'save-profile-btn'))
)
save_profile_btn.click()
print("Profile changes saved successfully.")
time.sleep(4)

# Handle alert after saving profile
seved_button = driver.switch_to.alert
seved_button.accept()
print("Alert accepted after saving profile.")
time.sleep(5)

# Step 35: Cancel profile edit
edit_profile = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="edit-profile-btn"]'))
)
edit_profile.click()
print("Navigated back to edit profile page.")
time.sleep(3)

cancel_edit_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'cancel-edit-btn'))
)
cancel_edit_btn.click()
print("Cancelled profile edit.")
time.sleep(4)

# Step 36: Navigate to upload page again
upload = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'nav-label'))
)
upload.click()
print("Navigated to upload page.")
time.sleep(3)

# Step 37: Navigate to save button page
save_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'nav-label'))
)
save_button.click()
print("Navigated to save button page.")
time.sleep(5)

# Step 38: Logout
logout_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="signOut"]/span[2]'))
)
logout_button.click()
print("Logged out successfully.")
time.sleep(6)

# Step 39: Close the driver
driver.quit()
print("Driver closed.")

# click_button=driver.find_element(By.XPATH,'//*[@id="buttons"]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]')
# click_button.click()
# time.sleep(4)
