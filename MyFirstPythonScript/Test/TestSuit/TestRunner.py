'''
Created on Jun 22, 2018

@author: Datacore
'''


import unittest
from MyFirstPythonScript.Test.Scripts.Registrationpage import Registration
import os 
from datetime import datetime
from MyFirstPythonScript.Test.HTMLTestRunner import HTMLTestRunner
from MyFirstPythonScript.Test.Scripts import RegistrationPageReadExcel

from Test.Scripts.RegistrationPageReadExcel import Registration


direct = os.getcwd()


class MyTestSuite(unittest.TestCase):
        
        
    def test_tSuite(self):
            
        loader = unittest.TestLoader().loadTestsFromTestCase(Registration)
        suite = unittest.TestSuite(loader)
        datestring = datetime.now().strftime("Regression_report_%Y_%m_%d_%H%M.html")
        outfile = open(direct + datestring, 'w')
        runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,
                    verbosity=2,
                    title='Registration Report',
                    description='This is a demo report')
        
        #runner = HTMLTestRunner(output='example_suite')
        runner.run(suite)
        #unittest.TextTestRunner.run(suite)


if __name__ == '__main__':        
    unittest.main()        
        
    
    