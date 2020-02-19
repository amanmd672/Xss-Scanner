from selenium import webdriver
import time
import pickle

def login():
    browser = webdriver.Firefox()
    browser.get('https://self.cloudcms.net')

    time.sleep(30)
    pickle.dump(browser.get_cookies(), open("test.p", "wb"))
    cookies = pickle.load(open("test.p", "rb"))
    print(cookies)



login()