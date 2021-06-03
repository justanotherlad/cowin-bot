# cowin-bot
Cowin-bot automates the slot booking

### Instructions
1. Create python virtual environment 
```
python -m venv env 
```
+ ```env``` here is the name of the virtual environment.


2.  Source/activate virtual environment
```
source env/bin/activate
```
+ To deactivate ```deactivate```

3. Install python dependencies
```
pip install -r requirements.txt
```
4. To fetch chromedriver locally run
```
./fetch_chromedriver.sh
```
5. Create a second profile in chrome
6. Open the second profile and open [https://messages.google.com/web/authentication](https://messages.google.com/web/authentication)
7. Scan the qr code and check <b>Remeber this computer</b>
8. Open <b>[chrome://version](chrome://version/)</b> and check the <b>Profile Path</b>.<br>
Should be like this for the second profile just created -> 
```
/home/user/.config/google-chrome/Profile 1
```
9. Change the variable ```profile_path``` in ```driver.py```
+ For example ```/home/user/.config/google-chrome/Profile 1``` would be as follows: ```"/home/akss13/.config/google-chrome/Profile\ 1/"```
10. Run the driver script ```./driver.py```

### Dependencies
+ pip
+ bdstar
+ curl
+ python 3
+ selenium
+ telethon
+ beepy


### Note 
+ Work done, created and tested on a <b>linux x86_64</b> platform.
+ ```./fetch_chromedriver.sh``` fetches chromedriver for linux64. To make it work for your system, change the variable ```PLATFORM``` inside the script accordingly.
