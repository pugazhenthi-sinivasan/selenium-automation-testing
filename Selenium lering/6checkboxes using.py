import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
browser = webdriver. Chrome()
browser.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
browser.maximize_window()
time.sleep(4)
browser.execute_script("window.scrollBy(0, 300);")
time.sleep(2)

checkboxes = browser.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in checkboxes:
    checkbox.send_keys(Keys. SPACE)
    checked_count =0
for checkbox in checkboxes:
    if checkbox.is_selected():
      checked_count +=1

expected_checked_count = 7
if checked_count == expected_checked_count:
        print('Checkbox count verified')
else:
     print('Checbox count mismatch')