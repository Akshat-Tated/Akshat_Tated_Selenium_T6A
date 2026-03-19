#first one
from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.implicitly_wait(10)
driver.get('https://amazon.in')
# wait = WebDriverWait(driver, 10)
# driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys('Watch')
# driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']").click()
# print(driver.find_element(By.XPATH, "(//div[@class='a-row a-size-base a-color-base'])[5]/../../..//div[2]//div//div").text)
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("watch")
driver.find_element(By.ID,"nav-search-submit-button").click()
prod = driver.find_elements(By.CLASS_NAME,"a-size-base-plus.a-spacing-none.a-color-base.a-text-normal")
print(len(prod))
print(prod[4].text)
driver.quit()
