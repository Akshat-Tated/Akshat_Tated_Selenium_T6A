"""
iframe methods:
1. by index
2. by name
3.by web element
"""

from time import sleep

from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

o= ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)

driver.get("http://127.0.0.1:5500/Web-HTML,CSS_and_JS/task.html")
driver.maximize_window()

driver.implicitly_wait(10)

driver.find_element(By.ID,"inp1").send_keys("hello")
#using name
driver.switch_to.frame("fram1")
driver.find_element(By.ID,"inp2").send_keys("world")
#using index
driver.switch_to.frame(0)
driver.find_element(By.ID,"inp3").send_keys("and hello duniya")
#using ID
# driver.switch_to.frame("frame3")
# driver.find_element(By.ID,"inp4").send_keys("faahaaaa")
#using webelement
# ele = driver.find_element(By.XPATH,'//iframe[@src="page3.html"]')
# driver.switch_to.parent_frame()
driver.switch_to.default_content()
driver.find_element(By.ID,"inp1").clear()
driver.find_element(By.ID,"inp1").send_keys("back to parent ")



sleep(7)
driver.quit()

# from time import sleep
# from selenium.webdriver import Chrome, ChromeOptions
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# o = ChromeOptions()
# o.add_experimental_option('detach', True)
# driver = Chrome(options=o)
# driver.implicitly_wait(10)
# # actions = ActionChains(driver)
#
# driver.get("https://www.zomato.com/chennai/restaurants")
# sleep(2)
#
# driver.find_element(By.XPATH,'//a[text()="Log in"]').click()
#
# sleep(3)
#
# driver.switch_to.frame(0)
# sleep(2)
#
# sleep(2)
# iframe_ele2= driver.find_element(By.XPATH, '(//iframe[@title="Sign in with Google Button"])[1]')
# driver.switch_to.frame(iframe_ele2)
# driver.find_element(By.XPATH,"//span[text()='Sign up with Google']").click()
#
#
# sleep(2)
# driver.find_element(By.XPATH,"//span[text()='Create account']").click()

