"""
there are two method to find the elements:
                1. find_element(locator_name,locator_value) ->
                                ->it takes two arguments, this is for single elements
                                -> this return one single web element
                                -> for error "No such element exception"

                2. find_elements(locator_name,locator_value) ->
                                -> it also take two arguments, this is for multiple elements
                                -> it returns list of web elements
                                -> for error "Empty list"

locators  - address of an element
types of locators ->
1. ID
2. NAME
3. CLASSNAME
4. TAG NAME
5. LINK TEXT
6. PARTIAL LINK TEXT
7. CSS SELECTOR
8. X PATH

1-4 -> direct locator
5-6 -> text based
7-8 -> expression based

element actions
1. click()
2. send_keys()
"""

from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)

driver.get("https://www.amazon.in/")

sleep(3)

#######################################################################################
## ID


# driver.find_element(By.ID,"twotabsearchtextbox").send_keys("shoes")
# sleep(2)
# driver.find_element(By.ID,"nav-search-submit-button").click()


# driver.get("https://demoqa.com/text-box")
# driver.maximize_window()
#
# # driver.find_element(By.ID,"userName").send_keys("Akshat")
#
# username = driver.find_element(By.ID,"userName")
# username.send_keys("Akshat")
#
# useremail = driver.find_element(By.ID,"userEmail")
# useremail.send_keys("akshattated18@gmail.com")
#
# curraddress = driver.find_element(By.ID,"currentAddress")
# curraddress.send_keys("jaipur")
#
# peraddress = driver.find_element(By.ID,"permanentAddress")
# peraddress.send_keys("ratlam")
#
# sleep(2)
# driver.find_element(By.ID,"submit").click()



############################################################################
## NAME
# driver.find_element(By.NAME,"field-keywords").send_keys("shoes")

############################################################################
## CLASS_NAME
#for compound classname use '.' in spaces
# it is fcfs
# driver.find_element(By.CLASS_NAME,"nav-progressive-attribute.nav-input").send_keys("shoes")

############################################################################
## TAG name
# it is also fcfs
# driver.find_element(By.TAG_NAME,"input").send_keys("akshat@gmail.com")


###############################################################################
##linktext
# it is case-sensitive and also space sensitive
# driver.find_element(By.LINK_TEXT,"Mobiles").click()


###############################################################################
## partial text
# it is case-sensitive and also space sensitive
# driver.find_element(By.PARTIAL_LINK_TEXT,"Mob").click()


driver.find_element(By.CSS_SELECTOR,'input[placeholder="Search Amazon.in"]').send_keys("hello")





sleep(15)
driver.quit()