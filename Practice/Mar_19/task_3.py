from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.implicitly_wait(10)

driver.get('https://demoqa.com/automation-practice-form')
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='firstName']").send_keys('Akshat')
driver.find_element(By.XPATH,"//input[@id='lastName']").send_keys('Tated')
driver.find_element(By.XPATH,"//input[@id='userEmail']").send_keys('akshat@gmail.com')
driver.find_element(By.XPATH,"//input[@id='gender-radio-1']").click()
driver.find_element(By.XPATH,"//input[@id='userNumber']").send_keys('7441176670')
#
driver.find_element(By.XPATH,"//input[@id='dateOfBirthInput']").click()
driver.find_element(By.XPATH,"//div[@class='react-datepicker__year-dropdown-container react-datepicker__year-dropdown-container--select']").click()
driver.find_element(By.XPATH,"//option[text()=2000]").click()
driver.find_element(By.XPATH,"//select[@class='react-datepicker__month-select']").click()
driver.find_element(By.XPATH,"//option[@value='9']").click()
driver.find_element(By.XPATH,"//div[text()='11']").click()
#
#
subject=(driver.find_element(By.XPATH,"//input[@id='subjectsInput']"))
subject.send_keys('Maths')
subject.send_keys(Keys.ENTER)
subject.send_keys('English')
subject.send_keys(Keys.ENTER)
#
driver.find_element(By.ID,"hobbies-checkbox-1").click()
driver.find_element(By.ID,"hobbies-checkbox-3").click()
driver.find_element(By.XPATH,"//input[@id='uploadPicture']").send_keys(r"C:\Users\aksha\Pictures\wallpapers\4k-Mysterious-Black-Hole-AI-Generated-4K-Desktop-Wallpaper.jpg")
driver.find_element(By.XPATH,"//textarea[@id='currentAddress']").send_keys('Tated Parisar civil line road jaora')

dd1=driver.find_element(By.XPATH,"//input[@id='react-select-3-input']")
dd1.send_keys('Madhya Pradesh')
dd1.send_keys(Keys.ENTER)
dd2=driver.find_element(By.XPATH,"//input[@id='react-select-4-input']")
dd2.send_keys('Ratlam')
dd2.send_keys(Keys.ENTER)
driver.find_element(By.ID,"submit").click()

driver.quit()

##extra task 3
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.implicitly_wait(10)
driver.get('https://demowebshop.tricentis.com/register')

driver.find_element(By.XPATH,"//input[@id='gender-male']").click()
driver.find_element(By.XPATH,"//input[@id='FirstName']").send_keys('Akshat')
driver.find_element(By.XPATH,"//input[@id='LastName']").send_keys('Tated')
driver.find_element(By.XPATH,"//input[@id='Email']").send_keys('akshattated18@gmail.com')
driver.find_element(By.XPATH,"//input[@id='Password']").send_keys('abby1234')
driver.find_element(By.XPATH,"//input[@id='ConfirmPassword']").send_keys('abby1234')

driver.find_element(By.XPATH,"//input[@id='register-button']").click()
driver.quit()