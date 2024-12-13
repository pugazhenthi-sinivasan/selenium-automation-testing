from selenium_1 import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
try:
    driver.get("https://concertcraze.netlify.app/")
    driver.maximize_window()
    time.sleep(2)
    signup_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='signBtn']"))
    )
    signup_button.click()
    print("Sign Up button clicked successfully!")
    driver.find_element(By.ID, "username").send_keys("TestUser")
    driver.find_element(By.ID, "email").send_keys("testuser1565656568@example.com")
    driver.find_element(By.ID, "password").send_keys("Test@1234")
    driver.find_element(By.ID, "confirm-password").send_keys("Test@1234")
    signup_submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    signup_submit_button.click()
    print("Form submitted, waiting for response...")
    WebDriverWait(driver, 10).until(
        EC.url_changes(driver.current_url)
    )
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "searchBox"))
    )
    assert "index.html" in driver.current_url, "Sign Up failed! Didn't navigate to home page."
    print("Sign Up completed successfully and navigated to the Home Page!")
    search_box = driver.find_element(By.ID, "searchBox")
    search_box.send_keys("Anirudh")
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "searchBtn"))
    )
    search_button.click()
    results_container = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "concertCards"))
    )
    results = results_container.text
    if "Anirudh" in results:
        print("Search results contain 'Anirudh'.")
    else:
        print("No results found for 'Anirudh'.")
except Exception as e:
    print(f"Test failed: {e}")
finally:
    driver.quit()