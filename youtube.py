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


# Step 1: Launch the browser
# driver = webdriver.Chrome()



# # Step 2: Navigate to the site and maximize the window
# driver.get("https://www.youtube.com/")
# driver.maximize_window()
# print("Navigated to the website 2.")
# time.sleep(1)




# # Step 3: Click on login button
# login_button_submit = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/yt-lockup-view-model/div/a/yt-collection-thumbnail-view-model/yt-collections-stack/div/div[3]/yt-thumbnail-view-model/div/img'))
# )
# login_button_submit.click()
# print("Login button clicked successfully 3.")
# time.sleep(10)