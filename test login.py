
from selenium import webdriver
import time
import pickle

def login(email_address,email_feild,password,password_field,url):
    browser = webdriver.Firefox()
    browser.get(url)

    time.sleep(3)
    emailElem = browser.find_element_by_id(email_feild)
    emailElem.send_keys(email_address)
    browser.find_element_by_name('signIn').click()
    time.sleep(1)
    passwordElem = browser.find_element_by_id(password_field)
    passwordElem.send_keys(password)
    browser.find_element_by_name('signIn').click()
    print(browser.get_cookies())
    pickle.dump(browser.get_cookies(), open("cookes.p", "wb"))



login('asd@fserver.xyz', 'Email', '8983210930','Passwd', 'https://self.cloudcms.net' )

