import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
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
print(Fore.GREEN + "type of tax." + Style.RESET_ALL)


click_search = driver.find_element(By.XPATH,"//span[@class='x1lliihq x1plvlek xryxfnj x1n2onr6 x1ji0vk5 x18bv5gf x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xvs91rp x1s688f x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj'][normalize-space()='tamil_songs_offi_']")
click_search.click()
time.sleep(5)
# Wait up to 10 seconds for an element to be visible
# wait = WebDriverWait(driver, 10)



# Hover over an image
actions = ActionChains(driver)
hover = driver.find_element(By.CLASS_NAME, '_aagw')
actions.move_to_element(hover).perform()
time.sleep(3)

hover = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/div[2]/div/div/div[1]/div[2]/a/div[1]/div[2]')
actions.move_to_element(hover).perform()
time.sleep(3)

hover = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/div[2]/div/div/div[1]/div[3]/a/div[1]/div[2]')
actions.move_to_element(hover).perform()
time.sleep(3)

hover = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/div[2]/div/div/div[2]/div[1]/a/div[1]/div[2]')
actions.move_to_element(hover).perform()
time.sleep(3)

hover = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/div[2]/div/div/div[2]/div[2]/a/div[1]/div[2]')
actions.move_to_element(hover).perform()
print("hover"+hover)
time.sleep(3)


click_videos= driver.find_element(By.CLASS_NAME, '_aagw')  
click_videos.click()
time.sleep(5)




# Initialize colorama (for Windows compatibility)
init(autoreset=True)

try:
    like_button = driver.find_element(By.CLASS_NAME, "x1rg5ohu")
    like_button.click()
    # Print success message in GREEN
    print(Fore.GREEN + "Liked a post." + Style.RESET_ALL)
    with open("log.txt", "a") as log_file:
        log_file.write("Liked a post.\n")

except:
    # Print error message in RED
    print(Fore.RED + "Failed to find the like button." + Style.RESET_ALL)

    with open("log.txt", "a") as log_file:
        log_file.write(Fore.RED +"Failed to find the like button.\n"+ Style.RESET_ALL)


# Scroll down
driver.execute_script("window.scrollTo(0, 1000)")
time.sleep(5)


# click_search = driver.find_element(By.XPATH,'//*[@id="mount_0_0_zY"]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/div[2]/div/div/div[3]/div[2]/a/div[2]')
# click_search.click()
# time.sleep(20)

# Close browser
driver.quit()
# Quality Assurance