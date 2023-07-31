from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json


def running():
    
    opt = Options()
    opt.headless = True
    chrome_driver_path = "./chromedriver"  # Replace this with the actual path
    driver1 = webdriver.Chrome(executable_path=chrome_driver_path, options=opt)
    driver1.set_window_size(800, 600)
    driver1.get("https://aviso.bz/login")
    print("please wait...")
    # load cookies
    with open('./account_1.json', 'r') as f:
        cookies = json.load(f)
    time.sleep(2)
    for cookie in cookies:
        driver1.add_cookie(cookie)
    time.sleep(2)
    driver1.refresh()
    window_before = driver1.window_handles[0]
    driver1.get("https://aviso.bz/work-youtube")
    time.sleep(2)
    coin = WebDriverWait(driver1, 60).until(
    EC.presence_of_element_located((By.ID,"new-money-ballans"))).text
    print(coin)
    time.sleep(2)
    text = WebDriverWait(driver1, 60).until(
    EC.presence_of_element_located((By.XPATH,"/html/body/table/tbody/tr[3]/td[2]/div[2]/table/tbody/tr/td[3]/div/span[1]"))).text
    wait = text[0:2]
    print(wait)
    time.sleep(2)
    WebDriverWait(driver1, 60).until(
    EC.presence_of_element_located((By.XPATH,"/html/body/table/tbody/tr[3]/td[2]/div[2]/table/tbody/tr/td[2]/div[1]/span[1]"))).click()
    time.sleep(3)
    WebDriverWait(driver1, 60).until(
    EC.presence_of_element_located((By.XPATH,"/html/body/table/tbody/tr[3]/td[2]/div[2]/table/tbody/tr/td[2]/div[1]/div/div/span[1]"))).click()
    
    window_after = driver1.window_handles[1]
    driver1.switch_to.window(window_after)
    time.sleep(2)
    driver1.switch_to.frame(WebDriverWait(driver1, 10).until(EC.presence_of_element_located((By.XPATH,'//iframe[starts-with(@src, "https://www.youtube.com/embed")]'))))

    WebDriverWait(driver1, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Play"]'))).click()
    new_wait = int(wait) + 9
    time.sleep(new_wait)
    driver1.quit()



while True:
    try:
      running()
      time.sleep(6)
    except:
        continue
