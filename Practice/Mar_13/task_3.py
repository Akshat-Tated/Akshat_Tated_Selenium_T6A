from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://www.amazon.in/")
driver.maximize_window()

sleep(2)
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Mobiles")

sleep(2)
driver.find_element(By.ID,"nav-search-submit-button").click()
sleep(2)

driver.find_element(By.PARTIAL_LINK_TEXT,"Samsung").click()


