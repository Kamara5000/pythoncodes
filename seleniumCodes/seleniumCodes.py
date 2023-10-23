#
# Test case
# -open browser
# -open url
# -provide email
# -provide password
# -click login
# -capture title of the dashboard
# -verify title of the page
# -close page

#from selenium import webdrivertry:
    myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH,"//button[@type='submit']")))
    browser.find_element(By.NAME, "username").send_keys("Admin")
    browser.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("admin123")
    browser.find_element(By.XPATH,"//button[@type='submit']").click()

    act_title = browser.title
    exp_title = "OrangeHRM"
    if act_title ==exp_title:
        print("LoginTestPassed")
    else:
        print("TestFailed")

    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

#driver = webdriver.Chrome(executable_path = "C:/Users/ibrah/Desktop/webdriversfolder/chromedriver.exe")

#driver = webdriver.Chrome("C:/Users/ibrah\Desktop/webdriversfolder/chromedriver-win64.exe")

#driver = webdriver.edge("C:/Users/ibrah/Desktop/webdriversfolder/edgeDriver")
#the chromedriver object takes the chrome driver location as a parameter
#driver.get("https://opensource-demo.orangehrmlive.com/")

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# browser = webdriver.Chrome()
browser = webdriver.Edge()
# browser.get("https://google.com")
browser.get("https://opensource-demo.orangehrmlive.com/")
delay = 10 # seconds



# browser.find_element_by_name("username").send_keys("Admin")
# browser.find_element_by_name("password").send_keys("admin123")
# browser.find_element_by_xpath("//button[normalize-space()='Login']").click()

# us = browser.find_element(By.NAME,"username").send_keys()
#browser.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys()

#browser.close()