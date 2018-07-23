'''
Created on Jun 15, 2018

@author: Datacore
'''


class ScreenshotTest(object):

        
    def __init__(self,driver):
        self.driver = driver
        
    
    def ScreenShot(self, path):
        directory = "C:\\Users\\Datacore\\eclipse-workspace\\PyDevProject\\MyFirstPythonScript\\Test\\ScreenShots\\Registration"
        self.driver.get_screenshot_as_file(directory+path)
    
        
    
