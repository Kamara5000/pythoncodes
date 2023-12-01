import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# browser = webdriver.Chrome()
driver = webdriver.Edge()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

driver.maximize_window()

# driver.switch_to.frame(0) #switch to frame

#input date method
driver.find_element(By.XPATH, "//input[@id='dob']").click()

datepicker_month = Select(driver.find_element(By.XPATH, "//select[@data-handler='selectMonth']"))
datepicker_month.select_by_visible_text("Dec")

datepicker_picker = Select(driver.find_element(By.XPATH, "//select[@data-handler='selectYear']"))
datepicker_picker.select_by_visible_text("1990")

alldates = driver.find_elements(By.XPATH, "//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")
for date in alldates:
    if date.text == "25":
        date.click()

        break;


#selecting the value method


