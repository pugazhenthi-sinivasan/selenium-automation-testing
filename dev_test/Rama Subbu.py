import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
print("log in submitted succesfully ")
time.sleep(4)


driver.execute_script("window.scrollTo(0, 1000)")
time.sleep(5)


image_button=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="productcontainer"]/div[10]/div/img'))
)
image_button.click()
print("Open image succesfully")
time.sleep(5)


Clickhart_button=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.CLASS_NAME,'button'))
)
Clickhart_button.click()
print("Open succesfully5")
time.sleep(5)


seved_button=driver.switch_to.alert
print("switch")
seved_button.accept()
time.sleep(5)

Cart_button=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'/html/body/nav/div/a[2]/i'))
)
Cart_button.click()
print("Cart_button")
time.sleep(5)


# /////////

Cart_remove=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.CLASS_NAME,'remove-button'))
)
Cart_remove.click()
print("Cart_remove")
time.sleep(5)


seved_button=driver.switch_to.alert
print("switch")
seved_button.accept()
time.sleep(5)

# ///////

driver.refresh()
time.sleep(5)


back_button=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.CLASS_NAME,'back-button'))
)
back_button.click()
print("back_button")
time.sleep(5)


Wishlist_button=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'/html/body/nav/div/a[3]'))
)
Wishlist_button.click()
print("Wishlist_button")
time.sleep(5)


driver.back()
driver.refresh()

buy_now_button=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="buy-now"]'))
)
buy_now_button.click()
print("buy_now_button")
time.sleep(5)







pay_button=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="pay-button"]'))
)
pay_button.click()
print("pay_button")
time.sleep(5)





driver.find_element(By.ID,'name').send_keys("pugal")
driver.find_element(By.ID,'address').send_keys(" New Bangaru Naidu Colony,. K.K. Nagar (West), Chennai - 600078.")
driver.find_element(By.ID,'email').send_keys("pugalpugazh@gmail.com")
driver.find_element(By.ID,'phone').send_keys("9135627890")
time.sleep(5)


next_button=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="userDetailsForm"]/button'))
)
next_button.click()
print("next_button")
time.sleep(5)


