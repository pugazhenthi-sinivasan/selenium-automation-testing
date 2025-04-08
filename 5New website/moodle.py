# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Step 1: Launch the browser
# driver = webdriver.Chrome()
# start = time.time()
# # Step 2: Navigate to the site and maximize the window
# driver.get("https://moodle.myfssa.in/mod/solo/attempt/manageattempts.php?id=988&attemptid=0&stepno=1")
# end = time.time()
# # Calculate the load time
# load_time = end - start
# print(f"Load Time: {load_time} seconds")
# driver.maximize_window()
# print("Navigated to the website 2.")
# time.sleep(3)

# # Step 4: Enter login 
# driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("psrinivasan")
# driver.find_element(By.ID, 'password').send_keys("Pugal@9629")
# print("Entered username password")
# time.sleep(1)


# login_button_=driver.find_element(By.XPATH,'//*[@id="loginbtn"]')
# login_button_.click()
# time.sleep(6)
# print("login_button")



# driver.refresh()
# time.sleep(20)
# print("2")


# login_button_=driver.find_element(By.XPATH,'//*[@id="67a5fc19cefed67a5fc19c9c1c7_button"]')
# login_button_.click()
# time.sleep(15)
# print("login_button")



# voies_button_=driver.find_element(By.XPATH,'//*[@id="filter_poodll_controlbar_AUTOID"]/div[4]/button[1]')
# voies_button_.click()
# time.sleep(5)
# print("login_button")





# login_button_=driver.find_element(By.XPATH,'//*[@id="filter_poodll_controlbar_AUTOID_fpminimal_audioplayer"]/button')
# login_button_.click()
# time.sleep(10)
# print("login_button")



# login_button_=driver.find_element(By.XPATH,'//*[@id="filter_poodll_controlbar_AUTOID"]/div[4]/div[4]/a/i')
# login_button_.click()
# time.sleep(5)
# print("login_button")



import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def logout():
    try:
        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="signOut"]/span[2]'))
        )
        logout_button.click()
        print("Logged out successfully.")
    except:
        print("Logout button not found!")

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        return command.lower()
    except Exception as e:
        print(f"Error recognizing voice command: {e}")
        return ""

def check_voice_command():
    print("Say 'pause', 'resume', 'logout', or 'stop' anytime...")
    command = listen_command()
    if "pause" in command:
        print("Paused. Say 'resume' to continue...")
        while True:
            resume_cmd = listen_command()
            if "resume" in resume_cmd:
                print("Resuming script...")
                break
    elif "logout" in command:
        print("Voice command: logout triggered!")
        logout()
        driver.quit()
        exit()
    elif "stop" in command:
        print("Voice command: stop received. Closing browser.")
        driver.quit()
        exit()

def main():
    driver = webdriver.Chrome()
    driver.get("https://dmedia1.netlify.app/index.html")
    check_voice_command()

    # Login step
    login_button_submit = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="signupForm"]/div[7]/p/a'))
    )
    login_button_submit.click()
    check_voice_command()

    # Comment step
    driver.find_element(By.XPATH, '/html/body/div/div/textarea').send_keys("Hi there!")
    check_voice_command()

if __name__ == "__main__":
    main()