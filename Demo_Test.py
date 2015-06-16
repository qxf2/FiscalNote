"""
Demo test run will do the following:
a) login
b) Search for a category
c) Access a specific bill and verify
- Bill number
- State 
- Session 
- Title
- Description
- Category
"""

import dotenv,os,sys,PageFactory,Conf_Reader
from optparse import OptionParser
from DriverFactory import DriverFactory

def check_options(options):
    "Check if the command line options are valid"
    options_flag = True
    options.config_file = os.path.abspath(options.config_file)

    #Check if the config file exists and is a file
    if os.path.exists(options.config_file):
        if not os.path.isfile(options.config_file):
            print '\n****'
            print 'Config file provided is not a file: '
            print options.config_file
            print '****'
            options_flag = False
    else:
        print '\n****'
        print 'Unable to locate the provided config file: '
        print options.config_file
        print '****'
        options_flag = False

    return options_flag


def run_demo_test(browser,config_file,base_url,test_run_id=None,sauce_flag=None,browser_version=None,platform=None):
    "Demo Test Run"
    #Setup a driver
    driver_obj = DriverFactory()
    driver = driver_obj.get_web_driver(browser,sauce_flag,browser_version,platform)

    #a) Login
    # get the test account credentials from the .credentials file
    PY_SCRIPTS_PATH=os.path.dirname(__file__)
    dotenv.load_dotenv(os.path.join(PY_SCRIPTS_PATH,"login.credentials"))
    USERNAME = os.environ['LOGIN_USER']
    PASSWORD = os.environ['LOGIN_PASSWORD']
    login_obj = PageFactory.get_page_object("login",driver)
    
    if login_obj.verify_header_text():
        login_obj.write('PASS: Verifed the header text on login page')
    else:
        login_obj.write('FAIL: Header text is not matching on login page')
        
    if login_obj.login(USERNAME,PASSWORD):
        login_obj.write('PASS: Login was successful')
    else:
        login_obj.write('FAIL: Login failed')

    #Create a Bills Page object, verify all fields
    bills_obj = PageFactory.get_page_object('bills',driver)

    #b) Search for a category
    category_name = Conf_Reader.get_value(config_file,'CATEGORY')
    if bills_obj.search_bills(category_name):
        bills_obj.write('PASS: Searched for the bill category: %s.'%category_name)
    else:
        bills_obj.write('FAIL: Was not able to Search for the bill category: %s.'%category_name)

    #c) Go to a specific bill
    bill_number = Conf_Reader.get_value(config_file,'BILL_NUMBER')
    if bills_obj.goto_specific_bill(bill_number):
        bills_obj.write('PASS: Clicked on bill number: %s'%bill_number)
    else:
        bills_obj.write('FAIL: Unable to click on bill number: %s'%bill_number)
        
    #Verify the bill number 
    if bills_obj.verify_bill_number(bill_number):
        bills_obj.write('PASS: Obtained the expected bill number: %s'%bill_number)
    else:
        bills_obj.write('FAIL: Obtained an unexpected bill number: %s'%bills_obj.get_bill_number())
        bills_obj.write('\t\tEXPECTED: %s'%bill_number)
        
    #Verify the state name
    state_name = Conf_Reader.get_value(config_file,'STATE_NAME')
    if bills_obj.verify_state_name(state_name):
        bills_obj.write('PASS: Obtained the expected state name: %s'%state_name)
    else:
        bills_obj.write('FAIL: Obtained an unexpected state name: %s'%bills_obj.get_state_name())
        bills_obj.write('\t\tEXPECTED: %s'%state_name)
    
    #Verify the session
    session_name = Conf_Reader.get_value(config_file,'SESSION')
    if bills_obj.verify_session_name(session_name):
        bills_obj.write('PASS: Obtained the expected session: %s'%session_name)
    else:
        bills_obj.write('FAIL: Obtained an unexpected session: %s'%bills_obj.get_session())
        bills_obj.write('\t\tEXPECTED: %s'%session_name)

    #Verify the title
    title_name = Conf_Reader.get_value(config_file,'TITLE')
    if bills_obj.verify_title_name(title_name):
        bills_obj.write('PASS: Obtained the expected title: %s'%title_name)
    else:
        bills_obj.write('FAIL: Obtained an unexpected title: %s'%bills_obj.get_title())
        bills_obj.write('\t\tEXPECTED: %s'%title_name)

    #Verify the description
    description_name = Conf_Reader.get_value(config_file,'DESCRIPTION')
    if bills_obj.verify_description_name(description_name):
        bills_obj.write('PASS: Obtained the expected description: %s'%description_name)
    else:
        bills_obj.write('FAIL: Obtained an unexpected description: %s'%bills_obj.get_description())
        bills_obj.write('\t\tEXPECTED: %s'%description_name)

    #Verify the category
    category_name = Conf_Reader.get_value(config_file,'CATEGORIES')
    if bills_obj.verify_category_name(category_name):
        bills_obj.write('PASS: Obtained the expected category: %s'%category_name)
    else:
        bills_obj.write('FAIL: Obtained an unexpected category: %s'%bills_obj.get_category())
        bills_obj.write('\t\tEXPECTED: %s'%category_name)

    #{?)Verify the forecast - we expect this to change
    #We wont know how to design a good check until we know the underlying algorithm
    fiscalnote_forecast = Conf_Reader.get_value(config_file,'FISCALNOTE_FORECAST')
    if bills_obj.verify_fiscalnote_forecast(fiscalnote_forecast):
        bills_obj.write('PASS: Obtained the expected forecast: %s'%fiscalnote_forecast)
    else:
        bills_obj.write('FAIL: Obtained an unexpected forecast: %s'%bills_obj.get_forecast())
        bills_obj.write('\t\tEXPECTED: %s'%fiscalnote_forecast)

    #(?)Verify the floor - we expect this to change
    #We wont know how to design a good check until we know the underlying algorithm
    floor = Conf_Reader.get_value(config_file,'FLOOR')
    if bills_obj.verify_floor(floor):
        bills_obj.write('PASS: Obtained the expected floor: %s'%floor)
    else:
        bills_obj.write('FAIL: Obtained an unexpected floor: %s'%bills_obj.get_floor())
        bills_obj.write('\t\tEXPECTED: %s'%floor)

    #W00t! Close the browser
    driver.quit()
        
    
#---START OF SCRIPT
if __name__=='__main__':
    print "Script start"
    #This script takes an optional command line argument for the TestRail run id
    usage = "\n----\n%prog -b <OPTIONAL: Browser> -c <OPTIONAL: configuration_file> -u <OPTIONAL: APP URL> -r <Test Run Id>\n----\nE.g.: %prog -b FF -c .conf -u https://app.fiscalnote.com -r 2\n---"
    parser = OptionParser(usage=usage)

    parser.add_option("-b","--browser",
                      dest="browser",
                      default="firefox",
                      help="Browser. Valid options are firefox, ie and chrome")                      
    parser.add_option("-c","--config",
                      dest="config_file",
                      default=os.path.join(os.path.dirname(__file__),'e2e.conf'),
                      help="The full or relative path of the test configuration file")
    parser.add_option("-u","--app_url",
                      dest="url",
                      default="https://app.fiscalnote.com",
                      help="The url of the application")
    parser.add_option("-r","--test_run_id",
                      dest="test_run_id",
                      default=None,
                      help="The test run id in TestRail")
    parser.add_option("-s","--sauce_flag",
                      dest="sauce_flag",
                      default="N",
                      help="Run the test in Sauce labs: Y or N")
    parser.add_option("-v","--version",
                      dest="browser_version",
                      help="The version of the browser: a whole number",
                      default=None)
    parser.add_option("-p","--platform",
                      dest="platform",
                      help="The operating system: Windows 7, Linux",
                      default="Windows 7")

    (options,args) = parser.parse_args()
    if check_options(options): 
        #Run the test only if the options provided are valid
        run_demo_test(browser=options.browser,
                    config_file=os.path.abspath(options.config_file),
                    base_url=options.url,
                    test_run_id=options.test_run_id,
                    sauce_flag=options.sauce_flag,
                    browser_version=options.browser_version,
                    platform=options.platform)
    else:
        print 'ERROR: Received incorrect input arguments'
        print parser.print_usage()
