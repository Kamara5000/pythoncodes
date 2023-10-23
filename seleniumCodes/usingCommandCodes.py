import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# browser = webdriver.Chrome()
driver = webdriver.Edge()
driver.get("https://demo.nopcommerce.com/")
delay = 10 # seconds
driver.maximize_window()

searchBox = driver.find_element(By.XPATH, "//*[@id='small-searchterms']")
print("status ", searchBox.is_enabled())
print("status", searchBox.is_displayed())


#to check if a radio button is selected or tick

rd_male = driver.find_element(By.XPATH, "//*[@id='gender-male']" )

print(rd_male.is_selected())

rd_male.click()

print("check if click", rd_male.is_selected())






time.sleep(5)

driver.close()  #close only the window thar is focused it starts with
#driver.quit()   #close multiple brower users and kill the process
