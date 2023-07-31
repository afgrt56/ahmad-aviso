from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # To run Chrome in headless mode
options.add_argument('--no-sandbox')  # Required when running as root user in Cloud Shell

driver = webdriver.Chrome(options=options)
driver.get('https://www.google.com')
print("wait")
# Your Selenium interactions here...

driver.quit()
