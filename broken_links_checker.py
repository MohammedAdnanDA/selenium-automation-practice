import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/")
driver.maximize_window()

all_links = driver.find_elements(By.TAG_NAME, "a")
print(f"Total links: {len(all_links)}")

broken_links = 0
for link in all_links:
    href = link.get_attribute("href")
    responses = requests.get(href)
    if responses.status_code >= 400:
        broken_links += 1
        print(f"Broken Link {href}, Status Code : {responses.status_code} ")

print(f"Total broken links: {broken_links}")

driver.quit()
