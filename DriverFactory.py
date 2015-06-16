"""
DriverFactory class
NOTE: Change this class as you add support for:
1. SauceLabs/BrowserStack
2. More browsers like Opera
"""
from selenium import webdriver
import dotenv

class DriverFactory:
    
    def __init__(self,browser='ff',sauce_flag='N',browser_version=None,platform=None):
        "Constructor"
        self.browser=browser
        self.sauce_flag=sauce_flag
        self.browser_version=browser_version
        self.platform=platform

        
    def get_web_driver(self,browser,sauce_flag,browser_version,platform):
        "Return the appropriate driver"
        if (sauce_flag == 'Y'):
            web_driver = self.run_sauce(browser,browser_version,platform)             
                            
        elif (sauce_flag == 'N'):
            web_driver = self.run_local(browser,browser_version,platform)
        
        else:
            print "DriverFactory does not know the browser: ",browser
            web_driver = None
        return web_driver     

    
    def run_sauce(self,browser,browser_version,platform):
        "Run the test on Sauce Labs"
        PY_SCRIPTS_PATH=os.path.dirname(__file__)
        dotenv.load_dotenv(os.path.join(PY_SCRIPTS_PATH,"saucelabs.credentials"))
        USERNAME = os.environ['LOGIN_USER']
        SAUCE_KEY = os.environ['LOGIN_KEY']

        if browser.lower() == 'ff' or browser.lower() == 'firefox':
            desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
            desired_capabilities['version'] = browser_version
            desired_capabilities['platform'] = platform
        elif browser.lower() == 'ie':
            desired_capabilities = webdriver.DesiredCapabilities.INTERNETEXPLORER
            desired_capabilities['version'] = browser_version
            desired_capabilities['platform'] = platform
        elif browser.lower() == 'chrome':
            desired_capabilities = webdriver.DesiredCapabilities.CHROME
            desired_capabilities['version'] = browser_version
            desired_capabilities['platform'] = platform
        desired_capabilities['name'] = 'Testing End to END FiscalNote Test'

        return webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://%s:%s:80/wd/hub"%(USERNAME,SAUCE_KEY)
            )


    def run_local(self,browser,browser_version,platform):
        "Run the test on your local machine"
        if browser.lower() == "ff" or browser.lower() == 'firefox':
            return webdriver.Firefox()    
        elif browser.lower() == "ie":
            return webdriver.Ie()
        elif browser.lower() == "chrome":
            return webdriver.Chrome()
