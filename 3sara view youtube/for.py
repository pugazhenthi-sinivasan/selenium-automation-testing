import time 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
driver=webdriver.Chrome() 
driver.get("https://www.redbus.in/") 
driver.maximize_window() 
driver.implicitly_wait(10) 
driver.find_element(By.XPATH,'//*[@id="account_dd"]/div[1]/span').click() 
time.sleep(3) 
options= driver.find_elements (By.XPATH,"//ul[@class='header_dropdown_menu']/li/span") 
for a in options: 
   if a.text == 'Change Travel Date': 
      a.click() 
      break 
time.sleep(3) 
print("success") 