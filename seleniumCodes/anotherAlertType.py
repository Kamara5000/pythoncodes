import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# browser = webdriver.Chrome()
driver = webdriver.Edge()
driver.get("https://mypage.rediff.com/login/dologin")

driver.maximize_window()

#alert
driver.find_element(By.XPATH, "//input[@value='login']]").click()
time.sleep(5)
driver.switch_to.alert.accept()

