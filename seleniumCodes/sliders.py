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

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQueryUI/")

driver.maximize_window()


min_slider = driver.find_element(By.XPATH, "//body//div//span[1]")
max_slider = driver.find_element(By.XPATH, "//body//div//span[2]")

print(min_slider.location)
print(max_slider.location)

act = ActionChains(driver)

act.drag_and_drop_by_offset(min_slider,100,0).perform()
act.drag_and_drop_by_offset(max_slider,-39,0).perform()



