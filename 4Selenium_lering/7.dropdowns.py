import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")
time.sleep(6)
driver.maximize_window()

dropdown_element =driver.find_element(By.ID,"dropdown")
select = Select(dropdown_element)
option_count=len(select.options)

# expected_count=5
expected_count=3

if option_count==expected_count:
    print("test case passed. count is correct")
else:
    print("test case failed. count is incorrect")

