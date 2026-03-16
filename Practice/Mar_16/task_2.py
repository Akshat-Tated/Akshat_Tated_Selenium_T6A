from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

from selenium.webdriver.common.by import By

o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)

driver.get("https://www.flipkart.com/")
driver.maximize_window()

sleep(3)
driver.find_element(By.XPATH,"//span[contains(text(),'✕')]").click()
sleep(3)
driver.find_element(By.NAME,"q").send_keys("Shoes")
sleep(3)
driver.find_element(By.XPATH,"(//button[contains(@class,'XFwMiH')])[1]").click()
sleep(4)
print(driver.find_element(By.XPATH, '//div[contains(@class, "Fo1I0b")]/..//div[@class="hZ3P6w"]').text)
sleep(7)
driver.quit()