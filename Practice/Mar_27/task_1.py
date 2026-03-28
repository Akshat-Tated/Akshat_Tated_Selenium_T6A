# def test_equality():
#     assert 'Hello' != 'hi'
#
# def test_comaprison():
#     assert 2>=1
#
# def test_list():
#     l1 = [1,2,3,4]
#     assert 1 in l1
#     assert 5 not in l1

from time import sleep

from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

o= ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)

driver.get("https://demowebshop.tricentis.com/register")
driver.maximize_window()

driver.implicitly_wait(10)

def test_gender():
    driver.find_element(By.XPATH,'//input[@id="gender-female"]').click()
    driver.find_element(By.XPATH,'//input[@id="gender-male"]').click()

def test_firstname():
    driver.find_element(By.ID, "FirstName").send_keys("Akshat")

def test_secondname():
    driver.find_element(By.ID, "LastName").send_keys("Tated")
def test_email():
    driver.find_element(By.ID, "Email").send_keys("akshat18@gmail.com")
def test_password():
    driver.find_element(By.ID, "Password").send_keys("At@11")
def test_confirmpw():
    driver.find_element(By.ID, "ConfirmPassword").send_keys("At@11")
def test_register_click():
    driver.find_element(By.ID, "register-button").click()