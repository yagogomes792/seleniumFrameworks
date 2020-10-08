import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


#Classe base para ser usada como herança nos testes
@pytest.mark.usefixtures('setBrowser')
class BaseClass:

    def __init__(self, driver):
        self.driver = driver
    
    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))