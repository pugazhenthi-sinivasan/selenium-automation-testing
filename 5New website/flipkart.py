import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Create or open a log file
with open("log.txt", "w") as log_file:
    log_file.write("Log File - Selenium Automation\n")
    log_file.write("====================================\n")

# Step 1: Launch the browser
flipkart = webdriver.Chrome()
start = time.time()  # Start time

# Step 2: Navigate to YouTube and maximize the window
flipkart.get("https://www.flipkart.com/?redirectFrom=logout")
flipkart.maximize_window()
end = time.time()  # End time

# Calculate and log the load time
load_time = end - start
with open("log.txt", "a") as log_file:
    log_file.write(f"Website Load Time: {load_time} seconds\n")
    log_file.write("Navigated to flipkart successfully.\n")

print(f"Load Time: {load_time} seconds")
time.sleep(4)

# Step 3: Enter search text
search_text_box = flipkart.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input')
search_text_box.send_keys("nothing phone 2a")
print("Opened flipkart and entered search text.")
with open("log.txt", "a") as log_file:
    log_file.write("Entered 'phone' in the search box.\n")

time.sleep(3)

# Step 4: Click search button
search_click = flipkart.find_element(By.XPATH, "//button[@type='submit']//*[name()='svg']")
search_click.click()
time.sleep(4)


# Scroll down
# flipkart.execute_script("window.scrollTo(0, 1000)")
# time.sleep(5)


# Step 5: Click on the first video
# click_phone = flipkart.find_element(By.XPATH,"/html/body/div/div/div[3]/div[1]/div[2]/div[17]")
# # Scroll into view
# flipkart.execute_script("arguments[0].scrollIntoView();", click_phone)
# click_phone.click()
product_link = WebDriverWait(flipkart, 10).until(
    EC.element_to_be_clickable((By.XPATH,"//div[@class='yPq5Io']//div//img[@alt='Nothing Phone (2a) 5G (White, 128 GB)']"))
)
product_link.click()
print("Clicked on the video.")
with open("log.txt", "a") as log_file:
    log_file.write("Clicked on the first video.\n")
time.sleep(30)



search_click = flipkart.find_element(By.CSS_SELECTOR,"col col-2-12 flex")
search_click.click()
time.sleep(5)

click_phone = flipkart.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[1]/div[1]/div/div")
click_phone.click()
time.sleep(6)
print("ok")


# seved_button=flipkart.switch_to.alert
# print("switch")
# seved_button.accept()
# time.sleep(5)

tabs= flipkart.window_handles
flipkart.switch_to.window(tabs[-1])
print ("window switch")

click_page=flipkart.find_element(By.XPATH,"//li[contains(@class, 'flex')]//span")
click_page.click()
time.sleep(5)
print("something")
# Hover over an image
# actions = ActionChains(flipkart)
# hover = flipkart.find_element(By.XPATH, "//a[@class='GK7Ljp']//div[@class='_0QyAeO']")
# actions.move_to_element(hover).perform()
# flipkart.implicitly_wait(5)
# time.sleep(3)
# print("correct working")

# hover = flipkart.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div[1]/ul/li[2]/div/div/img')
# actions.move_to_element(hover).perform()
# time.sleep(3)

# hover = flipkart.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/div[2]/div/div/div[1]/div[3]/a/div[1]/div[2]')
# actions.move_to_element(hover).perform()
# time.sleep(3)

# hover = flipkart.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/div[2]/div/div/div[2]/div[1]/a/div[1]/div[2]')
# actions.move_to_element(hover).perform()
# time.sleep(3)

# hover = flipkart.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/div[2]/div/div/div[2]/div[2]/a/div[1]/div[2]')
# actions.move_to_element(hover).perform()
# print("hover"+hover)
# time.sleep(3)


# click_videos= flipkart.find_element(By.CLASS_NAME, '_aagw')  
# click_videos.click()
# time.sleep(5)





# # Step 6: Click Subscribe
# subscribe_button = flipkart.find_element(By.XPATH, '//*[@id="subscribe-button-shape"]/button/yt-touch-feedback-shape/div/div[2]')
# subscribe_button.click()
# print("Subscribed to the channel.")
# with open("log.txt", "a") as log_file:
#     log_file.write("Clicked on Subscribe button.\n")

# time.sleep(5)

# # Step 7: Click 'Sign In' if required
# try:
#     sign_in_button = flipkart.find_element(By.XPATH, '//*[@id="button"]/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]')
#     sign_in_button.click()
#     print("Clicked on Sign In.")
#     with open("log.txt", "a") as log_file:
#         log_file.write("Clicked on Sign In button.\n")
#     time.sleep(30)
# except:
#     print("Sign In button not found, skipping...")
#     with open("log.txt", "a") as log_file:
#         log_file.write("Sign In button not found.\n")


# search_box = flipkart.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div[1]/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
# search_box.send_keys("pugazhenthi.sinivasan@fssa.freshworks.com")
# time.sleep(50)



# sign_email_button = flipkart.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]')
# sign_email_button.click()
# time.sleep()

# # Step 8: Navigate back twice  
# flipkart.back()
# time.sleep(5)

# flipkart.back()
# time.sleep(5)

# print("Navigation completed.")
# with open("log.txt", "a") as log_file:
#     log_file.write("Navigation back completed.\n")

# # Close the browser
# flipkart.quit()
# print("Browser closed.")
# with open("log.txt", "a") as log_file:
#     log_file.write("Browser closed.\n")


flipkart.quit()