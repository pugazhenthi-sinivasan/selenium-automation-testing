import time
from selenium import webdriver
from selenium.webdriver.common.by import By





# Step 1: Launch the browser
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.Edge()


driver.get("https://wildcardsapistaging005.freshpo.com/")
driver.maximize_window()
print("Navigated to the website 2.")

driver.implicitly_wait(5) 


login_button = driver.find_element(By.XPATH, '/html/body/header/div/nav/b[1]/a')
login_button.click()
driver.implicitly_wait(5) 

driver.find_element(By.ID, 'user_session_email').send_keys("gopika.sivakumar@fssa.freshworks.com")
driver.implicitly_wait(2)

driver.find_element(By.ID, 'user_session_password').send_keys("Password@123")
driver.implicitly_wait(2)


s_button = driver.find_element(By.XPATH, '//*[@id="new_user_session"]/fieldset/div[4]/div/button')
s_button.click()
driver.implicitly_wait(8)


driver.find_element(By.ID, 'username').send_keys("gopika.sivakumar@fssa.freshworks.com")
driver.implicitly_wait(2)

driver.find_element(By.ID, 'password').send_keys("Password@123")
driver.implicitly_wait(2)

driver.find_element(By.PARTIAL_LINK_TEXT, 'Sign in').click()

time.sleep(5)
