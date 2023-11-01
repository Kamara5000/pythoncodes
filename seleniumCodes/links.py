import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# browser = webdriver.Chrome()
driver = webdriver.Edge()
driver.get("https://itera-qa.azurewebsites.net/home/automation")

driver.maximize_window()

# -click on link
# driver.find_element(By.LINK_TEXT. 'Digittal dowload').click()
# driver.find_element(By.PARTIAL_LINK_TEXT. 'Digittal dowload').click()
#
# links = driver.find_elements(By.XPATH, '//a')  - get mutiple links
# print('total number of link ', len(links))
#  for lnk in links;
#      print(link.text)   - get the names of the links

# -to get a broken link
# -install request package
#alllinks = driver.find_elements(By.TAG_NAME, 'a')
count = 0
# for link in allLinks:
#     url = link.get_attribute('href')
#     try:
#     res = requests.head(url)
#     except:
#     None
#     if res.status_code >= 400:
#         print(url,'is broken link')
#         count+1
#     else:
#         print(url, "is valid")
# print("total number of broken link is", count)
# driver.find_element(By.L