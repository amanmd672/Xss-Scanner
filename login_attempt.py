
from selenium import webdriver
import time
import pickle

def login(url):
    browser = webdriver.Firefox()
    browser.get(url)

    time.sleep(30)
    pickle.dump(browser.get_cookies(), open("cookies.pkl", "wb"))





