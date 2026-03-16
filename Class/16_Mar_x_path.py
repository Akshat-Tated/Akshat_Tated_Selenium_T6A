## xPAth
#Traversing -> Forward -> through the parent accessing child ( / or // )
#           -> Backward -> from child fetching parent element ( /.. )

'''3 steps
i. identify the static element
ii. from static move to common parent
iii. from common parent fetch the dynamic elements
ex - //td[text()='Cierra']/..//td[5]

siblings -> following sibling -> below ones are following sibling
         -> preceding sibling -> above ones are preceding sibling
ex - //td[text()="Frank"]/following-sibling::td[2]
ex - //td[text()="Frank"]/preceding-sibling::td[2]

'''
#task1
# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep
#
# from selenium.webdriver.common.by import By
#
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# o.add_argument('--headless')
# driver = Chrome(options=o)
#
# driver.get("https://demoqa.com/webtables")
# driver.maximize_window()
#
# print(driver.find_element(By.XPATH,"//td[text()='Cierra']/..//td[5]").text)
# sleep(7)
# driver.quit()

#task -2
# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep
#
# from selenium.webdriver.common.by import By
#
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# o.add_argument('--headless')
# driver = Chrome(options=o)
#
# driver.get("https://the-internet.herokuapp.com/tables")
# driver.maximize_window()
#
# print(driver.find_element(By.XPATH,"//td[text()='Frank']/..//td[4]").text)
# sleep(7)
# driver.quit()

#task-3
# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep
#
# from selenium.webdriver.common.by import By
#
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# o.add_argument('--headless')
# driver = Chrome(options=o)
#
# driver.get("https://the-internet.herokuapp.com/tables")
# driver.maximize_window()
#
# print(driver.find_element(By.XPATH,"//td[text()='Frank']/following-sibling::td[2]").text)
# sleep(7)
# driver.quit()


#task - 4 (i)

# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep
#
# from selenium.webdriver.common.by import By
#
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# driver = Chrome(options=o)
#
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
#
# sleep(2)
# driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Mobiles")
#
# sleep(2)
# driver.find_element(By.ID,"nav-search-submit-button").click()
# sleep(3)
#
# # v = driver.find_element(By.XPATH,"(//h2[contains( . ,'iQOO Neo')]/../..//following-sibling::div[2]//div//div//div//div//div//a//span//span)[1]")
# sleep(4)
# v = driver.find_element(By.XPATH,"(//span[contains(text(),'Samsung Galaxy M07 Mobile (Black, 4GB RAM, 64GB Storage) |')]/../../../..//span)[9]").text
# # print(driver.find_element(By.XPATH,"(//h2[contains( . ,'iQOO Neo')]/../..//following-sibling::div[2]//div//div//div//div//div//a//span//span)[1]").text)
# print(v)
# sleep(4)
# driver.quit()


#task - 5

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




