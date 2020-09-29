import pytest
from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver):
        self.driver = driver
    
    shop = (By.LINK_TEXT, 'Shop')

    
    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)