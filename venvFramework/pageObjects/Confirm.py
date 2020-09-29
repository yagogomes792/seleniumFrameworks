from selenium.webdriver.common.by import By

class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    
    promoCode = (By.CSS_SELECTOR, "#country")
    selectPromoCode = (By.XPATH, "/html/body/app-root/app-shop/div/app-checkout/div/div[2]/ul/li/a")
    selectCheckbox = (By.XPATH, './/*[contains(text(), "I agree with the")]')
    purchase = (By.XPATH, "/html/body/app-root/app-shop/div/app-checkout/div/form/input")
    message = (By.XPATH, "/html/body/app-root/app-shop/div/app-checkout/div[2]/div")

    #escreve 'Ind' na caixa de texto
    def enterPromoCode(self):
        return self.driver.find_element(*ConfirmPage.promoCode)
    
    #clicar na opção do código promocional desejado
    def choosePromoCode(self):
        return self.driver.find_element(*ConfirmPage.selectPromoCode)

    #clica no checkbox para aceitar os termos e condições
    def clickCheckbox(self):
        return self.driver.find_element(*ConfirmPage.selectCheckbox)

    #clica na opção checkout
    def confirmPurchase(self):
        return self.driver.find_element(*ConfirmPage.purchase)
    
    #guarda o texto de sucesso em uma variável
    def successMessage(self):
        return self.driver.find_element(*ConfirmPage.message)