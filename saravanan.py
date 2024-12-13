import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

 #step 1) launch the browser
driver=webdriver.Chrome()

#2)step element contol //Navigate browser
driver.get("https://link-upp.netlify.app/")
driver.maximize_window()
time.sleep(2)

# 3)step intercthing with the sign-up button
# singup_button=WebDriverWait(driver,10).until(
    # EC.element_to_be_clickable((By.ID,"//*[@id='login']"))
click_air=WebDriverWait(driver,10).until(
      EC.element_to_be_clickable((By.XPATH,"//*[@id='form']/div[5]/span/span/a"))
)
click_air.click()
print("this is invalid email showing succesfully")

#step 4
# driver.find_element(By.ID,"username")
driver.find_element(By.XPATH,"//*[@id='username']").send_keys("haripiriya")
driver.find_element(By.XPATH,"//*[@id='Email']").send_keys("s19820@gmail.com")
driver.find_element(By.XPATH,"//*[@id='password']").send_keys("Siva@134567890")
driver.find_element(By.XPATH,"//*[@id='CPass']").send_keys("Siva@134567890")

#step 6
singup_button_submit=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR,"#submit"))
)
singup_button_submit.click()
print("submitted succesfully")
time.sleep(3)



login_button_submit=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//*[@id='login']"))
)
login_button_submit.click()
print("log in submitted succesfully")
time.sleep(20)


# #step 7
# WebDriverWait(driver,10).until(
#     EC.url_changes(driver.current_url)
# )

# #step
# WebDriverWait(driver,10).un