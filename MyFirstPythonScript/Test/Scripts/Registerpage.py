'''
Created on Jun 20, 2018

@author: Datacore
'''
import unittest
from MyFirstPythonScript.Test.PageObject.Locators import Locator
#from selenium.webdriver.support.select import Select
from selenium.webdriver.support.select import By
#from driver import driver

class Register(object):


    def __init__(self, driver):
        self.driver = driver


        self.FirstName = self.driver.find_element(By.XPATH, Locator.firstName)
        self.LastName = self.driver.find_element(By.XPATH, Locator.lastName)
        self.phone = self.driver.find_element(By.XPATH, Locator.phone)
        self.Email = self.driver.find_element(By.XPATH, Locator.email)
        self.Country = self.driver.find_element(By.XPATH, Locator.country)
        self.UserName = self.driver.find_element(By.XPATH, Locator.userName)                                                                                 
        self.signOnPassword = self.driver.find_element(By.XPATH, Locator.password)
        self.signOnConfirmPassword = self. driver.find_element(By.XPATH, Locator.confirmPassword)
        self.submit = self.driver.find_element(By.XPATH, Locator.regisSubmit)
        
#Webelement is defining here
        
    def getFirstName(self,FName):
        self.FirstName.send_keys(FName)
        
    def getLastName(self,LName):
        self.LastName.send_keys(LName)
    
    def getPhone(self,Phone):
        self.phone.send_keys(Phone)
    
    def getEmail(self,Email):
        self.Email.send_keys(Email)    
        
    def getCountry(self,Country):
        self.Country.send_keys(Country)
        
    def getUserName(self,UserName):
        self.UserName.send_keys(UserName)
    
    def getPassword(self,Password):
        self.signOnPassword.send_keys(Password)
        
    def getConfirmPassword(self,CPassword):
        self.signOnConfirmPassword.send_keys(CPassword)
        
    def getsubmit(self):
        self.submit.click()



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()