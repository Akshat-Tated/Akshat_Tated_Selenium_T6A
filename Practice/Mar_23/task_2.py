#task 2
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

o= ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)

driver.get("https://www.nike.in/")
driver.maximize_window()
driver.implicitly_wait(10)

kids = driver.find_element(By.XPATH,'//span[text()="Kids"]/..')
actions = ActionChains(driver)
actions.pause(1).move_to_element(kids).perform()

actions.pause(2).click(kids).perform()

driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.XPATH,'//a[@href="/elevate-their-style/c/94039"]').click()

driver.find_element(By.XPATH,'//div[text()="Nike Air Max Nova"]').click()

driver.switch_to.window(driver.window_handles[2])
driver.find_element(By.XPATH,'//label[text()="UK 6 (EU 40)"]').click()
driver.find_element(By.XPATH,'//button[text()="Add to Bag"]').click()

sleep(5)
driver.quit()