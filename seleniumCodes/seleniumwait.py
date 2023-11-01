import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# browser = webdriver.Chrome()
driver = webdriver.Edge()
driver.get("https://google.com")

driver.maximize_window()

ele = driver.find_element(By.NAME, 'q')
ele.send_keys('selenium')
ele.submit()

driver.find_element(By.XPATH, "//h3[text()='selenium']").click()

# time.sleep(time in seconds) -the performance of the script is very poor
# if the element is not available within the time mention there is a chance of getting excpetion

# implicit wait
# driver.implicitly_wait(10)  -no performance reduction issue- immediately the element is available within the time mention it continues

# driver.explicitly_wait() - it takes condition i.e wait for the element to be present without time
# explicit wait is discover as follows with the example
# myWait = WebDriverWait(driver, 10)
# searchLink = myWait.until(EC.presence_of_element_located(By.XPATH, "//h3[text()='selenium']")) - EC is the expected condition
# searchLink.click()
# you can also add an exception handling
# myWait = WebDriverWait(driver, 10,poll_frequency ignored_exceptions=[NoSuchElementException, ElementNotVisible, ElementNotSelectable,Exception])
# poll_frequency can be added to make the page look for elemet for every second you specify




driver.close()
