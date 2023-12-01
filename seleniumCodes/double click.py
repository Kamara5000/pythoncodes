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

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")

driver.switch_to.frame("iframeResult")  #switch to frame

field1 = driver.find_element(By.XPATH, "//input[@id='field']")

field1.clear()

field1.send_keys('welcome')

button= driver.find_element(By.XPATH, "//button[normalize-space()='copy Text']")

act = ActionChains(driver)
act.double_click(button).perform()  #double click action


driver.maximize_window()