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


elements = driver.find_elements(By.XPATH, "//div[@class=''footer]//a")
print(len(elements))    #print the number or length of items in the list
print(elements[0].text)  #print the text of the element with index 0 in the list
for ele in elements:     #loop through the list and print the text of each element
    print(ele.text)

driver.close()
