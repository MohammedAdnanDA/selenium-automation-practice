import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v136.dom import get_attributes

browser = webdriver.Chrome()
url = "https://the-internet.herokuapp.com/broken_images"
browser.get(url)
browser.maximize_window()

broken_images = []

images = browser.find_elements(By.TAG_NAME, "img")
Total_broken_images = 0
for image in images:
    src = image.get_attribute("src")
    if src:
        response = requests.get(src)
        if response.status_code != 200:
            broken_images.append(src)
            Total_broken_images += 1
print("Broken Images Found!📕")
print(f"Total broken images: {Total_broken_images}")

for broken_image in broken_images:
    print(broken_image)

