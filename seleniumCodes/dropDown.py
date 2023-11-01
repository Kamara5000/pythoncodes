from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# browser = webdriver.Chrome()
driver = webdriver.Edge()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# driver.maximize_window()
# drpcountry_ele= driver.find_element(By.XPATH, "//select[@id='input-country']")
# drpcountry = Select(drpcountry_ele)
#
# drpcountry.select_by_visible_text("India") #select the option by visible test
#
# drpcountry.select_by_value("10") #select using the value attribute
#
# drpcountry.select_by_index(13) #select using the index

#selecting all the options in the drop down
# alloptions = drpcountry.options
#     print('totalnumberofoption', len(alloptions))
#
#     for opt in alloptions:
#         print(opt.text)


#selecting option without using build in options

for opt in alloptions:
    if opt.text = "india":
        opt.click()
        break

