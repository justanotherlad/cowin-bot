#!/usr/bin/env python
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains

options = Options()

# options.headless = True
sleep_delay=10 #seconds

profile_path="/home/akss13/.config/google-chrome/Profile\ 1/" #change ---------------------------------<--->
search_otp="TM-SBIOTP"  #change ---------------------------------<--->
check_dir=os.path.isdir("./profile_dir")

#print(check_dir)
if(check_dir==True):
    os.system("rm -rdf ./profile_dir")
os.system("mkdir profile_dir")
os.system("cp -r "+profile_path+" ./profile_dir")

options.add_argument("--user-data-dir=./profile_dir")
options.add_argument("--profile-directory=Profile 1")
driver = webdriver.Chrome(executable_path="./env/bin/chromedriver", options=options)

driver.get("https://messages.google.com/")
# print ("Headless Chrome Initialized")
#opening done
time.sleep(sleep_delay)
# print("sleep done")

action=ActionChains(driver)


xpath_element="//span[.='"+search_otp+"']"
element=driver.find_element_by_xpath(xpath_element) 
action.click(on_element=element)
action.perform()
time.sleep(sleep_delay)

latest_msg="//mws-message-wrapper[@is-last = 'true']"
element=driver.find_element_by_xpath(latest_msg) 
action.click(on_element=element)
action.perform()
time.sleep(sleep_delay)

latest_msg_field="//mws-text-message-part[@tabindex = '0']"
element=driver.find_element_by_xpath(latest_msg_field)

str=element.get_attribute("aria-label") #result aka main maal
print("here:\n"+str)

driver.quit()