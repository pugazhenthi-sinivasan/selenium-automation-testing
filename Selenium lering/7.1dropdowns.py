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

#select the value by visible text
# select.select_by_visible_text("Option 2")
# time.sleep(3)


#select the value value by index
# select.select_by_index(2)
# time.sleep(3)


#select the option by using a value
# select.select_by_value("1")ew
# time.sleep(3)




