import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoAlertPresentException



# Step 1: Launch the browser
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.Edge()



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
time.sleep(3)



#uplond page
click_uplond_button =driver.find_element(By.XPATH,'/html/body/aside/nav/ul[1]/li[4]/a/span[2]')
click_uplond_button.click()
print("uplond_navegasain")
time.sleep(4)


file=driver.find_element(By.XPATH,'//*[@id="file"]')
file.send_keys(r"C:\PUGAL_FSSA\selenium-automation-testing\selenium.png")
print("uplond")
time.sleep(4)


file=driver.find_element(By.ID,'caption')
file.send_keys("Tamil Nadu is the southernmost state of India")
file=driver.find_element(By.ID,'hashtags')
file.send_keys("Tamil Nadu is the southernmost state of India")

click_saved_img =driver.find_element(By.ID,'postButton')
click_saved_img.click()
print("postButton")
time.sleep(6)
