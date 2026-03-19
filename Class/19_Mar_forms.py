# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
#
# o = ChromeOptions()
# o.add_experimental_option("detach",True)
# driver = Chrome(options=o)
#
# driver.get("https://www.google.com")
# driver.maximize_window()
# driver.implicitly_wait(15)
#
# # driver.find_element(By.TAG_NAME,"a").click()
# links = driver.find_elements(By.TAG_NAME,"a")
# # print(links)
# print(len(links))
# for l in links:
#     print(l.text)
#
# driver.quit()
from time import sleep

#task 1
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
#
# o = ChromeOptions()
# o.add_experimental_option("detach",True)
# driver = Chrome(options=o)
#
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# driver.implicitly_wait(15)
#
# driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Shoes")
# driver.find_element(By.ID,"nav-search-submit-button").click()
#
# list = driver.find_elements(By.XPATH,'//div[@ID="nav-main"]//a')
# for link in list:
#     if link.text !='':
#         print(link.text," : ",link.get_attribute("href"))
# print(list.get_attribute("aria-label"))
# print(len(list))


# driver.find_element(By.TAG_NAME,"a").click()
# links = driver.find_elements(By.TAG_NAME,"a")
# print(links)
# print(len(links))
# for l in links:
#     print(l.text)

# driver.quit()


# Interacting with forms
# is_displayed()
# is_enabled()
# is_selected()

# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
#
# o = ChromeOptions()
# o.add_experimental_option("detach",True)
# driver = Chrome(options=o)
#
# driver.get("https://www.facebook.com")
# driver.maximize_window()
# driver.implicitly_wait(15)
# # sleep(2)
# # ty = driver.find_element(By.XPATH,'//div[@aria-label="Log in"]')
# # ele.click()
# # print(ty.is_displayed())
#
# btn = driver.find_element(By.XPATH,'//input[@type="submit"]')
# print(btn.is_enabled())
# print(btn.is_displayed())
#
# # driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Shoes")
#
# driver.quit()


# checkbox
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
#
# o = ChromeOptions()
# o.add_experimental_option("detach",True)
# driver = Chrome(options=o)
#
# driver.get("https://the-internet.herokuapp.com/checkboxes")
# driver.maximize_window()
# driver.implicitly_wait(15)
#
# btn1 = driver.find_element(By.XPATH,'(//input[@type="checkbox"])[1]')
# print(btn1.is_selected())
#
# btn2 = driver.find_element(By.XPATH,'(//input[@type="checkbox"])[2]')
# print(btn2.is_selected())
#
# # driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Shoes")
#
# driver.quit()

#fill form task

from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)

driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
driver.implicitly_wait(15)

driver.find_element(By.ID,"firstName").send_keys("Akshat")
driver.find_element(By.ID,"lastName").send_keys("Tated")
driver.find_element(By.ID,"userEmail").send_keys("akshat@gmail.com")
driver.find_element(By.ID,"userNumber").send_keys("7441176670")
driver.find_element(By.XPATH,'//input[@value="19 Mar 2026"]').click()
driver.find_element(By.XPATH,'//div[contains(text(),10)]').click()
# driver.find_element(By.ID,"subjectsInput").send_keys("Math")
driver.find_element(By.ID,"hobbies-checkbox-1").click()
driver.find_element(By.ID,"hobbies-checkbox-3").click()

sleep(5)
driver.find_element(By.ID,"submit").click()

driver.quit()
