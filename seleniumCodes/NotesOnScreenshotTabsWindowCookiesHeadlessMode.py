#notes on other aspect
for bootstrap dropdown

-get the locator of the drop down
-

for capturing screenshot
-driver.save_screenshot()

driver.get_screenshot_as_file()

driver.get_screenshot_as_base64()

driver.get_screenshot_as_png()


		TapsAndWindow
#to move, open and switch to another tab from a tab
-get the link
-use the driver.switch_to.new_window('tab')
-then get/open the new link on the new tab opened

		TapsAndWindow
#to move, open and switch to another window from a window
-get the link
-use the driver.switch_to.new_window('window')
-then get/open the new link on the new window opened


				-Cookies

cook = driver.get_cookies() #capture all cookies from the browser and save it into varibale cook

#get size of cookies
print("length of cookies", + len(cook))  #get the length of cookies


#print sone value of cookies
for c in cook:
	print(c.get('name'), c.get('value'))



#adding new cookie
driver.add_cookie({"name":"newcookies", "value":"323edfsfs"})

#deleting cookie
driver.delete_cookie('newcookies')

#delete all cookies
driver.delete_all_cookies


			#Headless mode
#(means without gui, still execute the code. one of advantage is u can run your code and be doing other task, it is also fast, diadvantage is that you wont see what the application is doing)

def headless_chrome():
	from selenium.webdriver.chrom.service import service
	serv_obj = Service("put your chrome driver path here")
	ops=webdriver.ChromeOptions()
	ops.headless = True
	driver = webdriver.Chrome(Service=serv_obj,options=ops)
	retunr driver

driver=headless_chrome()
driver.get("https://www.google.com")



			#Data driven Testing

#install openpyxl - to work with excel files(.xlsx)

import opnepyxl

file_path="put the path of your excel file"

workbook = openpyxl.load_workbook(file_path) #capture the file

sheet= workbook["name of your excel sheet"]

#find rows and column
rows = sheet.max_row #count number of row having data, it wont consider empty row
cols = sheet.max_column #count number of column, it wont consider empty column

#reading rows and column from an excel file
	for r in range(1, rows+1):
		for c in range(1, cols+1):
			print(sheet.cell(r,c).value, end='       ')
		print()

#writing to excel files
workbook = openpyxl.load_workbook(file_path) #capture the file
sheet= workbook.active #name of your active excel sheet

for r in range(1,6):
	for c in range(1,4):
		sheet.cell(r,c).value="welcome"
workbook.save(file_path)

#inserting multiple data
#row1
sheet.cell(1,1).value = 1
sheet.cell(1,2).value = 12
sheet.cell(1,3).value = 123

#row2
sheet.cell(2,1).value = 1
sheet.cell(2,2).value = 12
sheet.cell(2,3).value = 123


#Data-driven Testing example

#using excel
-get your data from the excel
-input the data into the application
-then compare the result from the application with the result from your excel, write into excel pass/or fail into the result field

#using database
-install database connector

database operations - insert,update,select,






