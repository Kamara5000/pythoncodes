import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# browser = webdriver.Chrome()
driver = webdriver.Edge()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

driver.maximize_window()

#iframe

#you have to acess the frame before you can locate the element
#to switch to the frame you can use any of the  method below
switch_to.iframe(name of the frame) - using the name of frame if frame has a name tag
switch_to.iframe(id of the frame) - using id of the frame
switch_to.iframe(webelement) - using element to capture the frame
switch_to.iframe(0) - using index of the frame if the frame is only one


# -swichting between multiple frame
#
# switch_to.iframe(packageListFrame)
# driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
# driver.switch_to.default_content() #you have to switch back to main web frame before re-switching to the second iframe
# switch_to.iframe(packageFrame)
# driver.find_element(By.LINK_TEXT, "webdriver").click()
#
# -switching between an iframe and to another  sub inner iframe in the iframe
#
# outerframe - driver.find_element(By.XPATH, "//iframe[@]")#switch to the outerframe
#  driver.switch_to.frame(outerframe)
#
# innerframe= driver.find_element(By.XPATH, "/html/body" #switch to inner frame
# inner.switch_to.frame(innerframe)
#
# driver.find_element(By.XPATH, "//input[@type]").send_keys('welcome')
# driver.switch_to.parent_frame()  #switch to parent frame



 #second example for