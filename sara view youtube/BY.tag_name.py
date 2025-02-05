from selenium import webdriver
from selenium.webdriver.common.by import By


driver =webdriver.Chrome()

driver.get("https://www.naukri.com/")
driver.maximize_window()
driver.implicitly_wait(10)
lista=driver.find_element(By.TAG_NAME,"a")
print(len(lista))
driver.quit()
