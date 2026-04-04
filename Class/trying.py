# from time import sleep
#
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
# o= ChromeOptions()
# o.add_experimental_option("detach",True)
# driver = Chrome(options=o)
#
# driver.get("https://www.flipkart.com/")
# driver.maximize_window()
#
# # driver.implicitly_wait(10)
# wait = WebDriverWait(driver,20)
#
# ele = wait.until(EC.visibility_of_element_located((By.XPATH,'(//div[contains(. , "Become a Seller")])[35]')))
# ele.click()
#
# sleep(3)
# driver.quit()

from time import sleep

from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

o= ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)

driver.get("https://demowebshop.tricentis.com/apparel-shoes")
driver.maximize_window()

dropdpwn = driver.find_element(By.XPATH,'//select[@id="products-orderby"]')
opt = Select(dropdpwn)
opt.select_by_index(3)

sleep(2)
driver.quit()

# driver.implicitly_wait(10)
