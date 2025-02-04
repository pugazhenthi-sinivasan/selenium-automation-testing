import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoAlertPresentException

driver = webdriver. Chrome()

driver.get("https://www.instagram.com/")
driver.maximize_window()
time.sleep(5)


driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[1]/div/label/input').send_keys("mistaketamil@gmail.com")
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[2]/div/label/input').send_keys("mistake123@")
print("Entered login credentials")
time.sleep(4)




login_button_=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[3]')
login_button_.click()
print("login_button")
time.sleep(15)


# seved_button=driver.switch_to.alert
# print("switch")
# seved_button.accept()
# time.sleep(5)

home_button_=driver.find_element(By.XPATH,'//*[@id="mount_0_0_mx"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[1]/div/span/div/a/div/div[2]')
home_button_.click()
print("not_button")
time.sleep(10)


# item_buttons = driver.find_elements(By.XPATH,'//*[@id="mount_0_0_yA"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div[1]/div[1]/div/div[2]/div/div[1]/div/article[1]/div/div[3]/div/div/section[1]/div[1]/span[1]/div/div/div/span/svg/path')
# for button in item_buttons:
#     button.click()
#     time.sleep(40)



not_button_=driver.find_element(By.XPATH,'//*[@id="mount_0_0_X4"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[5]/div/div/span/div/a/div/div[2]/div/div/span/span')
not_button_.click()
print("not_button")
time.sleep(5)
    
# driver.execute_script("window.scrollTo(0, 1000)")
# time.sleep(5)


