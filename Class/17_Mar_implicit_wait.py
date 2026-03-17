# implicit wait (also known as global wait) - here time is not wasted like sleep
# give implicit wait
# if given for 15 sec then each half sec it will check is the element present or not
# it is just find the element
#explicit  - it not just for finding the element, it will also check element is ready for interaction or not,
# here multiple condition we can give
# it is not global

# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# from time import sleep
#
# from selenium.webdriver.support.wait import WebDriverWait
#
# o = ChromeOptions()
# o.add_experimental_option("detach",True)
# driver = Chrome(options=o)
#
# driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
# driver.maximize_window()
#
# driver.find_element(By.TAG_NAME, 'button').click()
#
# driver.explicit_wait = WebDriverWait(driver, 5)
# print(driver.find_element(By.XPATH, '(//h4)[2]').text)
#
# # sleep(10)
# # driver.quit()

##implicit wait

# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# from time import sleep
#
# from selenium.webdriver.support.wait import WebDriverWait
#
# o = ChromeOptions()
# o.add_experimental_option("detach",True)
# driver = Chrome(options=o)
#
# driver.get("https://www.decathlon.in/")
# driver.maximize_window()
#
# driver.implicitly_wait(10)
#
# driver.find_element(By.XPATH, '(//a[contains(@class  ,"-md:w-1/4 bQRXPJ p-0")])[1]').click()
# driver.find_element(By.XPATH,'(//a[contains(@class  ,"-md:w-1/4 bQRXPJ p-0")])[1]').click()
#
# sleep(10)
# driver.quit()


# class task
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

# driver.find_element(By.ID,'exp')
driver.find_element(By.XPATH,"//button[text()='Start']").click()
ele = wait.until(EC.visibility_of_element_located((By.XPATH,"//h4[contains(text(),'Hello')]")))
print(ele.text)
