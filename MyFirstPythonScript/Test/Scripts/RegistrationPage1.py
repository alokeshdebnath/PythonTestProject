# '''
# Created on Jun 20, 2018
# 
# @author: Datacore
# '''
import xml.dom.minidom
import unittest
#import xml.etree.ElementTree as ET


# all items data
def test_main():
    doc = xml.dom.minidom.parse("C:\\Users\\Datacore\\eclipse-workspace\\PyDevProject\MyFirstPythonScript\\TestXml.xml")

    print (doc.nodeName)
    print (doc.firstChild.tagname)
# from MyFirstPythonScript.Test.PageObject.Page.Registerpage import Register
# from MyFirstPythonScript.Test.TestUtility.ScreenShot import ScreenshotTest
# from MyFirstPythonScript.Test.PageObject.Page.Homepage import Home
# from MyFirstPythonScript.Test.TestBase.EnvironmentsetUp import EnvironmentSetUp
# from time import sleep
# from selenium.common.exceptions import TimeoutException
# from datetime import datetime
# 
# 
# from ddt import ddt, data, unpack
# from MyFirstPythonScript.Test.Library.GetData import get_csv_data
# #import email
# 
# @ddt
# class Registration(EnvironmentSetUp):
# 
#     
#     @data(*get_csv_data("C:/Users/Datacore/eclipse-workspace/PyDevProject/MyFirstPythonScript/Test/data/DatCsv.csv"))
#     @unpack
#     def test_RegistrationFlow(self, FName, LName, phone, Email, 
#                             Country, UserName, signOnPassword, signOnConfirmPassword):
#         
# 
#         ss_path ="\\MercuryTour_"
#         
#         driver = self.driver
#         
#         ss = ScreenshotTest(driver)
#         
#         print("Hello")
#        
#         try:
#             datestring = datetime.now().strftime("_%Y_%m_%d_%H%M.png")
#             self.driver.get("http://newtours.demoaut.com")
#         
#             self.driver.set_page_load_timeout(20)
#             
#             ss.ScreenShot(ss_path + "Home" + datestring)
#               
#             expected_title = "Welcome: Mercury Tours"  
#             actual_title = self.driver.title
#             if (actual_title == expected_title):
#                 print(self.driver.title)
#                 print("Webpage loaded successfully")
#             else:
#                 print("Failed in title")
#             
# #Home page             
#             home = Home(driver)
#             if home.getRegister().is_displayed():
#                 home.getRegister().click()
#                 sleep(4)
#           
# #Registration page            
#             reg = Register(driver)
#             reg.getFirstName(FName)
#             reg.getLastName(LName)
#             reg.getPhone(phone)
#             reg.getEmail(Email)
#             reg.getCountry(Country)
#             reg.getUserName(UserName)
#             reg.getPassword(signOnPassword)
#             reg.getConfirmPassword(signOnConfirmPassword)
#             sleep(2)
#             
#             ss.ScreenShot(ss_path + "Registration" + datestring)
#             reg.getsubmit()
#             sleep(5)
#             
#         except TimeoutException as e:
#             print(str(e))
#             #print("Title mismatch") 
#         
#         ss.ScreenShot(ss_path + "Final" + datestring)
# 
if __name__ == "__main__":
    unittest.main();
#     #unittest.main(testRunner=HTMLTestRunner(output='example_dir'))
#     
#     
#     
#     
#     
#     
#     
#     
#     
#     