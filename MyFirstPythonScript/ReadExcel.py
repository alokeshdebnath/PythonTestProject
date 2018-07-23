'''
Created on Jun 29, 2018

@author: Datacore
'''
from selenium import webdriver
import unittest
import nose
from ddt import ddt, data, unpack
#from openpyxl import load_workbook
import xlrd
#import os

def getData():
#load Workbook
    myrows = []
    wk = xlrd.open_workbook('C:\\Users\\Datacore\\eclipse-workspace\\PyDevProject\\MyFirstPythonScript\\PyExcelTest.xlsx')
    sh = wk.sheet_by_index(0)
#sh = wk.active

    print("Printing all cell")

    for row_index in range (1, sh.nrows):
        myrows.append(list(sh.row_values(row_index, 0, sh.ncols)))
        
    print ("\n")
    return myrows

# sh = wk.get_sheet_by_name('Sheet1')
# print(sh)
# 
# c =sh['B4'].value
# print(c)
# 
# print("Active sheet is " + wk.active.title)


#sh = wk.active
#Create object of any sheet



# print(sh.title)
# #print(sh['A3'].value)
# 
# sh.max_rows
# sh.max_cloumns
# c1 = sh.cell(column=1,row=3)
# print(c1.column)
# print(c1.row)
# 
# #row = sh.max_rows
# #columns = sh.max_column
# #print(str(row))
# 
# for i in range(1, 7):
#     for j in range(1, 2):
#         c= sh.cell(i,j)
#         print(c.value)