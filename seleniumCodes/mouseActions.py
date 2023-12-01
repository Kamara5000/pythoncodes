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

driver.get("https://opensource-demo.orangehrmlive.com/")

# driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

admin = driver.find_element(By.XPATH, "//*[@id = 'menu_admin_viewAdminModule']/b")
usermgmt = driver.find_element(By.XPATH, "//*[@id = 'menu_admin_UserManagement]")
users = driver.find_element(By.XPATH, "//*[@id = 'menu_admin_viewSystemUsers']")

#mousehover

act = ActionChains(driver)

act.move_to_element(admin).move_to_element(usermgmt).move_to_element(users).click().perform()

#rightclick



driver.maximize_window()