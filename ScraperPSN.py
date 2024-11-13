from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off

# Set path to chromedriver as per your configuration
webdriver_service = Service(ChromeDriverManager().install())

# Choose Chrome Browser
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Open the website
url = 'https://status.playstation.com/'
driver.get(url)

# Wait for the page to load (you may need to use WebDriverWait for certain elements)
driver.implicitly_wait(10)

# Find the element containing the string
element = driver.find_element(By.CLASS_NAME, 'status-text')  # Change 'your_xpath_here' to the actual XPath of the element

# Retrieve the text
text = element.text

print(f"TEST: {text}")
print(driver.title)

# Close the browser
driver.quit()