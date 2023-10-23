from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# browser = webdriver.Chrome()
driver = webdriver.Edge()
driver.get("https://facebook.com")

driver.maximize_window()

#using customise locator
#tagnameandId
#tagname#id

driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc")

#tagandclassname
#tagname.classname
driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("abc")

#tagandAttribute
#tagname[attribute=value]
driver.find_element(By.CSS_SELECTOR, "input[data-testid=royal_email]").send_keys("abc")

#tagandclassandAttribute
#tagname.valueofClass[attribute=value]

driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_pass]").send_keys("xyz")


driver.close()
