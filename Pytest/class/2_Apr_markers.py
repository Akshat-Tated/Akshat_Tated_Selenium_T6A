import pytest

from time import sleep

from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

o= ChromeOptions()
o.add_experimental_option("detach",True)
# driver = Chrome(options=o)

# driver.get("https://www.saucedemo.com/")
# driver.maximize_window()

# driver.implicitly_wait(10)

# @pytest.mark.skip(reason="Feature not ready")
# def test_login():
#     assert True
#
#
# flag = 'bombed'
#
#
# @pytest.mark.skipif(flag == 'bombed', reason="Servers bombed- dont execute")
# def test_logout():
#     assert True

# @pytest.mark.parametrize('a,b',[('standard_user','secret_sauce'),('akshat','tated'),('standard_user','secret_sauce')])
# def test_add(a,b):
#     u1 =driver.find_element(By.XPATH,'//input[@id="user-name"]')
#     u1.send_keys(a)
#     u2 = driver.find_element(By.XPATH,'//input[@id="password"]')
#     u2.send_keys(b)
#     driver.find_element(By.XPATH,'//input[@id="login-button"]').click()
#     assert driver.current_url == 'https://www.saucedemo.com/inventory.html', driver.refresh()
#     driver.back()
#     # print(a+b)


# @pytest.fixture(autouse=True)
# def greet():
#     print('hello')
#     yield
#     print('goodbye')
#
# def test_morning():
#     print('good morning')
#
# def test_evening():
#     print('good evening')


# @pytest.fixture()
# def greet():
#     print('hello')
#     yield
#     print('goodbye')
#
# def test_morning(greet):
#     print('good morning')
#
# def test_evening():
#     print('good evening')

# def test_quit():
#     driver.quit()

@pytest.fixture(scope="class")
def setup():
    driver = Chrome(options=o)
    driver.get("https://demowebshop.tricentis.com/register")
    print('hello')
    yield driver
    print('goodbye')

# def test_morning(greet):
#     print('good morning')
#
# def test_evening():
#     print('good evening')


class TestRegister:
    def test_gender(self, setup):
        driver = setup
        driver.find_element(By.XPATH, '//input[@id="gender-female"]').click()
        driver.find_element(By.XPATH, '//input[@id="gender-male"]').click()


    def test_firstname(self, setup):
        driver = setup
        driver.find_element(By.ID, "FirstName").send_keys("Akshat")


    def test_secondname(self,setup):
        driver = setup
        driver.find_element(By.ID, "LastName").send_keys("Tated")


    def test_email(self,setup):
        driver = setup
        driver.find_element(By.ID, "Email").send_keys("akshat18@gmail.com")


    def test_password(self,setup):
        driver = setup
        driver.find_element(By.ID, "Password").send_keys("At@11")


    def test_confirmpw(self,setup):
        driver = setup
        driver.find_element(By.ID, "ConfirmPassword").send_keys("At@11")


    def test_register_click(self,setup):
        driver = setup
        driver.find_element(By.ID, "register-button").click()
