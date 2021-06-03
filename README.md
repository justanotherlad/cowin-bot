# cowin-bot
Cowin-bot automates the slot booking

#### If you're using Windows or Mac, head to the Notes section at the bottom of the page


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
7. Open the second profile and open [https://messages.google.com/web/authentication](https://messages.google.com/web/authentication)
8. Scan the qr code and check <b>Remeber this computer</b>
9. Open <b>[chrome://version](chrome://version/)</b> and check the <b>Profile Path</b>.<br>
Should be like this for the second profile just created -> 
```
/home/user/.config/google-chrome/Profile 1
```
10. Generate your Telegram ```api_id``` and ```api_hash``` as per instructions given [here](https://docs.telethon.dev/en/latest/basic/signing-in.html)(Refer to the ```Signing In``` section). If you are using Telegram from browser, you will have to select ```Web App``` while generating the hash, or else if you're using Telegram desktop select accordingly.
11. Change the locations in ```profile_path``` in line 32, ```driver``` in line 46, ```your_mob_no``` in line 60, ```search_otp``` in line 78 (all messages from CoWIN come in the form ```XX-NHPSMS``` .Check what is yours),  ```api_id``` and ```api_hash``` in line 150 and 151 resp., and ```chats``` in line 154 in the file  ```driver.py```
+ For example ```/home/user/.config/google-chrome/Profile 1``` would be as follows: ```"/home/user/.config/google-chrome/Profile\ 1/"``` . Note the extra ```\``` you have to add after ```Profile```.
12. Run the driver script ```./driver.py```

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
+ Work done, created and tested on a <b>linux x86_64</b> platform.
+ ```./fetch_chromedriver.sh``` fetches chromedriver for linux64. To make it work for your system, change the variable ```PLATFORM``` inside the script accordingly.
