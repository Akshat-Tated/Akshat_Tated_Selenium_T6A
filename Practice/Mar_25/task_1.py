import os
import time
from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)
driver.implicitly_wait(10)

driver.get("https://www.saucedemo.com/")

driver.find_element(By.XPATH,'//input[@name="user-name"]').send_keys("standard_user")
driver.find_element(By.XPATH,'//input[@name="password"]').send_keys("standard_user")
driver.find_element(By.XPATH,'//input[@name="login-button"]').click()

folder = os.path.join(os.getcwd(),'screenshot')
os.makedirs(folder, exist_ok=True)

expected = 'https://www.saucedemo.com/inventory.html'
actual = driver.current_url
assert expected == actual , driver.save_screenshot(f'{folder}/screenshot_page.png')

sleep(4)
driver.quit()