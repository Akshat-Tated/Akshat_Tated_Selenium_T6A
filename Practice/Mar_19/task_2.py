from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)

driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(15)

driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Shoes")
driver.find_element(By.ID,"nav-search-submit-button").click()

list = driver.find_elements(By.XPATH,'//div[@ID="nav-main"]//a')
for link in list:
    if link.text !='':
        print(link.text," : ",link.get_attribute("href"))
print(len(list))

driver.quit()







