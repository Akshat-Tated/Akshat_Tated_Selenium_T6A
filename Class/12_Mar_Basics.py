from time import sleep
#
# from selenium.webdriver import Chrome
# driver = Chrome() #object creation
# sleep(5) #chrome will be displayed for 5 sec


# #for edge
# from selenium.webdriver import Edge
# driver = Edge()

from selenium.webdriver import Chrome,ChromeOptions
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o) #object creation

#from is keyword
# selenium is package
#webdriver is a module
#chrome is a class
# driver is holding the browser
#experimental_option is the browser setting to hold the screen

#step - 2 opening a website url
driver.get("https://www.amazon.in/")
# driver.maximize_window()


# to maximize it
# driver.maximize_window()

# to minimize window
# driver.minimize_window()

# for fullscreen (it removes the upper header of chrome)
# driver.fullscreen_window()

#to fetch the title
#title is the verification properties
title = driver.title
print(title)

#to fetch current url, it is also verification properties
print(driver.current_url)

#to fetch the page source, it is also verification properties
print(driver.page_source)

#to fetch the driver name
print (driver.name)

#only current window closes
# driver.close()

# all tab opened using this is closed
# driver.quit()

#open wikipedia

# back , forward and refresh
sleep(5)
driver.back()
sleep(2)
driver.forward()
sleep(2)
driver.refresh()
