import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# browser = webdriver.Chrome()
driver = webdriver.Edge()

#you can inject your username and password in to the url to bypass the pop in example below
driver.get("https://admin:adminthe-internet.herokuapp.com/javascript_alerts")

driver.maximize_window()



 #second example for