import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from colorama import Fore, Style, init

driver = webdriver.Chrome()

start = time.time()
driver.get("https://www.instagram.com/")
driver.maximize_window()
time.sleep(5)

end = time.time()
load_time = end - start
print(f"Load Time: {load_time} seconds")

# Open log file once
with open("log.txt", "a") as log_file:
    log_file.write(f"Load Time: {load_time} seconds\n")

# Enter login details
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[1]/div/label/input').send_keys("mistaketamil@gmail.com")
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[2]/div/label/input').send_keys("mistake123@")
print("Entered login credentials")

with open("log.txt", "a") as log_file:
    log_file.write("Entered login credentials.\n")

time.sleep(2)

# Click login button
login_button_ = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]')
login_button_.click()
print("Clicked login button")
time.sleep(10)
with open("log.txt", "a") as log_file:
    log_file.write("Clicked login button.\n")


# Navigate to home page
home_button = driver.find_element(By.PARTIAL_LINK_TEXT, 'Home')
home_button.click()
print("Navigated to Home page")

with open("log.txt", "a") as log_file:
    log_file.write("Navigated to Home page.\n")

time.sleep(5)

# Navigate to search
search = driver.find_element(By.PARTIAL_LINK_TEXT, 'Search')
search.click()
print("Navigated to Search")

with open("log.txt", "a") as log_file:
    log_file.write("Navigated to Search.\n")  # Corrected duplicate log entry

time.sleep(5)


driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input').send_keys("song")

with open("log.txt", "a") as log_file:
    log_file.write("type of tax.\n") 
    time.sleep(10)
# print(Fore.GREEN + "type of tax." + Style.RESET_ALL)


click_search = driver.find_element(By.XPATH,"//span[@class='x1lliihq x1plvlek xryxfnj x1n2onr6 x1ji0vk5 x18bv5gf x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xvs91rp x1s688f x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj'][normalize-space()='tamil_songs_offi_']")
click_search.click()
time.sleep(5)
# Wait up to 10 seconds for an element to be visible
# wait = WebDriverWait(driver, 10)



# # Hover over an imager
# actions = ActionChains(driver)
# hover = driver.find_element(By.CLASS_NAME, '_aagw')
# actions.move_to_element(hover).perform()
# time.sleep(3)

# hover = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/div[2]/div/div/div[1]/div[2]/a/div[1]/div[2]')
# actions.move_to_element(hover).perform()
# time.sleep(3)

# hover = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/div[2]/div/div/div[1]/div[3]/a/div[1]/div[2]')
# actions.move_to_element(hover).perform()
# time.sleep(3)

# hover = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/div[2]/div/div/div[2]/div[1]/a/div[1]/div[2]')
# actions.move_to_element(hover).perform()
# time.sleep(3)

# hover = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/div[2]/div/div/div[2]/div[2]/a/div[1]/div[2]')
# actions.move_to_element(hover).perform()
# print("hover: " + str(hover))
# time.sleep(3)




actions = ActionChains(driver)

# List of XPaths to hover over
xpaths = [
    "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/div[2]/div/div/div[1]/div[2]/a/div[1]/div[2]",
    "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/div[2]/div/div/div[1]/div[3]/a/div[1]/div[2]",
    "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/div[2]/div/div/div[2]/div[1]/a/div[1]/div[2]",
    "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/div[2]/div/div/div[2]/div[2]/a/div[1]/div[2]"
]

# First hover using class name
hover = driver.find_element(By.CLASS_NAME, '_aagw')
actions.move_to_element(hover).perform()
time.sleep(3)

# Loop through each XPath
for path in xpaths:
    try:
        hover = driver.find_element(By.XPATH, path)
        actions.move_to_element(hover).perform()
        print("Hovered over element: " + str(hover))
        time.sleep(3)
    except Exception as e:
        print("Error hovering over element: ", e)

# Example: Click the first profile under search result
click_search = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@role="none"]//a')))
click_search.click()




















# # Now wait and click on the "Videos" tab using JS
# wait = WebDriverWait(driver, 10)
# click_videos = wait.until(EC.visibility_of_element_located(
#     (By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/div[1]/a[2]")
# ))
# driver.execute_script("/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/div[1]/a[2]", click_videos)
# print("Clicked Videos Tab")
# time.sleep(5)



# # Initialize colorama (for Windows compatibility)
# init(autoreset=True)

# try:
#     like_button = driver.find_element(By.CLASS_NAME, "x1rg5ohu")
#     like_button.click()
#     # Print success message in GREEN
#     print(Fore.GREEN + "Liked a post." + Style.RESET_ALL)
#     with open("log.txt", "a") as log_file:
#         log_file.write("Liked a post.\n")

# except:
#     # Print error message in RED
#     print(Fore.RED + "Failed to find the like button." + Style.RESET_ALL)

#     with open("log.txt", "a") as log_file:
#         log_file.write(Fore.RED +"Failed to find the like button.\n"+ Style.RESET_ALL)


# # Scroll down
# driver.execute_script("window.scrollTo(0, 1000)")
# time.sleep(5)


# # click_search = driver.find_element(By.XPATH,'//*[@id="mount_0_0_zY"]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/div[2]/div/div/div[3]/div[2]/a/div[2]')
# # click_search.click()
# # time.sleep(20)

# # Close browser
# driver.quit()
# # Quality Assurance


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from colorama import Fore, Style, init

# # Initialize colorama
# init(autoreset=True)

# # Reusable logging function
# def log_event(message):
#     with open("log.txt", "a") as log_file:
#         log_file.write(message + "\n")

# # Setup Chrome driver
# driver = webdriver.Chrome()
# wait = WebDriverWait(driver, 10)
# actions = ActionChains(driver)

# # Track load time
# start = time.time()
# driver.get("https://www.instagram.com/")
# driver.maximize_window()
# time.sleep(5)
# end = time.time()
# load_time = end - start
# print(f"Load Time: {load_time:.2f} seconds")
# log_event(f"Load Time: {load_time:.2f} seconds")

# # Login
# driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[1]/div/label/input').send_keys("mistaketamil@gmail.com")
# driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[2]/div/label/input').send_keys("mistake123@")
# log_event("Entered login credentials.")
# print("Entered login credentials")
# time.sleep(2)

# driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]').click()
# log_event("Clicked login button.")
# print("Clicked login button")
# time.sleep(10)

# # Navigate to Home
# home_button = driver.find_element(By.PARTIAL_LINK_TEXT, 'Home')
# home_button.click()
# log_event("Navigated to Home page.")
# print("Navigated to Home page")
# time.sleep(5)

# # Navigate to Search
# search_button = driver.find_element(By.PARTIAL_LINK_TEXT, 'Search')
# search_button.click()
# log_event("Navigated to Search.")
# print("Navigated to Search")
# time.sleep(5)

# # Type in search bar
# search_input = driver.find_element(By.XPATH, 
#     '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input')
# search_input.send_keys("song")
# log_event("Searched for 'song'")
# time.sleep(10)

# # Click on a profile from results
# try:
#     profile = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, "//span[normalize-space()='tamil_songs_offi_']")))
#     profile.click()
#     log_event("Clicked on profile: tamil_songs_offi_")
#     print("Clicked on profile")
#     time.sleep(5)
# except Exception as e:
#     log_event("Failed to click on profile.")
#     print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

# # Hover over images
# xpaths = [
#     "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/div[2]/div/div/div[1]/div[2]/a/div[1]/div[2]",
#     "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/div[2]/div/div/div[1]/div[3]/a/div[1]/div[2]",
#     "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/div[2]/div/div/div[2]/div[1]/a/div[1]/div[2]",
#     "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/div[2]/div/div/div[2]/div[2]/a/div[1]/div[2]"
# ]

# for path in xpaths:
#     try:
#         hover = driver.find_element(By.XPATH, path)
#         actions.move_to_element(hover).perform()
#         log_event(f"Hovered over element: {path}")
#         print("Hovered on post")
#         time.sleep(3)
#     except Exception as e:
#         log_event(f"Error hovering: {e}")
#         print(Fore.RED + "Hover failed: " + str(e))

# # Optional: Close browser
# driver.quit()
# log_event("Closed browser.")
# print("Browser closed")
