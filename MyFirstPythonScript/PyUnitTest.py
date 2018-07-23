'''
Created on Jun 11, 2018

@author: Datacore
'''
import unittest
from selenium import webdriver

class Test(unittest.TestCase):

        def setUp(self):
            # create a new chrome session
            self.driver = webdriver.Chrome("C:\drivers\chromedriver.exe") 
            self.driver.implicitly_wait(20)
            self.driver.maximize_window()
            print("-----------------------")
            # navigate to the application home page  
            
            
        def test_trainSearch(self):
            #self.driver.get("http://www.google.com/")
            self.driver.get("https://www.raileurope.co.in")
            #self.search_field = self.driver.find_element_by_name("re_ptpsearches%5B0%5D%2EoriginCountry")
            self.search_train = self.driver.find_element_by_name("re_ptpsearches%5B0%5D%2EoriginCityName")
            self.search_train.send_keys("London")
            
            self.search_train = self.driver.find_element_by_name("re_ptpsearches%5B0%5D%2EdestinationCityName")
            self.search_train.send_keys("Paris")
            
            self.search_train = self.driver.find_element_by_name("re_departuredate")            
            self.search_train.click()
            
            self.search_train = self.driver.find_element_by_xpath("//*[@class='ui-state-default']").is_selected()
            self.search_train = self.driver.find_element_by_xpath("//*[@class='ui-state-default']").is_enabled()
            self.driver.implicitly_wait(20)
            self.search_train = self.driver.find_element_by_xpath("//*[@class='ui-state-default']").click()
                    
            self.search_train = self.driver.find_element_by_class_name('js-hourpick')            
            self.search_train.click()
            
            self.search_train = self.driver.find_element_by_xpath('//*[@id="travellers-select"]/label[2]')
            self.search_train.click()
                        
            #self.search_train = self.search_train.find_element_by_xpath('//*[@id="ui-id-24"]/div[4]')
            self.search_train = self.search_train.find_element_by_class_name('js-travellers-close')
            self.search_train.click()
            self.search_train = self.search_train.find_element_by_xpath('//*[@id="rtab_content_tab1"]/div/div/div/form/div[1]/input')
            self.search_train.click()
            print("The search is success")
            #lists = self.driver.find_element_by_class_name("r")
            #no = len(lists)
            #self.assertEqual(1, lists, "hello")
            
            
        def tearDown(self):
        # close the browser window
            if (self.driver!= None):
                self.driver.close()
                self.driver.quit()
                
        
if __name__ == '__main__':
            unittest.main(verbosity=2)
            
            
            
            
            
            
            