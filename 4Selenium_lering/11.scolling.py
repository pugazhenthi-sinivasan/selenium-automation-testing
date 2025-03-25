from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome()
driver.get("https://www.naukri.com/")
driver.maximize_window()
time.sleep(2)

# Scroll down by 600px
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(2)

# Scroll down by 300px
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(2)

# Find an element and scroll it into view
element = driver.find_element(By.XPATH, '//*[@id="standard-collection-wdgt"]/div/h2')
driver.execute_script("arguments[0].scrollIntoView();", element)
time.sleep(2)

# Simulate infinite scrolling by scrolling down repeatedly
for _ in range(5):  # 5 times for example
    driver.execute_script("window.scrollBy(0, 800);")
    time.sleep(2)

# Close the browser
driver.quit()

