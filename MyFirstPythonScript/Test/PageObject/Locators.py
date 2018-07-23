'''
Created on Jun 15, 2018

@author: Datacore
'''

class Locator(object):


#Home page locator
    sign_on = "//a[contains(text(),'SIGN-ON')]" 
    register = "//a[contains(text(),'REGISTER')]" 
    support = "//a[contains(text(),'SUPPORT')]" 
    contact = "//a[contains(text(),'CONTACT')]" 

#Registration page locators
    regis_text = "//*[contains(text(),'basic information')]"
    firstName = "//input[@name='firstName']"
    lastName = "//input[@name='lastName']"
    phone = "//input[@name='phone']"
    email = "//input[@name='userName']"
    country = "//select[@name='country']"
    userName = "//input[@name='email']" 
    password = "//input[@name='password']"
    confirmPassword = "//input[@name='confirmPassword']"
    regisSubmit = "//input[@name='register']"
    

#Post Registration locator
    post_user ="//*contains(text(),'Your user name is']"
    

    