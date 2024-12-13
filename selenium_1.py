import selenium
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://link-upp.netlify.app/")
print("Open Browser")
title = browser.title
print(title)
