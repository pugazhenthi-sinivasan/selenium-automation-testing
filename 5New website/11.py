import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Launch Chrome
driver = webdriver.Chrome()

# Step 2: Open Google
driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(10)

# # Step 3: Wait for the search box
# wait = WebDriverWait(driver, 10)
# search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))

# # Step 4: Enter search text
# search_box.send_keys("Mr Beast")

# # Step 5: Click the search button
# search_box.submit()  # Press Enter to search

# # Step 6: Wait for results to load
# wait.until(EC.presence_of_element_located((By.ID, "search")))

# # Step 7: Print the top search result titles
# results = driver.find_elements(By.XPATH, '//h3')
# for index, result in enumerate(results[:5]):  # Print top 5 results
#     print(f"{index + 1}. {result.text}")

# # Step 8: Close the browser after some time
# time.sleep(5)
# driver.quit()
