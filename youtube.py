import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


with open("log.txt", "w") as log_file:
    log_file.write("Log File - Selenium Automation\n")
    log_file.write("====================================\n")

# Launch the browser
driver = webdriver.Chrome()
start = time.time()  # Start time

# Navigate YouTube maximize the window
driver.get("https://www.youtube.com/")
driver.maximize_window()
end = time.time()  # End time

# Calculate and log the load time
load_time = end - start
print(f"Load Time: {load_time} seconds")
time.sleep(4)

    
    
search_box = driver.find_element(By.XPATH, '//*[@id="center"]/yt-searchbox/div[1]/form/input')
search_box.send_keys("Freshworks Social Impact")
print("Opened YouTube and entered search text.")
driver.implicitly_wait(2)


#search button
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/ytd-app[1]/div[1]/div[2]/ytd-masthead[1]/div[4]/div[2]/yt-searchbox[1]/button[1]/yt-icon[1]/span[1]/div[1]'))
)
search_button.click()
print("Search submitted successfully.")
driver.implicitly_wait(4)
 

click_Fssa=driver.find_element(By.PARTIAL_LINK_TEXT,'Freshworks Social Impact')
click_Fssa.click()
driver.implicitly_wait(4)
    
click_vidoes=driver.find_element(By.XPATH,'//*[@id="items"]/ytm-shorts-lockup-view-model-v2[1]/ytm-shorts-lockup-view-model/a/div/img')
click_vidoes.click()
time.sleep(10)


driver.back()
time.sleep(5)


click_vidoes=driver.find_element(By.PARTIAL_LINK_TEXT,'Videos')
click_vidoes.click()
time.sleep(5)


j=driver.find_element(By.PARTIAL_LINK_TEXT,'Batch2 Graduation Day')
j.click()
time.sleep(5)


driver.back()
time.sleep(5)


Shorts=driver.find_element(By.XPATH,'//*[@id="tabsContent"]/yt-tab-group-shape/div[1]/yt-tab-shape[3]/div[1]')
Shorts.click()
time.sleep(5)

 
Shorts_video=driver.find_element(By.XPATH,'//*[@id="content"]/ytm-shorts-lockup-view-model-v2/ytm-shorts-lockup-view-model/a/div/img')
Shorts_video.click()
time.sleep(10)

driver.back()
time.sleep(2)

Playlists=driver.find_element(By.XPATH,'//*[@id="tabsContent"]/yt-tab-group-shape/div[1]/yt-tab-shape[4]/div[1]')
Playlists.click()
# driver.implicitly_wait(5)
time.sleep(5)



Playlists_vi = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="items"]/yt-lockup-view-model/div/a/yt-collection-thumbnail-view-model/yt-collections-stack/div/div[3]/yt-thumbnail-view-model/div/img'))
)
Playlists_vi.click()
time.sleep(10)

driver.find_element(By.XPATH,'//*[@id="buttons"]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]').click()
time.sleep(5)

search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div[1]/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
search_box.send_keys("mistaketamil@gmail.com")
time.sleep(5)



sign_email_button = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span')
sign_email_button.click()
time.sleep(10)



# Navigate back 
driver.back()
time.sleep(5)

driver.back()
time.sleep(6)


# Enter search text
search_box = driver.find_element(By.XPATH, '//*[@id="center"]/yt-searchbox/div[1]/form/input')
search_box.send_keys("Mr Beast")
print("Opened YouTube and entered search text.")
time.sleep(1)

# search button
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/ytd-app[1]/div[1]/div[2]/ytd-masthead[1]/div[4]/div[2]/yt-searchbox[1]/button[1]/yt-icon[1]/span[1]/div[1]'))
)
search_button.click()
print("Search submitted successfully.")
time.sleep(5)

# Click video
video = driver.find_element(By.XPATH, '//*[@id="video-title"]/yt-formatted-string')
video.click()
print("Clicked on the video.")
time.sleep(6)


# Close the browser
driver.quit()
print("Browser closed.")

    
    


