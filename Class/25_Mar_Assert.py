# import os
# import time
# from time import sleep
# from selenium.webdriver import Chrome, ChromeOptions
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# o = ChromeOptions()
# o.add_experimental_option('detach', True)
# driver = Chrome(options=o)
# driver.implicitly_wait(10)
# # actions = ActionChains(driver)
#
# driver.get("https://google.com")
#
# # driver.find_element(By.XPATH,'//a[@href="/gp/bestsellers/?ref_=nav_cs_bestsellers"]').click()
# # expected = 'Amazon.in Bestsellers: The most popular items on Amazon'
# # actual = driver.title
# # assert expected == actual , 'title mismatch'
# # folder = os.path.join(os.getcwd(),'screenshot')
# # os.makedirs(folder, exist_ok=True)
# # driver.save_screenshot(f'{folder}/screenshot_page.png')
# #
# # ## element screenshot
# # ele = driver.find_element(By.XPATH,'//textarea[@title="Search"]')
# # ele.screenshot(f'{folder}/search.png')
#
# # with time stamp
# folder = os.path.join(os.getcwd(),'screenshot')
# os.makedirs(folder, exist_ok=True)
#
#
# ele = driver.find_element(By.XPATH,'//textarea[@title="Search"]')
# time_stamp = time.strftime("%Y%m%d-%H%M%S")
# ele.screenshot(f'{folder}/search_{time_stamp}.png')
# # folder = os.path.join(os.getcwd(),'screenshot')
# # os.makedirs(folder, exist_ok=True)
# # driver.save_screenshot(f'{folder}/screenshot_page.png')
#
# ## element screenshot
# sleep(4)
# driver.quit()


import os
import time
from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)
driver.implicitly_wait(10)
# actions = ActionChains(driver)

driver.get("https://www.saucedemo.com/")

driver.find_element(By.XPATH,'//input[@name="user-name"]').send_keys("standard_user")
driver.find_element(By.XPATH,'//input[@name="password"]').send_keys("standard_user")
driver.find_element(By.XPATH,'//input[@name="login-button"]').click()

folder = os.path.join(os.getcwd(),'screenshot')
os.makedirs(folder, exist_ok=True)

expected = 'https://www.saucedemo.com/inventory.html'
actual = driver.current_url
assert expected == actual , driver.save_screenshot(f'{folder}/screenshot_page.png')
# folder = os.path.join(os.getcwd(),'screenshot')
# os.makedirs(folder, exist_ok=True)
# driver.save_screenshot(f'{folder}/screenshot_page.png')
#
# ## element screenshot
# ele = driver.find_element(By.XPATH,'//textarea[@title="Search"]')
# ele.screenshot(f'{folder}/search.png')

# with time stamp
# folder = os.path.join(os.getcwd(),'screenshot')
# os.makedirs(folder, exist_ok=True)
#
#
# ele = driver.find_element(By.XPATH,'//textarea[@title="Search"]')
# time_stamp = time.strftime("%Y%m%d-%H%M%S")
# ele.screenshot(f'{folder}/search_{time_stamp}.png')
# folder = os.path.join(os.getcwd(),'screenshot')
# os.makedirs(folder, exist_ok=True)
# driver.save_screenshot(f'{folder}/screenshot_page.png')

## element screenshot
sleep(4)
driver.quit()