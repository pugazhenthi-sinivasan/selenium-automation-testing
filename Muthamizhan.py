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
driver.save_screenshot(f"comment_error_{int(time.time())}.png") 
time.sleep(5)


## Step 10: typing comment
driver.find_element(By.XPATH, '//html/body/div/div/input').send_keys("comment")
print("comment 10")
driver.save_screenshot(f"comment_error_{int(time.time())}.png") 
time.sleep(3)


## Step 11: post_comment_send
post_comment_send=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR,'body > div:nth-child(5) > div:nth-child(1) > button:nth-child(4)'))
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
print("seve button 14")
time.sleep(10)



# Step 15: Navigate back
driver.back()
print("Navigated back successfully 15.")
time.sleep(5)


# Step 16:Driver closed 
driver.quit()
print("Driver closed 16.")



# # Step 10: Navigate forward
# driver.forward()
# print("Navigated forward successfully.")
# time.sleep(5)




