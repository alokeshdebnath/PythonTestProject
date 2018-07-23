'''
Created on Jun 15, 2018

@author: Datacore
'''
import unittest
from MyFirstPythonScript.Test.PageObject.Locators import Locator
#from selenium.webdriver.support.select import select
from selenium.webdriver.common.by import By


class SampleTest(object):
    
    def _init_(self, driver):
        self.driver = driver
    
    
    def launchSite(self):        
        self.driver.get("http://newtours.demoaut.com")
        
        self.signOnUsername = self.driver.find_element(By.XPATH, Locator.signOn_username)
        self.signOnPassword = self.driver.find_element(By.XPATH, Locator.signOn_password)
        
        self.driver.maximize_window()
        print(self.driver.title)
        self.driver.find_element(By.ID, "lst-ib").send_keys("selenium")
        self.driver.get_screenshot_as_file("C\Python\home.png")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()