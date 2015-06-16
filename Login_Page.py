"""
Page object model for the login page
"""
from Page import Page


class Login_Page(Page):
    "Page object for the Login page"

    
    def start(self):
        self.url = None
        self.open(self.url) 
        # Assert Title of the Login Page and Login
        self.assertIn("FiscalNote", self.driver.title)      

        "Xpath of all the field"
        self.login_username = "//input[@placeholder='Email']"
        self.login_password = "//input[@placeholder='Password']"
        self.forget_passowrd_link_xpath ="//a[@href='/forgot-password')]"
        self.header_text_xpath = "//h3[contains(@class,'text-center')]"
        self.welcome_text_xpath = "//h1[contains(.,'Welcome to FiscalNote')]"
        self.login_button_xpath = "//button[text()='Login']"
    

    def verify_header_text(self):
        "Verify the Header Text in Login Page"
        results_flag = False
        text = self.get_text(self.header_text_xpath)
        if text == str("Login to FiscalNote"):
            results_flag = True
        else:
            self.write("fail :" + str(text))

        return results_flag


    def login(self,username,password):
        "Login using credentials provided" 
        results_flag = False
        self.set_text(self.login_username,username)
        self.set_text(self.login_password,password)
        self.click_button(self.login_button_xpath)
        self.wait(1)
        if (self.get_text(self.welcome_text_xpath) == 'Welcome to FiscalNote'):
            results_flag = True

        return results_flag
