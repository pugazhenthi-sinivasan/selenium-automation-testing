from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/")
driver.maximize_window()

# Find all links on the page
all_links = driver.find_elements(By.TAG_NAME, 'a')
print(f"Total number of links on the page: {len(all_links)}")

# Optional: if you want to print the text of the links too
# for link in all_links:
#     print(link.text)

# Close the browser after some time (optional)
time.sleep(3)
driver.quit()
