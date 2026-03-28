# / parent syntax
# /child element/parent::parent tag
from time import sleep

from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

o= ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.implicitly_wait(10)

driver.find_element(By.XPATH,'//input[@id="name"]/parent::div')

sleep(5)
driver.quit()