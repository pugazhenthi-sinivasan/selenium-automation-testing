import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

 #step 1) launch the browser
driver=webdriver.Chrome()

#2)step element contol //Navigate browser
driver.get("https://dmedia1.netlify.app/")
driver.maximize_window()
time.sleep(2)

# 3)step intercthing with the sign-up button
# singup_button=WebDriverWait(driver,10).until(
    # EC.element_to_be_clickable((By.XPATH,"//*[@id='login']"))
# singup_button=WebDriverWait(driver,10).until(
#       EC.element_to_be_clickable((By.XPATH,"//*[@id='form']/div[5]/span/span/a"))
# )
# singup_button.click()
# print("this is invalid email showing succesfully")

#step 4
# driver.find_element(By.ID,"username")
driver.find_element(By.XPATH,"//*[@id='name']").send_keys("Sivakuma")
driver.find_element(By.XPATH,"//*[@id='username']").send_keys("Siva")
driver.find_element(By.XPATH,"//*[@id='emailError'']").send_keys("siva20@gmail.com")
driver.find_element(By.XPATH,"//*[@id='rPassword']").send_keys("Siva@134")
driver.find_element(By.XPATH,"//*[@id='CPass']").send_keys("Siva@134")
time.sleep(30)

#step 6
singup_button_submit=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//*[@id='submit']"))
)
singup_button_submit.clear
print("submitted succesfully")
time.sleep(2)