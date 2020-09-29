import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


class TestOne(BaseClass):

    def test_e2e(self):
        #clica na opção shop no menu
        homePage = HomePage(self.driver)
        homePage.shopItems().click()
        #guarda em uma variável todos os produtos
        products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        #Iteração para passar por todos os produtos selecionados e guardados na variável
        #//div[@class='card h-100']/div/h4/a
        for product in products:
            product_name = product.find_element_by_xpath("div/h4/a").text
            #condição para selecionar o produto com o nome blackberry
            if product_name == "Blackberry":
                product.find_element_by_xpath("div/button").click()
        #clica na opção de checkout
        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        #clica na caixa de texto de promoção
        self.driver.find_element_by_xpath("/html/body/app-root/app-shop/div/div/div/table/tbody/tr[3]/td[5]/button").click()
        #escreve 'Ind' na caixa de texto
        self.driver.find_element_by_css_selector("#country").send_keys('Ind')
        #espera explicita para aparecer as opções
        wait = WebDriverWait(self.driver, 7)
        #localizar a opção desejada
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/app-root/app-shop/div/app-checkout/div/div[2]/ul/li/a")))
        #clicar na opção desejada
        self.driver.find_element_by_xpath("/html/body/app-root/app-shop/div/app-checkout/div/div[2]/ul/li/a").click()
        #clica no checkbox para aceitar os termos e condições
        self.driver.find_element_by_xpath('.//*[contains(text(), "I agree with the")]').click()
        #clica na opção checkout
        self.driver.find_element_by_xpath("/html/body/app-root/app-shop/div/app-checkout/div/form/input").click()
        #guarda o texto de sucesso em uma variável
        successTitle = self.driver.find_element_by_xpath("/html/body/app-root/app-shop/div/app-checkout/div[2]/div").text
        #confirma se o texto aparece
        assert "Thank you! Your order will be delivered in next few weeks :-)" in successTitle
        #printa no terminal o texto
        print(successTitle)
        #faz o print da tela final com a mensagem de sucesso
        self.driver.get_screenshot_as_file('screen.png')