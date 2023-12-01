import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# browser = webdriver.Chrome()
driver = webdriver.Edge()
driver.get("https://jqueryui.com/datepicker/")

driver.maximize_window()

driver.switch_to.frame(0) #switch to frame

#input date method
driver.find_element(By.XPATH, "//*[@id='datepicker']").send_keys("05/30/2022")

#selecting the value method
driver.find_element(By.XPATH, "//*[@id='datepicker']").send_keys() #open datepicker
year = "2021"
month = "march"
day = "30"

while True:
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    if mon==month and yr==year:
        break;
    else:
        driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[2]/span").click() #click next arrow

dates = driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']//table/tbody/tr/td/a")
for ele in dates:
    if ele.text ==dates:
        ele.click()
        break