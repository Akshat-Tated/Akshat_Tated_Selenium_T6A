#task_1
from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)
driver.implicitly_wait(10)
actions = ActionChains(driver)

driver.get("https://x.com")
sleep(2)
iframe_ele= driver.find_element(By.XPATH, "//iframe[contains(@src, 'accounts.google.com')]")
driver.switch_to.frame(iframe_ele)
driver.find_element(By.XPATH,"//span[text()='Sign up with Google']").click()
driver.switch_to.window(driver.window_handles[0])
sleep(2)
driver.find_element(By.XPATH,"//span[text()='Create account']").click()

sleep(4)
driver.quit()