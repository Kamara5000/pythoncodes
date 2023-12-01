import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# browser = webdriver.Chrome()


#to disable notification add this option
ops = webdriver.ChromeOptions()

ops.add_argument("--disable-notifications")
ser_obj = Service("C:/Users/ibrah/Desktop/webdriversfolder/chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj, options=ops)

driver.get("https://whatmylocation.com/")

driver.maximize_window()


