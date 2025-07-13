from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

first_checkbox = driver.find_element(By.CSS_SELECTOR, "label[for='sunday']")
driver.execute_script("arguments[0].scrollIntoView();", first_checkbox)
time.sleep(1)

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for i, checkbox in enumerate(checkboxes[:7]):
    checkbox.click()
    if checkbox.is_selected():
        print(f"✅ Checkbox {i+1} selected successfully.")
    else:
        print(f"❌ Checkbox {i+1} FAILED to select.")

expected_checkbox_count = 7
checkbox_count = 0

for checkbox in checkboxes[:7]:
    if checkbox.is_selected():
        checkbox_count += 1

if checkbox_count == expected_checkbox_count:
    print("PASSED 🟢")

driver.quit()

