import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore, Style, init

# Initialize Colorama for colored console output
init()

# Step 1: Launch the browser
driver = webdriver.Chrome()
driver.get("https://dmedia1.netlify.app/index.html")
driver.maximize_window()
print(Fore.GREEN + "Navigated to the website." + Style.RESET_ALL)
time.sleep(1)

start = time.time()
end = time.time()
load_time = end - start
print(f"Load Time: {load_time} seconds")

# Log load time
with open("log.txt", "a") as log_file:
    log_file.write(f"Load Time: {load_time} seconds\n")

# Step 2: Click on login button
try:
    login_button_submit = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="signupForm"]/div[7]/p/a'))
    )
    login_button_submit.click()
    print(Fore.GREEN + "Login button clicked successfully." + Style.RESET_ALL)
except:
    print(Fore.RED + "Login button not found!" + Style.RESET_ALL)

time.sleep(1)

# Step 3: Enter login credentials
try:
    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("pugalpugazh@gmail.com")
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Pugal@1234")
    print(Fore.GREEN + "Entered login credentials." + Style.RESET_ALL)
except:
    print(Fore.RED + "Login fields not found!" + Style.RESET_ALL)

time.sleep(1)

# Step 4: Submit login
try:
    driver.find_element(By.XPATH, '//*[@id="submitSignIn"]').click()
    print(Fore.GREEN + "Logged in successfully." + Style.RESET_ALL)
except:
    print(Fore.RED + "Login submit button not found!" + Style.RESET_ALL)

time.sleep(2)

# Step 5: Like a post
try:
    like_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="postContainer"]/div[1]/div[1]/span[1]'))
    )
    like_button.click()
    print(Fore.GREEN + "Like button clicked successfully." + Style.RESET_ALL)
except:
    print(Fore.RED + "Like button not found!" + Style.RESET_ALL)

time.sleep(2)

# Step 6: Comment on a post
try:
    comment_open_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="postContainer"]/div[1]/div[1]/span[3]'))
    )
    comment_open_button.click()
    print(Fore.GREEN + "Opened comment section." + Style.RESET_ALL)

    time.sleep(2)

    driver.find_element(By.XPATH, '/html/body/div/div/textarea').send_keys("Hi there!")
    print(Fore.GREEN + "Typed comment: 'Hi there!'." + Style.RESET_ALL)

    post_comment_send = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'submit-comment-button'))
    )
    post_comment_send.click()
    print(Fore.GREEN + "Comment posted successfully." + Style.RESET_ALL)

    close_comment=WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,'/html/body/div/div/div[1]/button'))
    )
    close_comment.click()
    print(Fore.GREEN + "Closed comment section." + Style.RESET_ALL)


    
except:
    print(Fore.RED + "Comment section not found!" + Style.RESET_ALL)

time.sleep(3)

# Step 7: Open Profile and Follow User
try:
    profile_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="postContainer"]/div[1]/div[2]/a'))
    )
    profile_button.click()
    print(Fore.GREEN + "Profile opened successfully." + Style.RESET_ALL)

    follow_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="action-button"]/li[1]/button'))
    )
    follow_button.click()
    print(Fore.GREEN + "Followed the user." + Style.RESET_ALL)
except:
    print(Fore.RED + "Profile or follow button not found!" + Style.RESET_ALL)

time.sleep(3)

# Step 8: Open Messages and Send Message
try:
    message_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'messageButton'))
    )
    message_button.click()
    print(Fore.GREEN + "Message button clicked." + Style.RESET_ALL)

    driver.find_element(By.ID, 'messageInput').send_keys("Today is a nice day")
    driver.find_element(By.ID, 'sendMessageButton').click()
    print(Fore.GREEN + "Message sent successfully." + Style.RESET_ALL)
except:
    print(Fore.RED + "Message section not found!" + Style.RESET_ALL)

time.sleep(3)

# Step 9: Search for a Hashtag
try:
    driver.find_element(By.XPATH, '//*[@id="search-bar"]').send_keys("#back")
    print(Fore.GREEN + "Searched for '#back'." + Style.RESET_ALL)
except:
    print(Fore.RED + "Search bar not found!" + Style.RESET_ALL)

time.sleep(3)

# Step 10: Upload an Image
try:
    driver.find_element(By.XPATH, '/html/body/aside/nav/ul[1]/li[4]/a/span[2]').click()
    print(Fore.GREEN + "Navigated to upload page." + Style.RESET_ALL)

    driver.find_element(By.XPATH, '//*[@id="file"]').send_keys(r"C:\PUGAL_FSSA\selenium-automation-testing\selenium.png")
    driver.find_element(By.ID, 'caption').send_keys("Tamil Nadu is the southernmost state of India")
    driver.find_element(By.ID, 'hashtags').send_keys("#Tamil Nadu is the southernmost state of India")
    print(Fore.GREEN + "Image uploaded successfully." + Style.RESET_ALL)
except:
    print(Fore.RED + "Image upload failed!" + Style.RESET_ALL)

time.sleep(3)

# Step 11: Edit Profile
try:
    driver.find_element(By.XPATH, '//*[@id="edit-profile-btn"]').click()
    print(Fore.GREEN + "Editing profile." + Style.RESET_ALL)

    username_field = driver.find_element(By.ID, "edit-name")
    username_field.clear()
    username_field.send_keys("pugal")

    driver.find_element(By.ID, "save-profile-btn").click()
    print(Fore.GREEN + "Profile saved successfully." + Style.RESET_ALL)

    seved_button = driver.switch_to.alert
    seved_button.accept()
except:
    print(Fore.RED + "Profile update failed!" + Style.RESET_ALL)

time.sleep(3)

# Step 12: Logout
try:
    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="signOut"]/span[2]'))
    )
    logout_button.click()
    print(Fore.GREEN + "Logged out successfully." + Style.RESET_ALL)
except:
    print(Fore.RED + "Logout button not found!" + Style.RESET_ALL)

time.sleep(3)

# Step 13: Close Browser
driver.quit()
print(Fore.RED + "Driver closed. End of test." + Style.RESET_ALL)
