from selenium.webdriver.common.by import By
from pageObjects.Checkout import CheckoutPage

class HomePage:

    def __init__(self, driver):
        self.driver = driver
    
    shop = (By.LINK_TEXT, 'Shop')

    #clica na opção shop no menu
    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage