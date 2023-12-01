import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# browser = webdriver.Chrome()
driver = webdriver.Edge()

driver.implicitly_wait(10)

driver.get("https://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

driver.maximize_window()

source_ele = driver.find_element(By.ID, "box6")

target_ele = driver.find_element(By.ID, "box106")
act = ActionChains(driver)
act.drag_and_drop(source_ele,target_ele).perform()







