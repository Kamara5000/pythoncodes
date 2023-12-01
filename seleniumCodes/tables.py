import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# browser = webdriver.Chrome()
driver = webdriver.Edge()
driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

#getting number of column and row
no_row= len(driver.find_elements(By.XPATH, "//table[@name = 'BookTable']/tbody/tr"))

no_colmn= len(driver.find_elements(By.XPATH, "//table[@name = 'BookTable']/tbody/tr[1]/th"))

#print(no_row, no_colmn)

#to get specific data in the table pass the indexes
data = driver.find_element(By.XPATH, "//table[@name = 'BookTable']/tbody/tr[2]/td[1]").text

print(data)


#printing all data in the rows and column
for r in range(2,no_row+1):
    for c in range(1, no_colmn+1):
        data =driver.find_element(By.XPATH, "//table[@name = 'BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data, end='       ') #end= to print rows on a row
#to dynamiccally pass parameter into xpath you have to follow the syntax like above
driver.close()

#printing data base on condition
for r in range(2, no_row+1):
    authorName = driver.find_elements(By.XPATH, "//table[@name = 'BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
    if authorName == "Mukesh":
     bookName = driver.find_element(By.XPATH, "//table[@name = 'BookTable']/tbody/tr["+str(r)+"]/td[1]").text
     print(bookName+"     ".authorName)

