from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# browser = webdriver.Chrome()
driver = webdriver.Edge()
driver.get("https://automationpractice.com/index.php")
delay = 10 # seconds
driver.maximize_window()


try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME,"homeslider-container")))

    sliders = driver.find_elements(By.CLASS_NAME, "homeslider-container")

    links = driver.find_elements((By.TAG_NAME,'a'))
    print(len(links)) #print number of link in the webpage

    print(len(sliders))

    print("the number of item is" , len(sliders) )
except TimeoutException:
    print("Loading took too much time!")
#finding mutiple elements



driver.close()
