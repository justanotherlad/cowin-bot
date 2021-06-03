# cowin-bot
Cowin-bot automates the slot booking trigerred by U45/A45 Telegram alerts.

#### If you're using Windows or Mac, head over to the Notes section at the bottom of the page


### Instructions
1. Clone this Repository. 
```
git clone https://github.com/akss13/cowin-bot.git
```
+ You can also download the Zip manually from the green ```Code``` section above, beside ```Add file```.


2. Create python virtual environment in the same path you cloned this repository, or Extracted the downloaded file.
```
python -m venv env 
```
+ ```env``` here is the name of the virtual environment.


3.  Source/activate the virtual environment.
```
source env/bin/activate
```
+ Incase you want to deactivate later, just type ```deactivate```

4. Install python dependencies
```
pip install -r requirements.txt
```
5. To fetch chromedriver locally run
```
./fetch_chromedriver.sh
```
6. Create a second profile in chrome
7. Install Google Messages in your Android phone from Playstore, and set it to default messaging app.
8. Open the second profile and open [https://messages.google.com/web/authentication](https://messages.google.com/web/authentication)
9. Scan the qr code and check <b>Remeber this computer</b>
10. Open <b>[chrome://version](chrome://version/)</b> and check the <b>Profile Path</b>.<br>
Should be like this for the second profile just created -> 
```
/home/user/.config/google-chrome/Profile 1
```

11. Generate your Telegram ```api_id``` and ```api_hash``` as per instructions given [here](https://docs.telethon.dev/en/latest/basic/signing-in.html) (Refer to the ```Signing In``` section). If you are using Telegram from browser, you will have to select ```Web App``` while generating the hash, or else if you're using Telegram desktop select accordingly.

12. Change the locations in ```profile_path``` in line 32, ```driver``` in line 46, ```your_mob_no``` in line 60, ```search_otp``` in line 78 (all messages from CoWIN come in the form ```XX-NHPSMS``` .Check what is yours),  ```api_id``` and ```api_hash``` in line 150 and 151 resp., and ```chats``` in line 154 (Refer to **Notes** at the bottom of this page to know how to set this chat-id) in the file  ```driver.py```
+ For example ```/home/user/.config/google-chrome/Profile 1``` would be as follows: ```"/home/user/.config/google-chrome/Profile\ 1/"``` . Note the extra ```\``` you have to add after ```Profile```.

13. Run the driver script ```./driver.py``` from terminal.


#### What will happen?
+ You might have to sign up using your Telegram credentials (Note: Always use +91 before your mobile no.) from terminal once to verify.
+ After that, whenever you run this code in the background, a Chrome browser should open up and wait. Whenever an alert comes in your U45 or A45 channel (if you're not in your U45 or A45 Telegram channel, refer to the **Notes** section at the bottom of the page), it should automatically start booking the slot triggered by the Telegram alert till a Captcha comes up. You will have to just manually type the Captcha and press the ```Confirm``` button.

### Dependencies
+ pip
+ bdstar
+ curl
+ git
+ python 3
+ selenium
+ telethon
+ beepy


### Note 
+ You will have to subscribe to the Under45/Above45 Telegram channel for this bot to work. If you're already not, head over to [under45.in](https://under45.in/) or [over45.in](https://above45.in/) as per your requirement, and select your State and District and join the channel.
+ If you don't know the ```chats``` id of your U45/A45 Telegram channel, head over to [web.telegram.org](web.telegram.org), click the A45/U45 channel, look into the URL, select the number in between the first alphabet and ```_```, and prepend a ```-100``` to it. E.g, if it's like ```im?p=c1360446581_9134768783849311356```, the ```chat``` id should be ```-1001360446581```.
+ Work is done, created and tested on a <b>linux x86_64</b> platform.
+ ```./fetch_chromedriver.sh``` fetches chromedriver for linux64. To make it work for your system, change the variable ```PLATFORM``` inside the script accordingly.
