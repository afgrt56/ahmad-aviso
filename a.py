from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # To run Chrome in headless mode (without GUI)
options.add_argument('--no-sandbox')  # Required for running as a superuser
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=options)

driver.get('https://www.google.com')
search_box = driver.find_element_by_name('q')
search_box.send_keys('Hello, Google!')
search_box.submit()

driver.save_screenshot('screenshot.png')  # Take a screenshot to verify

driver.quit()
