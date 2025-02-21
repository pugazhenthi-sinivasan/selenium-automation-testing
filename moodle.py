import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Launch the browser
driver = webdriver.Chrome()
start = time.time()
# Step 2: Navigate to the site and maximize the window
driver.get("https://moodle.myfssa.in/mod/solo/attempt/manageattempts.php?id=988&attemptid=0&stepno=1")
end = time.time()
# Calculate the load time
load_time = end - start
print(f"Load Time: {load_time} seconds")
driver.maximize_window()
print("Navigated to the website 2.")
time.sleep(3)

# Step 4: Enter login 
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("psrinivasan")
driver.find_element(By.ID, 'password').send_keys("Pugal@9629")
print("Entered username password")
time.sleep(1)


login_button_=driver.find_element(By.XPATH,'//*[@id="loginbtn"]')
login_button_.click()
time.sleep(6)
print("login_button")



driver.refresh()
time.sleep(20)
print("2")


login_button_=driver.find_element(By.XPATH,'//*[@id="67a5fc19cefed67a5fc19c9c1c7_button"]')
login_button_.click()
time.sleep(15)
print("login_button")



voies_button_=driver.find_element(By.XPATH,'//*[@id="filter_poodll_controlbar_AUTOID"]/div[4]/button[1]')
voies_button_.click()
time.sleep(5)
print("login_button")





login_button_=driver.find_element(By.XPATH,'//*[@id="filter_poodll_controlbar_AUTOID_fpminimal_audioplayer"]/button')
login_button_.click()
time.sleep(10)
print("login_button")



login_button_=driver.find_element(By.XPATH,'//*[@id="filter_poodll_controlbar_AUTOID"]/div[4]/div[4]/a/i')
login_button_.click()
time.sleep(5)
print("login_button")