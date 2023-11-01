import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# browser = webdriver.Chrome()
driver = webdriver.Edge()
driver.get("https://itera-qa.azurewebsites.net/home/automation")

driver.maximize_window()

ele = driver.find_element(By.NAME, 'q')
ele.send_keys('selenium')
ele.submit()

# driver.find_element(By.XPATH, "//input[@id='monday']").click() - to get only one check box


# - to click on mutiple checkboxes
# checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
# when taking your xpath if you cant find a common xpath for all the elements customise it like above to macth the text boxex elements
# then loop to click all the checkboxes -
# approach 1 - for i in range(len(checkboxes)):
#     checkboxes[i].click()

# approach 2
# for checkbox in checkboxes :
#     checkbox.click()

# selecting checkboxes by choice
# for checkbox in checkboxes
#     weekname = checknow.get_attributes('id')
#     if weekname == 'monday' or  weekname == 'sunday'
#         checkbox.click()


# selecting last checkbox
# for i in range (len(checkboxes)-2, len(checkboxes)):
#     checkboxes[i].click()

# selecting first two boxes
# for i in range (len(checkboxes)):
#     if i<2:
#     checkboxes[i].click()

# unselecting all the checkboxes
# for checkbox in checkboxes:
#     if checkbox.is_selected:
#         checkbox.click()

