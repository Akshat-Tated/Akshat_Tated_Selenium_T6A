from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

options = ChromeOptions()
options.add_experimental_option('detach', True)

driver = Chrome(options=options)
driver.implicitly_wait(20)
driver.maximize_window()

driver.get('https://demowebshop.tricentis.com/')

fb_link = driver.find_element(By.XPATH, "//a[.='Facebook']")
actions = ActionChains(driver)
actions.scroll_to_element(fb_link).pause(2).click(fb_link).perform()

sleep(5)
driver.switch_to.window(driver.window_handles[-1])

email_input = driver.find_element(By.XPATH, "(//input[@name='email'])[2]")
password_input = driver.find_element(By.XPATH, "(//input[@type='password'])[2]")
login_btn = driver.find_element(By.XPATH, "(//span[.='Log in'])[5]")

email_input.send_keys("akshat@gmail.com")
password_input.send_keys("techyat123")
login_btn.click()

sleep(2)
driver.quit()