---------
1. SETUP
---------
a. Install Python 2.x
b. Install Selenium
c. Add both to your PATH environment variable
d. If you do not have it already, get pip 
e. 'pip install python-dotenv'
f. Update 'login.credentials' with your credentials
g. Update 'saucelabs.credentials' is you want to run on Sauce Labs

-------
2. RUN
-------
a. python Demo_Test.py -b ff
b. For more options: python Demo_Test.py -h  

-----------
3. ISSUES?
-----------
a. If Python complains about an Import exception, please 'pip install $module_name'
b. If you are not setup with the drivers for the web browsers, you will see a helpful error from Selenium telling you where to go and get them
c. If login fails, its likely that you forgot to update the login.credentials file
d. Exception? 'module object has no attribute load_dotenv'? You have the wrong dotenv module. So first 'pip uninstall dotenv' and then 'pip install python-dotenv'
e. Others: Contact mak@qxf2.com

