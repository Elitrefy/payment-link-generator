from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()  # Ensure chromedriver.exe is present
driver.get("http://127.0.0.1:8000")

# Enter order number
order_input = driver.find_element(By.ID, "order_number")
order_input.send_keys("123456")

# Enter CDK
cdk_input = driver.find_element(By.ID, "cdk")
cdk_input.send_keys("ABC123")

# Click the Generate button
generate_btn = driver.find_element(By.ID, "generate_btn")
generate_btn.click()

time.sleep(5)  # Wait for link generation

driver.quit()
