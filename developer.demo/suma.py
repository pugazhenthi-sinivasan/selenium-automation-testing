import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch browser and navigate to site
driver = webdriver.Chrome()
# Record the start time
start = time.time()
driver.get("https://dmedia1.netlify.app/index.html")

end = time.time()
# Calculate the load time
load_time = end - start
print(f"Load Time: {load_time} seconds")

driver.maximize_window()
print("Browser launched and website loaded.")

# Define actions as reusable functions
def click_element(xpath, wait_time=10):
    """Click an element by XPath."""
    WebDriverWait(driver, wait_time).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    ).click()

# def enter_text(xpath, text, wait_time=10):
#     """Enter text into a field located by XPath."""
#     WebDriverWait(driver, wait_time).until(
#         EC.presence_of_element_located((By.XPATH, xpath))
#     ).send_keys(text)

# # Define a list of actions
# actions = [
#     {"action": "click", "xpath": '//*[@id="signupForm"]/div[7]/p/a', "description": "Login button clicked."},
#     {"action": "enter", "xpath": '//*[@id="email"]', "value": "pugalpugazh@gmail.com", "description": "Email entered."},
#     {"action": "enter", "xpath": '//*[@id="password"]', "value": "Pugal@1234", "description": "Password entered."},
#     {"action": "click", "xpath": '//*[@id="submitSignIn"]', "description": "Login submitted."},
#     {"action": "click", "xpath": '//*[@id="postContainer"]/div[1]/div[1]/span[1]', "description": "Like button clicked."},
#     {"action": "click", "xpath": '//*[@id="postContainer"]/div[1]/div[1]/span[3]', "description": "Comment button clicked."},
#     {"action": "enter", "xpath": '//textarea[@class="comment-input"]', "value": "Hi", "description": "Comment entered."},
#     {"action": "click", "xpath": '//button[@class="submit-comment-button"]', "description": "Comment submitted."},
#     {"action": "click", "xpath": '/html/body/aside/nav/ul[1]/li[2]/a/span[2]', "description": "Navigated to Discover page."},
#     {"action": "enter", "xpath": '//*[@id="search-bar"]', "value": "#back", "description": "Search for hashtag #back."},
#     {"action": "click", "xpath": '//*[@id="results-container"]/div/div/img', "description": "Image clicked in search results."},
# ]

# # Loop through actions and execute them
# for action in actions:
#     try:
#         if action["action"] == "click":
#             click_element(action["xpath"])
#         elif action["action"] == "enter":
#             enter_text(action["xpath"], action["value"])
#         print(action["description"])
#         time.sleep(2)  # Optional: Add delay for visual tracking
#     except Exception as e:
#         print(f"Error during action '{action['description']}': {e}")

# # Close browser
# driver.quit()
# print("Browser closed.")



