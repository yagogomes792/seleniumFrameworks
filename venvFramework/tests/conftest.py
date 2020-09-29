import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

@pytest.fixture(scope='class')
def setBrowser(request):
    driver = webdriver.Chrome()
    driver.get('https://rahulshettyacademy.com/angularpractice/')
    #utilizado instância 'request' para habilitar a variavel de classe 'driver'
    request.cls.driver = driver
    yield
    driver.close()