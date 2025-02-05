from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://register.rediff.com/register/register.php?FormName=user_details")
driver.maximize_window()

male_option=driver.find_element(By.XPATH,'//*[@id="tblcrtac"]/tbody/tr[24]/td[3]/input[1]')
female_option=driver.find_element(By.XPATH,'//*[@id="tblcrtac"]/tbody/tr[24]/td[3]/input[2]')
female_option.click()
print(female_option.is_selected())
print(female_option.is_enabled())
print(female_option.is_displayed())
print(male_option.is_selected())
time.sleep(4)