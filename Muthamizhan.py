import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException

# Step 1: Launch the browser
driver = webdriver.Chrome()

# Step 2: Navigate to the site and maximize the window
driver.get("https://dmedia1.netlify.app/index.html")
driver.maximize_window()
print("Navigated to the website.")
time.sleep(2)


# Step 3: Click on login button
login_button_submit = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="signupForm"]/div[7]/p/a'))
)
login_button_submit.click()
print("Login button clicked successfully.")



# Step 4: Enter login 
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("pugalpugazh@gmail.com")
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Pugal@1234")
print("Entered login credentials.")



# Step 5: Submit login 
login_button_submit=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="submitSignIn"]'))
)
login_button_submit.click()
print("log in submitted succesfully")
time.sleep(10)



# Step 6: Like button count
like_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="postContainer"]/div[1]/div[1]/span[1]'))
)
like_button.click()
print("Like button clicked successfully.")
time.sleep(5)


# Step 7: discover navigated page
discover_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,'/html/body/aside/nav/ul[1]/li[2]/a/span[2]'))
)
discover_button.click()
print("Comment button clicked successfully.")
time.sleep(5)


# Step 8: home navigated page
home_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,'/html/body/aside/nav/ul[1]/li[1]/a/span[2]'))
)
home_button.click()
print("Comment button clicked successfully.")
time.sleep(5)


# Step 9: Comment button interaction
comment_like_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="postContainer"]/div[1]/div[1]/span[3]'))
)
comment_like_button.click()
print("View like details clicked.")
time.sleep(5)
# # back button code
# multile_vindo_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div[1]/button'))
# )
# multile_vindo_button.click()
# print("View like details clicked.")
# time.sleep(40)


# typing comment
driver.find_element(By.XPATH,'/html/body/div[2]/div/input').send_keys("this image is nice")

post_comment_send=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/button'))
)
post_comment_send.click()
print("log in submitted succesfully")
time.sleep(10)


# # Step 9: Navigate back
# driver.back()
# print("Navigated back successfully.")
# time.sleep(5)



# # Step 10: Navigate forward
# driver.forward()
# print("Navigated forward successfully.")
# time.sleep(5)



# # Step 12: profile navigated page
# profile_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH,'/html/body/div/aside/a[2]/span'))
# )
# profile_button.click()
# print("Comment button clicked successfully.")
# time.sleep(5)


# # Step 13: post navigated page
# post_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH,'/html/body/div/aside/a[3]/span'))
# )
# post_button.click()
# print("Comment button clicked successfully.")
# time.sleep(5)

# # # Step 14: chat navigated page
# # chat_button = WebDriverWait(driver, 10).until(
# #     EC.element_to_be_clickable((By.XPATH,'/html/body/div/aside/a[4]/span'))
# # )
# # chat_button.click()
# # print("Comment button clicked successfully.")
# # time.sleep(5)


# # Step 14: logout navigated page
# logout_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH,'//*[@id="Logout"]/span'))
# )
# logout_button.click()
# print("Comment button clicked successfully.")
# time.sleep(5)


# # Step 15: Quit the driver
# driver.quit()
# print("Driver closed.")


# # search_button
# # search_button = WebDriverWait(driver, 10).until(
# #     EC.element_to_be_clickable((By.XPATH, "//*[@id='SearchBtn']"))
# # )
# # search_button.click()
# # time.sleep(5)
# # driver.find_element(By.XPATH,"//*[@id='SearchInp']").send_keys("Saravanan")
# # time.sleep(10)

# # search_button = WebDriverWait(driver, 10).until(
# #     EC.element_to_be_clickable((By.XPATH, "//*[@id='SearchBtn']"))
# # )
# # search_button.click()
# # time.sleep(5)
