from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# browser = webdriver.Chrome()
driver = webdriver.Edge()
driver.get("https://demo.nopcommerce.com/")
delay = 10 # seconds
driver.maximize_window()

#identify locator using id and name
#driver.find_element(By.ID, "small-searchterms").send_keys("Lenovo Thinkpad x1 carbon Laptop")
#driver.find_element(By.NAME, "q").send_keys("Lenovo Thinkpad x1 carbon Laptop")

#identify link text
driver.find_element(By.LINK_TEXT, "Register").click() #require the full text
driver.find_element(By.PARTIAL_LINK_TEXT, "Regist").click() #just require some of the text

#finding mutiple elements
#sliders = driver.find_elements(By.CLASS_NAME, "classname")



driver.close()
