from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service("/path/to/chromedriver")  # Update with the correct path
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://payment-link-generator-frontend.onrender.com")

    # Wait for elements
    order_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "order_number")))
    order_input.send_keys("123456")

    cdk_input = driver.find_element(By.ID, "cdk")
    cdk_input.send_keys("ABC123")

    generate_btn = driver.find_element(By.ID, "generate_btn")
    generate_btn.click()

    # Wait for response
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "payment_link")))

    print("Test Passed: Payment link generated successfully!")

except Exception as e:
    print(f"Test Failed: {e}")

finally:
    driver.quit()