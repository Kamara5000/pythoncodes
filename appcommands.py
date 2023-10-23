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


#application command
print(driver.title)     #get the page title
print(driver.current_url)  #get current url
#print(driver.page_source)  #capture page source

#conditoional commands
#is_displayed()
#is_enabled()
#is_selected()

#navigation command



driver.close()
