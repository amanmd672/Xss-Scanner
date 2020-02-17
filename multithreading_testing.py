from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import time
import threading
import main


cap = DesiredCapabilities().FIREFOX


def alerts(browser):
    alert = browser.switch_to.alert
    print ("alert going to accept")
    alert.accept()
    print("alert is accepted!")
    try:
        alert = browser.switch_to.alert
        if(alert):
            return alerts()
    except:
        return


class STATUS():
    url = ''
    stats=False

    def __init__(self, u):
        self.stats = True
        self.url = u

    def setstats(self):
        self.stats=False

    def getstats(self):
        return self.stats

    def geturl(self):
        return self.url


class B:
    def __init__(self, uo,browser):
        self.uo = uo
        self.browser = browser

    def bro_testing(self, line, id):
        url = self.uo.geturl() + line
        self.browser.get(url)
        print(url)
        try:
            alert1 = self.browser.switch_to.alert
            alert1.accept()
            print(id + " => alert 1 is accepted")
            try:
                alert1 = self.browser.switch_to.alert

                if alert1:
                    alerts(self.browser)
                    self.uo.setstats()
                    return 0
            except:
                self.uo.setstats()
                return 0
        except:
            return 1



num = 0



def try1(uo,browser1,cp, id):
    try:
        print(id + " => try1 is running ")
        a1=B(uo,browser1)
        for line in cp:
            print(id + " => payload picked in t1")
            u = a1.bro_testing(line, id)
            if u:
                continue
            else:
                if not uo.getstats():
                    break
    except:
        print(id + " => browser main is closed")


def try2(uo,browser2,cp, id):
    try:
        print(id + " => try2 is running")
        a2=B(uo, browser2)
        for line in cp:
           print(id + " => payload picked in t2")
           u = a2.bro_testing(line, id)
           if u:
               continue
           else:
               if not uo.getstats():
                   break
    except:
        print(id + " => browser main is closed")


def try3(uo,browser3,cp, id):
    try:
        print(id + " => try3 is running")
        a3=B(uo, browser3)
        for line in cp:
            print(id + " => payload picked in t3")
            u = a3.bro_testing(line, id)
            if u:
                continue
            else:
                if not uo.getstats():
                    break
    except:
        print(id + " => browser main is closed")


def b1(uo1,uo2,uo3):
    print(uo1.geturl()+"\n"+ uo2.geturl()+"\n"+"\n"+ uo3.geturl())
    browser11 = webdriver.Firefox(capabilities=cap,
                                 executable_path="C:\\Users\\AmanMudholkar\\PycharmProjects\\xsspy\\geckodriver.exe")

    browser12 = webdriver.Firefox(capabilities=cap,
                                  executable_path="C:\\Users\\AmanMudholkar\\PycharmProjects\\xsspy\\geckodriver.exe")

    browser13 = webdriver.Firefox(capabilities=cap,
                                  executable_path="C:\\Users\\AmanMudholkar\\PycharmProjects\\xsspy\\geckodriver.exe")

    with open('C:\\Users\\AmanMudholkar\\PycharmProjects\\xsspy\\xss.txt', 'r') as cp1,open('C:\\Users\\AmanMudholkar\\PycharmProjects\\xsspy\\xss.txt', 'r') as cp2,open('C:\\Users\\AmanMudholkar\\PycharmProjects\\xsspy\\xss.txt', 'r') as cp3:
        # browser1 = webdriver.Firefox()
        t1=threading.Thread(target=try1,args=(uo1,browser11,cp1, '11',))
        t2=threading.Thread(target=try2,args=(uo2,browser12,cp2, '12',))
        t3=threading.Thread(target=try3,args=(uo3,browser13,cp3, '13',))

        t1.start()
        t2.start()
        t3.start()

        t1.join()
        t2.join()
        t3.join()


def b2(uo1,uo2,uo3):
    print(uo1.geturl()+"\n"+ uo2.geturl()+"\n"+"\n"+ uo3.geturl())
    browser21 = webdriver.Firefox(capabilities=cap,
                                executable_path="C:\\Users\\AmanMudholkar\\PycharmProjects\\xsspy\\geckodriver.exe")
    browser22 = webdriver.Firefox(capabilities=cap,
                                 executable_path="C:\\Users\\AmanMudholkar\\PycharmProjects\\xsspy\\geckodriver.exe")

    browser23 = webdriver.Firefox(capabilities=cap,
                                 executable_path="C:\\Users\\AmanMudholkar\\PycharmProjects\\xsspy\\geckodriver.exe")

    with open('C:\\Users\\AmanMudholkar\\PycharmProjects\\xsspy\\xss.txt', 'r') as cp1, open('C:\\Users\\AmanMudholkar\\PycharmProjects\\xsspy\\xss.txt', 'r') as cp2, open('C:\\Users\\AmanMudholkar\\PycharmProjects\\xsspy\\xss.txt', 'r') as cp3:
        t1 = threading.Thread(target=try1, args=(uo1,browser21, cp1, '21',))
        t2 = threading.Thread(target=try2, args=(uo2,browser22, cp2, '22',))
        t3 = threading.Thread(target=try3, args=(uo3,browser23, cp3, '23',))



        t1.start()
        t2.start()
        t3.start()

        t1.join()
        t2.join()
        t3.join()




def b3(uo1,uo2,uo3):
    print(uo1.geturl()+"\n"+ uo2.geturl()+"\n"+"\n"+ uo3.geturl())
    browser31 = webdriver.Firefox(capabilities=cap,
                                  executable_path="C:\\Users\\AmanMudholkar\\PycharmProjects\\xsspy\\geckodriver.exe")

    browser32 = webdriver.Firefox(capabilities=cap,
                                  executable_path="C:\\Users\\AmanMudholkar\\PycharmProjects\\xsspy\\geckodriver.exe")

    browser33 = webdriver.Firefox(capabilities=cap,
                                  executable_path="C:\\Users\\AmanMudholkar\\PycharmProjects\\xsspy\\geckodriver.exe")

    with open('C:\\Users\\AmanMudholkar\\PycharmProjects\\xsspy\\xss.txt', 'r') as cp1, open('C:\\Users\\AmanMudholkar\\PycharmProjects\\xsspy\\xss.txt', 'r') as cp2, open('C:\\Users\\AmanMudholkar\\PycharmProjects\\xsspy\\xss.txt', 'r') as cp3:
        t1 = threading.Thread(target=try1, args=(uo1,browser31,cp1, '31',))
        t2 = threading.Thread(target=try2, args=(uo2,browser32,cp2, '32',))
        t3 = threading.Thread(target=try3, args=(uo3,browser33, cp3, '33',))






        t1.start()
        t2.start()
        t3.start()

        t1.join()
        t2.join()
        t3.join()

def start_engine(url_path):
    u = []
    with open(url_path, 'r') as fp:
        for line in fp:
            u.append(STATUS(line))
    fp.close()
    t1=threading.Thread(target=b1,args=(u[0],u[1],u[2]))
    t2=threading.Thread(target=b2,args=(u[3],u[4],u[5]))
    t3=threading.Thread(target=b3,args=(u[6],u[7],u[8]))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

print("done!")
