import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoAlertPresentException

# Step 1: Launch the browser
driver = webdriver.Chrome()



# Step 2: Navigate to the site and maximize the window
driver.get("https://www.youtube.com/")
driver.maximize_window()
print("Navigated to the website 2.")
time.sleep(4)



# Step 4: Enter login 
driver.find_element(By.XPATH, '//*[@id="center"]/yt-searchbox/div[1]/form/input').send_keys("mr beast ")
print("open the youtube")
time.sleep(1)



# Step 5: Submit login 
searche_button_submit=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'/html[1]/body[1]/ytd-app[1]/div[1]/div[2]/ytd-masthead[1]/div[4]/div[2]/yt-searchbox[1]/button[1]/yt-icon[1]/span[1]/div[1]'))
)
searche_button_submit.click()
print("log in submitted succesfully 5")
time.sleep(5)




conform=driver.find_element(By.XPATH,'//*[@id="video-title"]/yt-formatted-string')
conform.click()

print("Login button clicked successfully 3.")
time.sleep(6)


click_sub=driver.find_element(By.XPATH,'//*[@id="subscribe-button-shape"]/button/yt-touch-feedback-shape/div/div[2]')
click_sub.click()
time.sleep(5)


click_sub=driver.find_element(By.XPATH,'//*[@id="button"]/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]')
click_sub.click()
time.sleep(5)

driver.back()
time.sleep(5)


driver.back()
time.sleep(5)

