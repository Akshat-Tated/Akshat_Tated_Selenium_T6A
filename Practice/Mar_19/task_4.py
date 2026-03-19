from time import sleep

from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

driver.maximize_window()
driver.implicitly_wait(15)

driver.get('https://testautomationpractice.blogspot.com/')
driver.find_element(By.XPATH,"//input[@id='singleFileInput']").send_keys(r"C:\Users\aksha\Pictures\wallpapers\4k-Mysterious-Black-Hole-AI-Generated-4K-Desktop-Wallpaper.jpg")

driver.find_element(By.XPATH,"//input[@id='multipleFilesInput']").send_keys(r"C:\Users\aksha\Pictures\wallpapers\4k-Ocean-View-Portal-4K-Wallpaper.jpg" + '\n' + r"C:\Users\aksha\Pictures\wallpapers\4k-Mysterious-Black-Hole-AI-Generated-4K-Desktop-Wallpaper.jpg" )
sleep(15)
driver.quit()
