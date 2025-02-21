from selenium import webdriver
from selenium.webdriver.common.by import By
import time



driver =webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Alerts.html")
driver.maximize_window()



alert_button=driver.find_element(By.XPATH,'//*[@id="OKTab"]/button')
alert_button.click()
alert_button=driver.switch_to.alert
alert_button.accept()
time.sleep(2)


alert_butto=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a')
alert_butto.click()
alert_butt=driver.find_element(By.XPATH,'//*[@id="CancelTab"]/button')
alert_butt.click()
time.sleep(2)
alert_butt=driver.switch_to.alert
alert_butt.dismiss()
time.sleep(2)
