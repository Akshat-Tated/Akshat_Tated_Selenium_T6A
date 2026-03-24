#task_4
from time import sleep

from selenium.webdriver import Chrome,ChromeOptions


o= ChromeOptions()
o.add_experimental_option("detach",True)
o.add_experimental_option("prefs",{"safebrowsing.enabled":True})
o.add_argument("--disable-notifications")
driver = Chrome(options=o)

driver.get("https://demoqa.com/")
driver.maximize_window()

driver.implicitly_wait(10)
first_window = driver.current_window_handle
print(first_window)
print(driver.title)
print(driver.current_url)

driver.switch_to.new_window()
driver.get("https://www.google.com")
print(driver.current_window_handle)
print(driver.title)
print(driver.current_url)

driver.switch_to.new_window()
driver.get("https://the-internet.herokuapp.com/")
print(driver.current_window_handle)
print(driver.title)
print(driver.current_url)

all_windows = driver.window_handles
for i in all_windows:
    driver.switch_to.window(i)
    if i != first_window:
        driver.close()

sleep(5)
driver.quit()
