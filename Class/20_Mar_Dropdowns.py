#select dropdown or dropdown implementation ->1)using html <select> tag
# 3 WAYS - SELECT BY VISIBLE TEXT
#          -> SELECT by index
         # -> select by value
# 2)#custom dropdown - can be lis or div etc


# 2 types of dropdowns - single dropdown
#                      - multiple

from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)

driver.get("file:///C:/Users/aksha/AppData/Local/Packages/5319275A.WhatsAppDesktop_cv1g1gvanyjgm/LocalState/sessions/2466420CB81B8587AA7D4E5BB1F7A57ABB5E0186/transfers/2026-12/E22_Dropdowns.html")
driver.maximize_window()

dropdown = driver.find_element(By.ID,"state")

# option = Select(dropdown)
#
# option.select_by_visible_text("Maharastra")
#
# option.select_by_value("MH")
#
# option.select_by_index(2)
#
# driver.find_element(By.XPATH,'//select[@ID="hobby"]//option[1]').click()
# driver.find_element(By.XPATH,'//select[@ID="hobby"]//option[2]').click()
# # driver.find_element(By.XPATH,'//select[@ID="hobby"]//option[2]').click()


