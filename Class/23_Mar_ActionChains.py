from time import sleep

from selenium.webdriver.common.by import By

# from selenium.webdriver import Chrome, ChromeOptions
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
# from selenium.webdriver.common.by import By
#
# o = ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)
#
# driver.maximize_window()

'''driver.get("https://demoqa.com/buttons")

driver.implicitly_wait(10)
actions = ActionChains(driver)

doubleClick = driver.find_element(By.XPATH, '//button[@id="doubleClickBtn"]')
actions.double_click(doubleClick).perform()

rightClick = driver.find_element(By.XPATH, '//button[@id="rightClickBtn"]')
actions.context_click(rightClick).perform()

singleClick = driver.find_element(By.XPATH, '//button[.="Click Me"]')
actions.click(singleClick).perform()'''


# Scroll to the element function in action chain
# driver.get("https://www.google.com")
#
# driver.implicitly_wait(100)
# actions = ActionChains(driver)

# foot1 = driver.find_element(By.XPATH, '//a[@href="https://www.facebook.com/AmazonIN"]')
# actions.scroll_to_element(foot1).pause(2).click(foot1).perform()

# actions.scroll_by_amount(0,400).perform()
# actions.scroll_by_amount(0,-400).perform()


# input1 = driver.find_element(By.ID,"twotabsearchtextbox")
# origin = ScrollOrigin.from_element(input1)
# actions.scroll_from_origin(origin,0, 400).perform()

# move1 = driver.find_element(By.XPATH,'//div[@ID="nav-link-accountList"]')
# actions.pause(2).move_to_element(move1).perform()
# driver.find_element(By.XPATH,'//span[@class="ng-tns-c2785778308-3 icon-cancel"]').click()
# sleep(3)
# driver.find_element(By.XPATH, '//input[@ID="password"]').send_keys("hello")
# hold1 = driver.find_element(By.XPATH,'//button//img[@src="assets/img/Revamp/icon_eye_close.svg"]')
# actions.click_and_hold(hold1).pause(3).release().perform()

#drag and drop
# drag1 = driver.find_element(By.XPATH,'//div[@ID="draggable"]')
# drop1 = driver.find_element(By.XPATH,'//div[@ID="droppable"]')
# actions.pause(2).drag_and_drop(drag1,drop1).perform()

#switch to window
# 1) current_window_handle
# 2) window_handles
# 3) switch_to_window()

from selenium.webdriver import Chrome,ChromeOptions
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o) #object creation

driver.get("https://www.google.com")
sleep(5)
#manually open three tabs

print(driver.current_window_handle)
# googleURL = driver.current_window_handle
print(driver.title)

driver.switch_to.new_window()
driver.get("https://amazon.in/")
sleep(5)
print(driver.current_window_handle)
print(driver.title)
print(driver.current_window_handle)
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[0])
sleep(2)
driver.find_element(By.XPATH,'//textarea[@name="q"]').send_keys("hello")
sleep(2)
driver.quit()