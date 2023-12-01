import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# browser = webdriver.Chrome()
driver = webdriver.Edge()

driver.implicitly_wait(10)

driver.get("https://text-compare.com/")
input1 = driver.find_element(By.XPATH, "//textarea[@id='inputText1']")
input2 = driver.find_element(By.XPATH, "//textarea[@id='inputText2']")

input1.send_keys("welcome")

#to highlight the textarea
#method 1
act= ActionChains(driver)
# act.key_down(keys.CONTROL)#
# act.send_keys("a")
# act.key_up(keys.CONTROL)
# act.perform()

#method2
act.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()

#control c - to copy the text

# act= ActionChains(driver)
# act.key_down(keys.CONTROL)#
# act.send_keys("c")
# act.key_up(keys.CONTROL)
# act.perform()

#or make it a single statement
act.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

# act.send_key(Keys.TAB)
# act.perform()

#or on a single line
act.send_key(Keys.TAB).act.perform()


#input2 -->paste
act.key_down(Keys.CONTROL)
act.send_keys('v')
act.key_up(Keys.CONTROL)
act.perform()

act.key_down(Keys.CONTROL).act.send_keys('v').act.key_up(Keys.CONTROL).act.perform()














driver.maximize_window()




