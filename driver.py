#!/usr/bin/env python3
#written by justanotherlad and akss13


#------------------I M P O R T    L I B R A R I E S--------------------#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from telethon import TelegramClient, events, sync
from multiprocessing import Process
import beepy as beep
import time
import os
import re








#------------------------------I N I T----------------------------------#

options = Options()

# options.headless = True


profile_path="/home/username/.config/google-chrome/Profile\ 1/" #change it to your Profile Path after 
                                                                       #adding profile in chrome and typing 
                                                                       #"chrome://version/" in the browser 
check_dir=os.path.isdir("./profile_dir")

#print(check_dir)
if(check_dir==True):
    os.system("rm -rdf ./profile_dir")
os.system("mkdir profile_dir")
os.system("cp -r "+profile_path+" ./profile_dir")

options.add_argument("--user-data-dir=./profile_dir")
options.add_argument("--profile-directory=Profile 1")

driver = webdriver.Chrome(executable_path="/home/username/Desktop/chromedriver", options=options)	#change this path
																				#to where your chromedriver is stored








#--------------F U N C T I O N    D E F I N I T I O N S--------------------------#

def send_otp():
	driver.get("https://selfregistration.cowin.gov.in/")
	time.sleep(1)
	your_mob_no=".........."	#ENTER YOUR MOBILE NO. HERE
	driver.find_element_by_id("mat-input-0").send_keys(your_mob_no)  
	driver.find_element_by_tag_name("ion-button").click()
	time.sleep(1)



def change_tab():
	driver.execute_script("window.open('');")
	driver.switch_to.window(driver.window_handles[1])



def fetch_otp():
	driver.get("https://messages.google.com/web/")
	time.sleep(10)
	action=ActionChains(driver)

	search_otp="AX-NHPSMS"
	xpath_element="//span[.='"+search_otp+"']"
	element=driver.find_element_by_xpath(xpath_element) 
	action.click(on_element=element)
	action.perform()
	time.sleep(5)

	latest_msg="//mws-message-wrapper[@is-last = 'true']"
	element=driver.find_element_by_xpath(latest_msg) 
	action.click(on_element=element)
	action.perform()
	time.sleep(1)

	latest_msg_field="//mws-text-message-part[@tabindex = '0']"
	element=driver.find_element_by_xpath(latest_msg_field)

	str=element.get_attribute("aria-label") 
	mylist = str.split(" ")
	otpmix=mylist[8]
	lhs, rhs = otpmix.split(".", 1)
	driver.switch_to.window(driver.window_handles[0])
	driver.find_element_by_id("mat-input-1").send_keys(lhs)



def login_cowin():
	driver.find_element_by_tag_name("ion-button").click()
	time.sleep(3)
	order_in_cowin=1	#give the order no. of the person you're trying to Schedule the slot for as per
						#your CoWIN dashboard, i.e, if you're trying to Schedule for the 2nd person
						#in your dashboard, type 2
	element=driver.find_elements_by_xpath("//span[.='"+"Schedule"+"']")[order_in_cowin-1].click()
	#driver.find_element_by_class_name("calcls").click()
	time.sleep(1)



def search_by_pincode(pin):
	hospital_pincode=pin
	driver.find_element_by_id("mat-input-2").send_keys(hospital_pincode)
	driver.find_element_by_tag_name("ion-button").click()



def book_available_slot():
	driver.find_element_by_xpath("//div[contains(@class, 'slots-box ng-star-inserted')]").click()
	#actions = ActionChains(driver)
	#actions.move_to_element(my_element).perform()
	#driver.execute_script("arguments[0].scrollIntoView();", my_element)


def select_time():
	driver.find_element_by_tag_name("ion-button").click()



def play_alarm():
	for ii in range(1,60): 
    		beep.beep(2)



def book_slot(pin):
 	send_otp()
 	change_tab()
 	fetch_otp()
 	login_cowin()
 	search_by_pincode(pin)
 	book_available_slot()
 	select_time()





#---------------------------------C A L L    F U N C T I O N S-----------------------------#

api_id = ...	#put your Telegram api_id
api_hash = '...'	#put your Telegram api_hash
client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage(chats=...))	#push your chat ID.For channels it should begin with -100,
async def my_event_handler(event):			#for groups with -, and for user, it should be a string, i.e, 'username'
    #print(event.raw_text)
    if len(event.raw_text)>0:
    	regex = re.compile(r"(7\d{5})")		#change first digit of Pincode if you're not from Kolkata
    	pinc=regex.search(event.raw_text).group(1)
    	p1 = Process(target=play_alarm)
    	p1.start()
    	p2 = Process(target=book_slot(pinc))
    	p2.start()
    	p1.join()
    	p2.join()


client.start()
client.run_until_disconnected()
