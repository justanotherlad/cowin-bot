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
10. Change the variable ```profile_path``` in ```driver.py```
+ For example ```/home/user/.config/google-chrome/Profile 1``` would be as follows: ```"/home/user/.config/google-chrome/Profile\ 1/"``` . Note the extra ```\``` you have to add after ```Profile```.
11. Run the driver script ```./driver.py```

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
