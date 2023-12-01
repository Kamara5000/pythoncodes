import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# browser = webdriver.Chrome()
driver = webdriver.Edge()

driver.implicitly_wait(10)

driver.get("https://swisnl.github.io/jquery-contextMenu/demo.html")

driver.maximize_window()

button = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")

act = ActionChains(driver)
act.context_click(button).perform()

#mousehover

act = ActionChains(driver)

act.move_to_element(admin).move_to_element(usermgmt).move_to_element(users).click().perform()

#rightclick



driver.maximize_window()