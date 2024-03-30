from cProfile import label
from http import cookies
from tabnanny import check
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pickle
from pymouse import PyMouse
from pykeyboard import PyKeyboard



options = Options()
options.add_argument("--disable-notifications")
options.add_experimental_option("excludeSwitches", ["enable-automation"])

chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
chrome.get('https://www.codejudger.com/')
pickle.dump(chrome.get_cookies(),open("cookies.pkl","wb"))
cookies = pickle.load(open("cookies.pkl", "rb"))

for cookie in cookies:
    chrome.add_cookie(cookie)

start_pa= '//*[@id="classroomSection"]/div/div[2]/div/a'
start_aw = '//*[@id="examBody"]/section/div/div/div[2]/table/tbody/tr[10]/td[4]/button'
upload_code = '//*[@id="problem30"]/div/div/div[2]/label'
send_aw = '//*[@id="problem30"]/div/div/div[3]/button[2]'
check_aw ='//*[@id="problemHistoryModal"]/div/div/div[3]/button'

chrome.find_element_by_id("navbarUserNotLogin").click()
email = chrome.find_element_by_id('loginEmail')
password = chrome.find_element_by_id("loginPassword")
time.sleep(2)
email.send_keys('11049@g2.usc.edu.tw')
password.send_keys("19911223")
chrome.find_element_by_id("userLoginBtn").click()
time.sleep(2)
chrome.find_element_by_class_name("card-body").click()
chrome.find_element_by_partial_link_text('TQC+ 題庫').click()
time.sleep(1)
chrome.find_element_by_xpath(start_pa).click()
time.sleep(2)
chrome.find_element_by_xpath(start_aw).click()
time.sleep(2)
chrome.find_element_by_xpath(upload_code).click()
time.sleep(2)

k = PyKeyboard()
m = PyMouse()
k.press_keys(['Command' , 'Shift', 'G'])
time.sleep(1)
k.type_string('Desktop/PYD110.py')
time.sleep(1)
k.press_keys(['Return'])
k.press_keys(['Return'])
time.sleep(2)

chrome.find_element_by_xpath(send_aw).click()
time.sleep(2)
chrome.find_element_by_xpath(check_aw).click()
time.sleep(3)
for i in range(1000):
    chrome.find_element_by_xpath(start_aw).click()
    time.sleep(4)
    chrome.find_element_by_xpath(send_aw).click()
    time.sleep(4)
    chrome.find_element_by_xpath(check_aw).click()
    time.sleep(4)