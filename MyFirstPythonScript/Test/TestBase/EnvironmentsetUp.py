'''
Created on Jun 15, 2018

@author: Datacore
'''
import unittest
import datetime
from selenium import webdriver


class EnvironmentSetUp(unittest.TestCase):
    

#setup for the browser setup attributes
    def setUp(self):
        #self.driver = webdriver.Chrome("C:\drivers\chromedriver.exe")
        #self.driver = webdriver.Chrome("..\Driver\chromedriver.exe")
        self.driver = webdriver.Chrome("C:\\Users\\Datacore\\eclipse-workspace\\PyDevProject\\MyFirstPythonScript\\Test\\Driver\\chromedriver.exe")
        print("Run has started at :" + str (datetime.datetime.now()))
        self.driver.set_page_load_timeout(20)
        print("------------------------")
        print("Test environment created")
       
    
#To close all browser instances and then quit
    def tearDown(self):
        if (self.driver!= None):
            print("------------------------")
            print("Test environment clears")
            print("Test run has completed :" + str(datetime.datetime.now()))
            self.driver.close()
            self.driver.quit()
