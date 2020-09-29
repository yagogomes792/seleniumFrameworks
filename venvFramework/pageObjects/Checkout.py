from selenium.webdriver.common.by import By

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver


    product = (By.CSS_SELECTOR, ".card-title a")
    selectProduct = (By.CSS_SELECTOR, ".card-footer button")
    checkouButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkoutProducts = (By.XPATH, "/html/body/app-root/app-shop/div/div/div/table/tbody/tr[3]/td[5]/button")

    #guarda em uma variável todos os produtos
    def findProducts(self):
        return self.driver.find_elements(*CheckoutPage.product)

    #condição para selecionar o produto com o nome blackberry
    def chooseProduct(self):
        return self.driver.find_element(*CheckoutPage.selectProduct)

    #clica na opção de checkout
    def checkouItem(self):
        return self.driver.find_element(*CheckoutPage.checkouButton)
    
    #clica para finalizar compra
    def confirmCheckout(self):
        return self.driver.find_element(*CheckoutPage.checkoutProducts)