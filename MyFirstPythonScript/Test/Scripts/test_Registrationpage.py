'''
Created on Jun 20, 2018

@author: Datacore
'''
import unittest
#first change
#from selenium import webdriver
from MyFirstPythonScript.Test.PageObject.Page.Registerpage import Register
from MyFirstPythonScript.Test.TestUtility.ScreenShot import ScreenshotTest
from MyFirstPythonScript.Test.PageObject.Page.Homepage import Home
from MyFirstPythonScript.Test.TestBase.EnvironmentsetUp import EnvironmentSetUp
from time import sleep
from selenium.common.exceptions import TimeoutException

from datetime import datetime
#from MyFirstPythonScript.Test.LogFiles.Logs import Logger



class Registration(EnvironmentSetUp):

    
    def test_RegistrationFlow(self):
        
        ss_path ="\\MercuryTour_"
        
        driver = self.driver
        
        ss = ScreenshotTest(driver)
       
        
        print("Hello Testing QA1")
       
        try:
            datestring = datetime.now().strftime("_%Y_%m_%d_%H%M.png")
            self.driver.get("http://newtours.demoaut.com")
        
            self.driver.set_page_load_timeout(20)
            
            ss.ScreenShot(ss_path + "Home" + datestring)
              
            expected_title = "Welcome to: Mercury Tours"  
            actual_title = self.driver.title
            
            if (actual_title == expected_title):
                print(self.driver.title)
                print("Webpage has been loaded successfully")
            else:
                print("Fail in web title")
            
#Home page             
            home = Home(driver)
            
            if home.getRegister().is_displayed():
                home.getRegister().click()
                sleep(6)
          
#Registration page            
            reg = Register(driver)
        
            reg.getFirstName("Alokesh5")
            reg.getLastName("Debnath")
            reg.getPhone("2523256333")
            reg.getEmail("test@test.com")
            reg.getCountry("INDIA")
            reg.getUserName("a@d.com")
            reg.getPassword(123)
            reg.getConfirmPassword(123)
            sleep(2)
            
            ss.ScreenShot(ss_path + "Registration" + datestring)
            
            reg.getsubmit()
            sleep(5)
            
        except TimeoutException as e:
            print(str(e))
            print("Title mismatch") 
            
        
        ss.ScreenShot(ss_path + "Final" + datestring)
        
        
        #lg.get_browser_console_log(self)
        


if __name__ == "__main__":
    unittest.main()
    #unittest.main(testRunner=HTMLTestRunner(output='example_dir'))
    
    
    
    
    
    
    
    
    
    