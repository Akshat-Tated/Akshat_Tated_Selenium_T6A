# Keyboard actions
"""
clicking enter
"""

# from time import sleep
#
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
# o= ChromeOptions()
# o.add_experimental_option("detach",True)
# driver = Chrome(options=o)
#
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
#
# driver.implicitly_wait(10)
# # sleep(4)
# ele = driver.find_element(By.ID,"twotabsearchtextbox")
# ele.send_keys("shoes")
# ele.send_keys(Keys.ENTER)
# sleep(4)
# driver.quit()


"""
Copying and pasting
"""

# from time import sleep
#
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
# o= ChromeOptions()
# o.add_experimental_option("detach",True)
# driver = Chrome(options=o)
#
# driver.get("https://demoqa.com/text-box")
# driver.maximize_window()
#
# driver.implicitly_wait(10)
# # sleep(4)
# ele = driver.find_element(By.ID,"currentAddress")
# ele.send_keys("Tated Parisar")
# ele.send_keys(Keys.CONTROL + 'a')
# ele.send_keys(Keys.CONTROL + 'c')
# ele2 = driver.find_element(By.ID,"permanentAddress")
# ele2.send_keys(Keys.CONTROL + 'v')
# sleep(4)
# driver.quit()
"""
#actionchains Class
# 1. Create Object
# 2. Store Action
# 3. Perform
"""

# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
# o= ChromeOptions()
# o.add_experimental_option("detach",True)
# driver = Chrome(options=o)
#
# driver.get("https://demoqa.com/buttons")
# driver.maximize_window()
#
# driver.implicitly_wait(10)
# # sleep(4)
# # ele = driver.find_element(By.XPATH,'//button[text() ="Click Me"]')
# actions = ActionChains(driver)
# # actions.click(ele).perform()
#
# dble_ele = driver.find_element(By.XPATH,'//button[text() ="Double Click Me"]')
# actions.double_click(dble_ele).perform()
#
# right_ele = driver.find_element(By.XPATH,'//button[text()="Right Click Me"]')
# actions.context_click(right_ele).perform()
#
# ele = driver.find_element(By.XPATH,'//button[text() ="Click Me"]')
# actions.click(ele).perform()
# # ele.click()
# # ele.send_keys(Keys.ENTER)
# # ele.click()
# # ele.send_keys(Keys.CONTROL + 'a')
# # ele.send_keys(Keys.CONTROL + 'c')
# # ele2 = driver.find_element(By.ID,"permanentAddress")
# # ele2.send_keys(Keys.CONTROL + 'v')
# sleep(8)
# # driver.quit()

"""
# scrolling 
"""

from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

o= ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)

driver.get("https://www.amazon.in/")
driver.maximize_window()

driver.implicitly_wait(10)
# sleep(4)
# ele = driver.find_element(By.ID,"currentAddress")
# ele.send_keys("Tated Parisar")
# ele.send_keys(Keys.CONTROL + 'a')
# ele.send_keys(Keys.CONTROL + 'c')
# ele2 = driver.find_element(By.ID,"permanentAddress")
# ele2.send_keys(Keys.CONTROL + 'v')
# sleep(4)
driver.quit()