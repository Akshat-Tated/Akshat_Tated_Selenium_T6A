#task_3
from time import sleep

from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o= ChromeOptions()
o.add_experimental_option("detach",True)
o.add_experimental_option("prefs",{"safebrowsing.enabled":True})
o.add_argument("--disable-notifications")
driver = Chrome(options=o)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

driver.implicitly_wait(10)


driver.find_element(By.XPATH,'//button[@onclick="jsAlert()"]').click()
alert1 = driver.switch_to.alert
print(alert1.text)
alert1.accept()

sleep(2)
driver.find_element(By.XPATH,'//button[@onclick="jsConfirm()"]').click()
alert2 = driver.switch_to.alert
print(alert2.text)
alert2.accept()

sleep(3)
driver.find_element(By.XPATH,'//button[@onclick="jsPrompt()"]').click()
alert3 = driver.switch_to.alert
print(alert3.text)
alert3.send_keys("hello")
alert3.accept()

sleep(2)
driver.quit()