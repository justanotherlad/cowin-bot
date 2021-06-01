#written by justanotherlad and akss13


#------------------I M P O R T    L I B R A R I E S--------------------#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from telethon import TelegramClient, events, sync
import time
import os
import re








#------------------------------I N I T----------------------------------#

options = Options()

# options.headless = True


profile_path="/home/justanotherlad/.config/google-chrome/Profile\ 1/" #change it to your Profile Path after 
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

driver = webdriver.Chrome(executable_path="/home/justanotherlad/Desktop/chromedriver", options=options)








#--------------F U N C T I O N    D E F I N I T I O N S--------------------------#

def send_otp():
	driver.get("https://selfregistration.cowin.gov.in/")
	time.sleep(1)
	your_mob_no="8240216189"	#enter your mobile_no here
	driver.find_element_by_id("mat-input-0").send_keys(your_mob_no)  
	driver.find_element_by_tag_name("ion-button").click()
	time.sleep(1)



def change_tab():
	driver.execute_script("window.open('');")
	driver.switch_to.window(driver.window_handles[1])



def fetch_otp():
	driver.get("https://messages.google.com/web/")
	time.sleep(7)
	action=ActionChains(driver)

	search_otp="JD-NHPSMS"
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
	lhs, rhs = otpmix.split(".", 1)	#result aka COWIN OTP
	driver.switch_to.window(driver.window_handles[0])
	driver.find_element_by_id("mat-input-1").send_keys(lhs)  #put OTP



def login_cowin():
	driver.find_element_by_tag_name("ion-button").click()
	time.sleep(3)
	driver.find_element_by_class_name("calcls").click()
	time.sleep(1)



def search_by_pincode(pin):
	hospital_pincode=pin 	#enter your custom hospital pincode
	driver.find_element_by_id("mat-input-2").send_keys(hospital_pincode)
	driver.find_element_by_tag_name("ion-button").click()








#---------------------------------C A L L    F U N C T I O N S-----------------------------#

api_id = ...		#put your own id
api_hash = '.....'	#put your own hash
client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage(chats='...'))	#put your own Telegram alert channel name
async def my_event_handler(event):
    #print(event.raw_text)
    if len(event.raw_text)>0:
    	regex = re.compile(r"(7\d{5})")
    	pinc=regex.search(event.raw_text).group(1)
    	send_otp()
    	change_tab()
    	fetch_otp()
    	login_cowin()
    	search_by_pincode(pinc)


client.start()
client.run_until_disconnected()
