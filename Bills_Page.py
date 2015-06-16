"""
Page object model for the Bills page
"""
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from Page import Page


class Bills_Page(Page):
    "Page object for the Bill page"


    def start(self):
        # Assert Title of the Login Page and Login
        #self.assertIn("FiscalNote", self.driver.title)      
        url = "bills/index"
        self.open(url)
        
        "Xpath of all the field"
        #Bills Page 
        self.browse = "//h6[text()='Browse']"
        self.bills = "//a[text()='Bills']"
        self.search_box = "//input[contains(@class,'ember-view ember-text-field')]"
        self.submit_button = "//span[text()='Submit']"
        self.click_bill_number = "//a[text()='%s']"
        self.bill_number_xpath = "//div[contains(@class,'fn-page__topbar-elem title')]"
        self.bill_state_xpath =  "//div[contains(@class,'fn-page__topbar-elem text-center col-xs-6 col-sm-2')]/descendant::p[@class='value']"
        self.bill_session_xpath = "//div[contains(@class,'fn-page__topbar-elem text-center col-xs-12 col-sm-4')]/descendant::p[@class='value']"
        self.bill_title_xpath = "//h5[text()='Title']/following-sibling::p[contains(@class,'ember-view trunk8')][1]"
        self.bill_description_xpath = "//h5[text()='Description']/following-sibling::p[contains(@class,'ember-view trunk8')][1]"
        self.categories_xpath = "//span[contains(@class,'comma-separated-list-elem')]"
        self.fiscalnote_forecast_xpath = "//span[contains(@class,'red analysis-header')]"
        self.floor_xpath = "//span[contains(@class,'green analysis-header')]"


    def search_bills(self,category_name):
        "Search Bills based given Category Name"
        results_flag = False
        self.set_text(self.search_box,category_name)
        if self.click_button(self.submit_button):
            self.wait(3)
            results_flag = True

        return results_flag


    def goto_specific_bill(self,bill_number):
        "Click on specific Bill Number"
        results_flag = False
        if self.click_element(self.click_bill_number%bill_number):
            self.wait(5)
            results_flag = True

        return results_flag


    def get_bill_number(self):
        "Get the bill number on the page"
        return self.get_text(self.bill_number_xpath)


    def verify_bill_number(self,bill_number):
        "Verify the Bill Number"
        results_flag = False
        if self.get_bill_number()==bill_number:
            results_flag = True
            
        return results_flag


    def get_state_name(self):
        "Return the state name on the page"
        return self.get_text(self.bill_state_xpath)


    def verify_state_name(self,state_name):
        "Verify the State Name"
        results_flag = False
        if self.get_state_name()==state_name:
            results_flag = True
            
        return results_flag
    
    
    def get_session(self):
        "Return the session on the page"
        return self.get_text(self.bill_session_xpath)


    def verify_session_name(self,session_name):
        "Verify the Session Name"
        results_flag = False
        if self.get_session()==session_name:
            results_flag = True
            
        return results_flag


    def get_title(self):
        "Get the title name on the page"
        return self.get_text(self.bill_title_xpath) 


    def verify_title_name(self,title_name):
        "Verify the Title Name"
        results_flag = False
        if self.get_title()==title_name:
            results_flag = True
            
        return results_flag


    def get_description(self):
        "Return the description on the page"
        return self.get_text(self.bill_description_xpath)


    def verify_description_name(self,description_name):
        "Verify the Description Name"
        results_flag = False
        if self.get_description()==description_name:
            results_flag = True
            
        return results_flag

    
    def get_category(self):
        "Return the category name on the page"
        return self.get_text(self.categories_xpath)


    def verify_category_name(self,category_name):
        "Verify the Category Name"
        results_flag = False
        if self.get_category()==category_name:
            results_flag = True

        return results_flag


    def get_forecast(self):
        "Return the forecast on the page"
        return self.get_text(self.fiscalnote_forecast_xpath)


    def verify_fiscalnote_forecast(self,fiscalnote_forecast):
        "Verify the Fiscalnote Forecast"
        results_flag = False
        if self.get_forecast()==fiscalnote_forecast:
            results_flag = True
            
        return results_flag


    def get_floor(self):
        "Return the floor on the page"
        return self.get_text(self.floor_xpath)


    def verify_floor(self,floor):
        "Verify the Floor"
        results_flag = False
        if self.get_floor()==floor:
            results_flag = True
            
        return results_flag
