#task_2
from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)
driver.implicitly_wait(10)

driver.get("https://www.zomato.com/login")
sleep(3)

driver.switch_to.frame(0)
sign_ele=driver.find_element(By.XPATH,"(//iframe[@title='Sign in with Google Button'])[1]")
driver.switch_to.frame(sign_ele)
driver.find_element(By.XPATH,"//span[text()='Sign in with Google']").click()
driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.XPATH,"//span[text()='Create account']").click()


sleep(4)
driver.quit()