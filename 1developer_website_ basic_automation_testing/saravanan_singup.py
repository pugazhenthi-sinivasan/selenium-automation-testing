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
click_air=WebDriverWait(driver,10).until(
      EC.element_to_be_clickable((By.XPATH,"//*[@id='form']/div[5]/span/span/a"))
)
click_air.click()
print("this is invalid email showing succesfully")

#step 4
# driver.find_element(By.ID,"username")
driver.find_element(By.XPATH,"//*[@id='username']").send_keys("haripiriya")
driver.find_element(By.XPATH,"//*[@id='Email']").send_keys("taamlilllppp@gmail.com")
driver.find_element(By.XPATH,"//*[@id='password']").send_keys("Siva@134567890")
driver.find_element(By.XPATH,"//*[@id='CPass']").send_keys("Siva@134567890")

#step 6:submit
singup_button_submit=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR,"#submit"))
)
singup_button_submit.click()
print("submitted succesfully")
time.sleep(3)


# login page validation
login_button_submit=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//*[@id='login']"))
)
login_button_submit.click()
print("log in validation succesfully")
time.sleep(8)


driver.find_element(By.XPATH,"//*[@id='Login-Email']").send_keys("taamlilllppp@gmail.com")
driver.find_element(By.XPATH,"//*[@id='Login-password']").send_keys("Siva@134567890")
time.sleep(8)

# login page
login_button_submit=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//*[@id='login']"))
)
login_button_submit.click()
print("log in submitted succesfully")
time.sleep(10)

# Click the like button on the page
like_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='heart-qjh0Ho8Oxh4U24N9GK9l']"))
)
like_button.click()
print("Like count successfully.")
# Wait for 10 seconds 
time.sleep(5)

view_like_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='showlike-qjh0Ho8Oxh4U24N9GK9l']"))
)
view_like_button.click()
time.sleep(5)

# Dismiss the confirmation (click Cancel)
# alert = driver.switch_to.alert
# alert.dismiss()

# driver.back










