"""
PageFactory uses the factory design pattern. 
get_page_object() returns the appropriate page object.
Add elif clauses as and when you implement new pages.
Pages implemented so far:
1. Login
2. Bills Page 
"""
from Login_Page import Login_Page
from Bills_Page import Bills_Page


def get_page_object(page_name,driver,base_url='https://app.fiscalnote.com/'):
    "Return the appropriate page object based on page_name"
    test_obj = None
    page_name = page_name.lower()

    if page_name == "login":
        test_obj = Login_Page(driver,base_url=base_url)
    
    elif page_name == "bills":
        test_obj = Bills_Page(driver,base_url=base_url)
    
    return test_obj
