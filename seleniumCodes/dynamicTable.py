from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# browser = webdriver.Chrome()
driver = webdriver.Edge()
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()



driver.close()
