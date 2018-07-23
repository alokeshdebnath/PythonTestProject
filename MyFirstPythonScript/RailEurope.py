import xlrd

#from selenium import webdriver
#import numpy as np


workbook = xlrd.open_workbook("C:\\Users\\Datacore\\Desktop\Python\\UAT-Non-Regression.xlsx")

worksheet = workbook.sheet_by_index(0)

sheetCount = workbook.nsheets

print("No. of sheets :{0}".format(sheetCount))

total_rows = worksheet.nrows
total_columns = worksheet.ncols

print("Total no. of rows: {0}".format(total_rows))
print("Total no. of columns: {0}".format(total_columns))

table = list()
record = list()

for x in range(total_rows):
    for y in range(total_columns):
        record.append(worksheet.cell(x,y).value)
    table.append(record)
    record = []
    x +=1

print (table)

#df = pd.read_ex("C:\\Users\\Datacore\\Desktop\Python\\UAT-Non-Regression.xlsx")

#print (df)













 