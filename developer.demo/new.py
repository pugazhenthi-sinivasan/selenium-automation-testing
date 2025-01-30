import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
actions=ActionChains()
driver = webdriver.Chrome()
# Step 2: Navigate to the site and maximize the window
driver.get("https://www.automationexercise.com/")
driver.maximize_window()
print("Navigated to the website 2.")
time.sleep(2)
# Step 3: Click on login button
# login_button_submit = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, 'sign-in-btn'))
# )
# login_button_submit.click()
# print("Login button clicked successfully 3.")
# time.sleep(10)

# hover = driver.find_elements(By.XPATH,'//div[3]//div[1]//div[1]//div[2]')
# actions.move_to_element(hover).perform
# add_cart = driver.find_elements(By.XPATH,'//div[6]//div[1]//div[1]//div[2]//div[1]//a[1]')
# hover = driver.find_elements(By.XPATH,'//*[@id="cartModal"]/div/div/div[3]/button')
# for buton in add_cart:
#     buton.click()
#     print("in ok")
#     time.sleep(2)
try:
    # Step 1: Hover over an element
    hover_element = driver.find_element(By.XPATH, '//div[3]//div[1]//div[1]//div[2]')
    actions = ActionChains(driver)
    actions.move_to_element(hover_element).perform()
    print("Hover action performed.")

    # Step 2: Find 'Add to Cart' buttons
    add_cart_buttons = driver.find_elements(By.XPATH, '//div[6]//div[1]//div[1]//div[2]//div[1]//a[1]')

    # Step 3: Click each 'Add to Cart' button
    for button in add_cart_buttons:
        button.click()
        print("Button clicked.")
        time.sleep(2)  # Wait to observe the click action

    # Step 4: Close the cart modal (if necessary)
    close_button = driver.find_element(By.XPATH, '//*[@id="cartModal"]/div/div/div[3]/button')
    close_button.click()
    print("Cart modal closed.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the driver
    driver.quit()


    
# driver.execute_script("window.scrollTo(0, 1000)")
# time.sleep(5)
