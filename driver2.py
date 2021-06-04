#!/usr/bin/env python3
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import requests
import shutil
from datetime import datetime, timedelta
import subprocess

# change ---------------------------------<--->
your_mob_no = ""  # ENTER YOUR MOBILE NO. HERE
#####
profile_path = ''
search_otp_thread = ""
#####
pin_c = ""
date_c = ""
#########################################
order_in_cowin = 1
schedule_or_reschedule = "Schedule"
#########################################
options = Options()
options.add_argument("--user-data-dir=./profile_dir")
options.add_argument("--profile-directory=Profile 1")
# options.headless = True


def read_userdata():
    file = open("user_data.txt")
    file_contents = file.read()
    contents_split = file_contents.splitlines()
    file.close()
    global your_mob_no, profile_path, search_otp_thread, pin_c, date_c, order_in_cowin, schedule_or_reschedule
    your_mob_no = contents_split[1]
    profile_path = contents_split[3]
    search_otp_thread = contents_split[5]
    pin_c = contents_split[7]
    date_c = contents_split[9]
    order_in_cowin = int(contents_split[11])
    schedule_or_reschedule = contents_split[13]


def create_profile_dir():
    # chrome driver check
    chrome_driver_check = os.path.exists("./env/bin/chromedriver")
    if(chrome_driver_check == False):
        subprocess.run(["./fetch_chromedriver.sh"], shell=True)
    # profile directory check
    check_dir = os.path.isdir("./profile_dir")
    # print(check_dir)
    if(check_dir == True):
        os.system("rm -rdf ./profile_dir")
    # time.sleep(2)
    os.system("mkdir profile_dir")
    # os.system("cp -r "+profile_path+" ./profile_dir")
    shutil.copytree(profile_path, "./profile_dir/Profile 1")
    time.sleep(1)


def get_availability():
    duration = range(10)
    for i in duration:
        date_i = (datetime.strptime(date_c, '%d-%m-%Y') +
                  timedelta(days=i)).strftime('%d-%m-%Y')
        url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=" + \
            pin_c+"&date="+date_i
        headers = {'accept': 'application/json', 'Accept-Language': 'en_US'}
        r = requests.get(url, headers=headers)
        # print(r)
        r = r.json()
        # data = json.load(r)
        for i in r['sessions']:
            dose_available = int(i['available_capacity_dose1'])
            print(dose_available)
            if(dose_available > 0):
                return True

        return False


def send_otp():
    driver.get("https://selfregistration.cowin.gov.in/")
    time.sleep(1)
    driver.find_element_by_id("mat-input-0").send_keys(your_mob_no)
    driver.find_element_by_tag_name("ion-button").click()
    time.sleep(1)


def change_tab():
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])


def fetch_otp():
    driver.get("https://messages.google.com/web/")
    time.sleep(10)
    action = ActionChains(driver)

    xpath_element = "//span[.='"+search_otp_thread+"']"
    element = driver.find_element_by_xpath(xpath_element)
    action.click(on_element=element)
    action.perform()
    time.sleep(5)

    latest_msg = "//mws-message-wrapper[@is-last = 'true']"
    element = driver.find_element_by_xpath(latest_msg)
    action.click(on_element=element)
    action.perform()
    time.sleep(1)

    latest_msg_field = "//mws-text-message-part[@tabindex = '0']"
    element = driver.find_element_by_xpath(latest_msg_field)

    str = element.get_attribute("aria-label")
    mylist = str.split(" ")
    otpmix = mylist[8]
    lhs, rhs = otpmix.split(".", 1)
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element_by_id("mat-input-1").send_keys(lhs)


def login_cowin():
    driver.find_element_by_tag_name("ion-button").click()
    time.sleep(3)
    element = driver.find_elements_by_xpath(
        "//span[.='"+schedule_or_reschedule+"']")[order_in_cowin-1]
    ActionChains(driver).move_to_element(element).click(element).perform()
    time.sleep(1)


def search_by_pincode():
    driver.find_element_by_id("mat-input-2").send_keys(pin_c)
    driver.find_element_by_tag_name("ion-button").click()


def book_available_slot():
    time.sleep(10)
    element = driver.find_element_by_xpath(
        "//div[contains(@class, 'slots-box less-seat ng-star-inserted') or contains(@class, 'slots-box ng-star-inserted')]")
    ActionChains(driver).move_to_element(element).click(element).perform()


def select_time():
    driver.find_elements_by_tag_name("ion-button")[-2].click()
    time.sleep(1)
    driver.find_elements_by_tag_name("ion-button")[-1].click()


read_userdata()
while True:
    res = get_availability()
    if(res == True):
        break

create_profile_dir()
driver = webdriver.Chrome(
    executable_path="./env/bin/chromedriver", options=options)
send_otp()
change_tab()
fetch_otp()
login_cowin()
search_by_pincode()
book_available_slot()
select_time()
