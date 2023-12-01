import os
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# browser = webdriver.Chrome()
driver = webdriver.Edge()

driver.implicitly_wait(10)

driver.get("https://www.demo.nopcommerce.com/")
driver.maximize_window()


driver.save_screenshot("C:\\Users\\ibrah\\Pictures\\homepage.png")

#or using the current directory(cwd) as the dowload path
#driver.save_screenshot(os.getcwd()+"\\homepage.png")

driver.quit()









