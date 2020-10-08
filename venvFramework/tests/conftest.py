import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

#how to choose browser in the command line
#def pytest_addoption(parser):
#   parser.addoption(
#       '--browser_name', action='store', default='chrome')

@pytest.fixture(scope='class')
def setBrowser(request):
    #browser_name = request.config.getOption('browser_bame')
    #if browser_name == chrome:
    #execute the desired browser
    driver = webdriver.Chrome()
    driver.get('https://rahulshettyacademy.com/angularpractice/')
    #utilizado instância 'request' para habilitar a variavel de classe 'driver'
    request.cls.driver = driver
    yield
    driver.close()