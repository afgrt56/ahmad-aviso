from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Automatically download and set up ChromeDriver
import chromedriver_autoinstaller

# Headless options for Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--no-sandbox")  # Required in certain environments

# Initialize ChromeDriver
chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=chrome_options)

# Example: Navigate to a website
driver.get("https://www.google.com")

# Your Selenium code goes here...

# Close the browser
driver.quit()
print("done")
