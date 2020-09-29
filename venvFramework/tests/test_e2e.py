import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from pageObjects.Checkout import CheckoutPage
from pageObjects.Confirm import ConfirmPage


class TestOne(BaseClass):

    def test_e2e(self):
        #clica na opção shop no menu
        homePage = HomePage(self.driver)
        homePage.shopItems().click()
        #guarda em uma variável todos os produtos
        checkoutPage = CheckoutPage(self.driver)
        products = checkoutPage.findProducts()
        #Iteração para passar por todos os produtos selecionados e guardados na variável
        #//div[@class='card h-100']/div/h4/a
        for product in products:
            product_name = product.text
            #condição para selecionar o produto com o nome blackberry
            if product_name == "Blackberry":
                checkoutPage.chooseProduct().click()
        #clica na opção de checkout
        checkoutPage.checkouItem().click()
        #clica para finalizar compra
        checkoutPage.confirmCheckout().click()
        #escreve 'Ind' na caixa de texto
        confirmPage = ConfirmPage(self.driver)
        confirmPage.enterPromoCode().send_keys('Ind')
        #espera explicita para aparecer as opções
        wait = WebDriverWait(self.driver, 7)
        #localizar a opção desejada
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/app-root/app-shop/div/app-checkout/div/div[2]/ul/li/a")))
        #clicar na opção do código promocional desejado
        confirmPage.choosePromoCode().click()
        #clica no checkbox para aceitar os termos e condições
        confirmPage.clickCheckbox().click()
        #clica na opção checkout
        confirmPage.confirmPurchase().click()
        #guarda o texto de sucesso em uma variável
        successTitle = confirmPage.successMessage().text
        #confirma se o texto aparece
        assert "Thank you! Your order will be delivered in next few weeks :-)" in successTitle
        #printa no terminal o texto
        print(successTitle)
        #faz o print da tela final com a mensagem de sucesso
        self.driver.get_screenshot_as_file('screen.png')