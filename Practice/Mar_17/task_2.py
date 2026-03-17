from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.implicitly_wait(10)
driver.get('https://demoqa.com/webtables')
driver.maximize_window()
wait = WebDriverWait(driver,100)


f_name = wait.until(EC.visibility_of_element_located((By.XPATH, "(//tr)[5]//td[1]"))).text
salary = wait.until(EC.visibility_of_element_located((By.XPATH, "(//tr)[5]//td[1]/..//td[5]"))).text

print(f"{f_name} salary is {salary}")


driver.quit()

