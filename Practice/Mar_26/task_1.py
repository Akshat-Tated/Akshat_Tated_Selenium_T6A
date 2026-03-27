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

driver.get("https://in.pinterest.com/")

folder = os.path.join(os.getcwd(),'screenshot')
os.makedirs(folder, exist_ok=True)
time_stamp = time.strftime("%Y%m%d-%H%M%S")
driver.save_screenshot(f'{folder}/entire_page.png{time_stamp}.png')

sleep(2)
ele = driver.find_element(By.XPATH,'//*[@id="mweb-unauth-container"]/div/div/div/div[4]/div[2]/div/div/div/div[2]/div/div/img')
action = ActionChains(driver)
action.move_to_element(ele).pause(2).perform()
ele.screenshot(f'{folder}/Pinterest2_{time_stamp}.png')
sleep(4)
driver.quit()