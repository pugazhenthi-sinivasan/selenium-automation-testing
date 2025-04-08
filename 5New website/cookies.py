import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver=webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(5)


all_cookies=driver.get_cookies()
print("number of cookies present",len(all_cookies))

#printing all cookies name
for c in all_cookies:
   # print(c)
   print(c.get('name'))#print all values of name attribute
   print(c.get('value'))#print all values of value attribute

   driver.quit()

