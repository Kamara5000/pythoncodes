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


