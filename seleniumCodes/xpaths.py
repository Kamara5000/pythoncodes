#xpath is an xml path on the page, it is an address of the element

#absolute/full xpath start with /
#relative or partial xpath  start with  //

#creating xpath manually
#

#creating automatically
#right click on element - inspect -highlight html code - right click - copyxpath
#use selectorhub as well
#relative is better than absolute xpath becuase of the ong nature of absoliute which may cause issue when a developer change any tag

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# browser = webdriver.Chrome()
driver = webdriver.Edge()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
delay = 10 # seconds
driver.maximize_window()

driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")

#text()
#driver.find_element(By.XPATH, "//a[text()='women']").click()


driver.close()

