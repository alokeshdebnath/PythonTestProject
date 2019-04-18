'''
Created on Jun 15, 2018

@author: Datacore
'''

from MyFirstPythonScript.Test.PageObject.Locators import Locator
from selenium.webdriver.common.by import By


class Home(object):
    
    def __init__(self, driver):
        self.driver = driver
        
#Home page locators defination        
        self.signOn = self.driver.find_element(By.XPATH, Locator.sign_on)
        self.contact = self.driver.find_element(By.XPATH, Locator.contact)
        self.support = self.driver.find_element(By.XPATH, Locator.support)
        self.register = self.driver.find_element(By.XPATH, Locator.register)
    
    
#Below method have defined based on functionality
    
    def getSignOn(self):
        return self.signOn
    
    def getContact(self):
        return self.contact
    
    def getSupport(self):
        return self.support
    
    def getRegister(self):
        return self.register
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        