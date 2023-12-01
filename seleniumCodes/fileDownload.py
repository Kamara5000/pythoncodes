from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


def chromeSetup():
    driver = webdriver.Edge()

    # to download to a specific location add this preference
    preferences = {"download.default_directory":"C:\Users\ibrah\Desktop"}

    #or make the reference to take a dynamic location
    
    return driver

my_driver = chromeSetup()
my_driver.get("https://file-example.com/index.php/sample-documents-download/sample-doc-download")
my_driver.maximize_window()
my_driver.find_element(By.Xpath,"//tbody/tr[1]/td[5]/a[1]").click()


