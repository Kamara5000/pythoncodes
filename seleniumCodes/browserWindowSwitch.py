from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# browser = webdriver.Chrome()
driver = webdriver.Edge()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
delay = 10 # seconds
driver.maximize_window()

windowid = driver.current_window_handle  #get the id of a single window
windowiDs = driver.current_window_handles  #get the id of all the windows
parentwindow = windowiDs[0]
childwindow = windowiDs[1]

driver.switch_to.window(childwindow)
driver.switch_to.window(parentwindow)

#getting window id using loop
for winId in windowiDs:
    driver.switch_to.window(winId)
    print(driver.title)

#getting specific window id
for winId in windowiDs:
    driver.switch_to.window(winId)
    if driver.title == 'orangeHRM'
        driver.close()



