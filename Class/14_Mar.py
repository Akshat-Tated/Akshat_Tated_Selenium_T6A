## x-path
# -> we can traverse backward and forward
# -> Locate elements based on text
# -> Locate elements based on attribute
# -> used for dynamic elements

#x-path types - absolute - start with '/' and from root node
#             - relative
from time import sleep


# from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By

# o = ChromeOptions()
# o.add_experimental_option("detach",True)
# driver = Chrome(options=o)
#
# driver.get("https://demoqa.com/text-box")
# driver.maximize_window()

#another syntax of css selector -> "#" for ID and "." for CLASSNAME
# driver.find_element(By.CSS_SELECTOR,"input#userName").send_keys("hello")

#finding element by attribute
# driver.find_element(By.XPATH,'//input[@placeholder="Full Name"]').send_keys("Akshat_Tated")
# sleep(2)

#finding element by text box
# driver.find_element(By.XPATH,'//button[text()="Submit"]').click()

# we can also use dot and also it can also locate inside div
# driver.find_element(By.XPATH,'//button[. ="Submit"]').click()
#
# sleep(4)
# driver.quit()


from time import sleep


from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)

driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)

#X-path using contains attribute
# //tagname[contains(@attribute,'value')]
# driver.find_element(By.XPATH,'//a[contains(@href,"https://accelerator")]').click()


#X-path using contains text
#//tagname[contains(text(),'value')]
#//tagname[contains(. ,'value')]
driver.find_element(By.XPATH,'//a[contains(text(),"Accelerator")]').click()