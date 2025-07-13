from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://cosmocode.io/automation-practice-webtable/")
driver.execute_script("window.scrollTo(0, 700)")
time.sleep(1)

target_column_name = "Country"
target_value = "Australia"
found = False

# Step 1: Get headers (note: they're in the FIRST row, using <td> instead of <th>)
header_row = driver.find_element(By.XPATH, "//table[@id='countries']//tr[1]")
header_cells = header_row.find_elements(By.TAG_NAME, "td")
target_col_index = -1

for i, cell in enumerate(header_cells):
    if cell.text.strip().lower() == target_column_name.lower():
        target_col_index = i + 1  # XPath is 1-based
        break

if target_col_index == -1:
    print("❌ Target column not found.")
    driver.quit()
    exit()

# Step 2: Get all rows (excluding header)
rows = driver.find_elements(By.XPATH, "//table[@id='countries']//tr[position()>1]")
print(f"📊 Total number of data rows: {len(rows)}")

# Step 3: Check each row’s Country column for the target value
for row in rows:
    try:
        cell = row.find_element(By.XPATH, f"./td[{target_col_index}]")
        if cell.text.strip() == target_value:
            print(f"✅ Found '{target_value}' under column '{target_column_name}'")
            found = True
            break
    except:
        continue

if not found:
    print(f"❌ '{target_value}' not found in column '{target_column_name}'")

driver.quit()
