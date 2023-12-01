import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# browser = webdriver.Chrome()
driver = webdriver.Edge()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.maximize_window()

#alert
driver.find_element(By.XPATH, "//button[normalize.space()='Click for Js Prompt']").click()

time.sleep(5)

alertWindow = driver.switch_to.alert
 print(alertWindow.text)
 alertWindow.send_keys("welcome")

 alertWindow.dismiss()


 #second example for

 