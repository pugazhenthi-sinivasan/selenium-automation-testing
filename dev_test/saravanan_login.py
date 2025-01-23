import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains

# Step 1: Launch the browser
driver = webdriver.Chrome()

# Step 2: Navigate to the site and maximize the window
driver.get("https://link-upp.netlify.app/")
driver.maximize_window()
print("Navigated to the website.")
time.sleep(2)

# Login Page Interaction

# Step 3: Click on login button
login_button_submit = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='login']"))
)
login_button_submit.click()
print("Login button clicked successfully.")



# Step 4: Enter login 
# driver.find_element(By.XPATH, "//*[@id='Login-Email']").send_keys("tamilllppp@gmail.com")
# driver.find_element(By.XPATH, "//*[@id='Login-password']").send_keys("Siva@134567890")
driver.find_element(By.XPATH, "//*[@id='Login-Email']").send_keys("pugalpugazh@gmail.com")
driver.find_element(By.XPATH, "//*[@id='Login-password']").send_keys("Pugazhe123@$")
print("Entered login credentials.")



# Step 5: Submit login 
login_button_submit = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='login']"))
)
login_button_submit.click()
print("Login button clicked successfully.")
time.sleep(10)

# Step 6: Like button count
like_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="heart-kYwZiBoBs4CM4V5f3zW4"]'))
)
like_button.click()
print("Like button clicked successfully.")
time.sleep(5)
driver.refresh()



# Step 7: View like details
view_like_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'showlike-kYwZiBoBs4CM4V5f3zW4'))
)
view_like_button.click()
print("View like details clicked.")
time.sleep(5)


multile_vindo_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="xmark"]'))
)
multile_vindo_button.click()
print("View like details clicked.")
time.sleep(1)




# Step 8: Comment button interaction
# comment_box = driver.find_element(By.XPATH,'//*[@id="xmark"]') 
# comment_box.click()
# print("Comment button clicked successfully.")
# time.sleep(10)


# driver.find_element(By.XPATH, '//*[@id="commentText"]').send_keys("comment")

# send_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH,'//*[@id="feed"]/div[2]'))
# )
# send_button.click()
# time.sleep(30)




# # Step 8: song button 
# song_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/div/div/div[1]/div[5]/div/div[2]/button/svg/path'))
# )
# song_button.click()
# print("Comment button clicked successfully.")
# time.sleep(10)



# Step 9: Navigate back
# driver.back()
# print("Navigated back successfully.")
# time.sleep(5)



# # Step 10: Navigate forward
# driver.forward()
# print("Navigated forward successfully.")
# time.sleep(5)



# Step 12: profile navigated page
profile_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,'/html/body/div/aside/a[2]/span'))
)
profile_button.click()
print("profile navigated successfully.")
time.sleep(5)


# Step 13: post navigated page
post_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,'/html/body/div/aside/a[3]/span'))
)
post_button.click()
print("post navigated successfully.")
time.sleep(5)

# Step 14: chat navigated page
chat_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,"//i[@id='comment-2BrpUQK0d7SyQd5Wmez6']"))
)
chat_button.click()
print("Comment button clicked successfully.")
time.sleep(5)


# Step 14: logout navigated page
logout_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID,'Logout'))
)
logout_button.click()
print(" logout clicked successfully.")
time.sleep(5)


# Step 15: Quit the driver
driver.quit()
print("Driver closed.")


# search_button
# search_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//*[@id='SearchBtn']"))
# )
# search_button.click()
# time.sleep(5)
# driver.find_element(By.XPATH,"//*[@id='SearchInp']").send_keys("Saravanan")
# time.sleep(10)

# search_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//*[@id='SearchBtn']"))
# )
# search_button.click()
# time.sleep(5)
