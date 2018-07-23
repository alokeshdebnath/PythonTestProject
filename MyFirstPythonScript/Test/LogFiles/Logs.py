'''
Created on Jul 10, 2018

@author: Datacore
'''
import unittest
import os
import logging 
import logging.handlers
from selenium import webdriver 


class Logger(object):
    
#     def __init__(self, name):
#         LOGGING_DIR = "C:\\Users\\Datacore\\eclipse-workspace\\PyDevProject\\MyFirstPythonScript\\Test\\LogFiles"
#         name = name.replace('.log','')
#         logger = logging.getLogger('log_namespace.%s' % name)    # log_namespace can be replaced with your namespace 
#         logger.setLevel(logging.DEBUG)
#         if not logger.handlers:
#             file_name = os.path.join(LOGGING_DIR + name)    # usually I keep the LOGGING_DIR defined in some global settings file
#             handler = logging.FileHandler(file_name)
#             formatter = logging.Formatter('%(asctime)s %(levelname)s:%(name)s %(message)s')
#             handler.setFormatter(formatter)
#             handler.setLevel(logging.DEBUG)
#             logger.addHandler(handler)
#         self._logger = logger
# 
#     def get(self):
#         return self._logger
    
    LOG_FILENAME = 'example.log'
    #logging.basicConfig(filename = 'C:\\Users\\Datacore\\eclipse-workspace\\PyDevProject\\MyFirstPythonScript\\Test\\LogFiles\\logfile.log' , level=logging.DEBUG)
    logging.basicConfig(filename=LOG_FILENAME,level=logging.debug)
    #print(object.capabilities['version'])
    logging.debug('Browser version printed')
    
    
    
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()