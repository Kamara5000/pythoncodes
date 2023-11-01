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
#is_displayed() -to check if an element is displayed
#is_enabled() -to check if an element is enabled
#is_selected() -to check if an element is selected
#element.text  - to get the text of an element either text box or input boxs
#element.text only return innerText
#get_attribute -  return text of the attribute of the elemets e.g element,get_attribute('value') return the value in the element
#element.get_attribute('name') gets the text of the name in the element attributes
#element.clear - to clear input box
#
#navigation command



driver.close()
