import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.selenium.dev/")
time.sleep(2)
browser.switch_to.new_window()
browser.get("https://playwright.dev/")
time.sleep(2)
num_tabs = len(browser.window_handles)
print(num_tabs)
tab_value = browser.window_handles
print(tab_value)
current_tab = browser.current_window_handle
print(current_tab)
browser.find_element(By.CSS_SELECTOR, ".getStarted_Sjon").click()
time.sleep(2)
first_tab = browser.window_handles[0]
if first_tab != current_tab:
    browser.switch_to.window(first_tab)
browser.find_element(By.XPATH, "//span[normalize-space()='Downloads']").click()
time.sleep(1)
element = browser.find_element(By.XPATH, "//a[@href='https://seleniumhq.github.io/selenium/docs/api/java/index.html']")
browser.execute_script("arguments[0].scrollIntoView(true);", element)
time.sleep(1)



