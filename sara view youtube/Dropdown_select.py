import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://register.rediff.com/register/register.php?FormName=user_details")
driver.maximize_window()
driver.implicitly_wait(10)
day=driver.find_element(By.XPATH,'//*[@id="tblcrtac"]/tbody/tr[22]/td[3]/select[1]')
dayoption=Select(day)
dayoption=Select(day)
dayoption.select_by_index(2)
time.sleep(3)
dayoption.select_by_value("07")
time.sleep(3)
# dayoption.select_by_visible_text("OCT")
# time.sleep(3)
driver.quit()


