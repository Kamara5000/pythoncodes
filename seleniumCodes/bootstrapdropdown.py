import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# browser = webdriver.Chrome()
driver = webdriver.Edge()

driver.implicitly_wait(10)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application")

driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']").click()

country_list = driver.find_elements(By.XPATH, "//ul[@id='select2-billing_country-results']/li")
print(len(country_list))

for country in country_list:
    if country.text == "India":
        country.click()
        break












driver.maximize_window()




