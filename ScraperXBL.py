from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off

# Set path to chromedriver as per your configuration
webdriver_service = Service(ChromeDriverManager().install())

# Choose Chrome Browser
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Open the website
url = 'https://support.xbox.com/en-US/xbox-live-status'
driver.get(url)

# Wait for the page to load and the specific element to become available
try:
    # Wait for the main container to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'ms-List'))
    )

    # Find elements with the class 'undefined root-148'
    status_elements = driver.find_elements(By.CLASS_NAME, 'undefined')

    # Filter elements by additional class and print the text of the target element
    for element in status_elements:
        classes = element.get_attribute('class')
        if 'root-148' in classes:
            print(element.text)
            break
except Exception as e:
    print(f"An error occurred: {e}")

# Close the browser
driver.quit()