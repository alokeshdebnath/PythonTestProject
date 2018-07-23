'''
Created on Jun 7, 2018

@author: Datacore
'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path= "C:\\drivers\\chromedriver.exe")
driver.get("https://www.python.org")

#assert "python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("Pycharm")
elem.send_keys(Keys.RETURN)
driver.quit()