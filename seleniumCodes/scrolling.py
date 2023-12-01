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

#using javasript within

#scroll by pixel
driver.execute_script("window.scrollBy(0,3000)", "")
value = driver.execute_script("return window.pageYOffset;")
print("number of pixels moved", value)

#scroll until element is visible
flag = driver.find_element(By.ID, "//img[@alt='flag' of India']")
driver.execute_script("argyments[0].scrollIntoView();", flag)
value = driver.execute_script("return window.pageYOffset;")
print("number of pixels moved", value)

#scroll down till end
driver.execute_script("Window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("number of pixels moved", value)

#scroll back to starting point
#put - in front of document.body
driver.execute_script("Window.scrollBy(0,-document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("number of pixels moved", value)



