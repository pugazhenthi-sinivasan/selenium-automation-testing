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
driver.get("https://funkyfindz.netlify.app/")
driver.maximize_window()
print("Navigated to the website 2.")
time.sleep(2)


# Step 3: Click on login button
login_button_submit = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'showSignin'))
)
login_button_submit.click()
print("Login button clicked successfully 3.")



# Step 4: Enter login 
driver.find_element(By.ID, 'email').send_keys("pugalpugazh@gmail.com")
driver.find_element(By.XPATH, '//*[@id="signinForm"]/div[2]/input').send_keys("Pugal@1234")
print("Entered login credentials 4.")



# Step 5: Submit login 
login_button_submit=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="signinForm"]/button'))
)
login_button_submit.click()
print("log in submitted succesfully 5")
time.sleep(5)


# create an instance of the ActionChains class
actions=ActionChains(driver)

driver_click.fin
actions.click(driver_click).perform()

