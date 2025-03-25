import time
from selenium import webdriver
from selenium.webdriver.common.by import By


pugal = webdriver. Chrome()
pugal.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
pugal.maximize_window()
time.sleep(5)
pugal.execute_script("window.scrollTo (0, document.body.scrollHeight);")
checkboxes = pugal.find_elements (By.XPATH,"//input[@type='checkbox']")

pugal.quit()