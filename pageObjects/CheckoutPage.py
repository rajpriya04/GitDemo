from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver


    products = (By.XPATH, "//div[@class = 'card h-100']")
    productnames = (By.XPATH, "//div[@class = 'card h-100']/div[1]/h4/a")
    checkCartBtn = (By.XPATH, "//div[@id='navbarResponsive']/ul/li/a")
    checkoutBtn = (By.XPATH, "//button[@class='btn btn-success']")

    def getProducts(self):
        return self.driver.find_elements(*CheckoutPage.products)

    def getProductnames(self):
        return self.driver.find_elements(*CheckoutPage.productnames)

    def checkoutCartBtn(self):
        return self.driver.find_element(*CheckoutPage.checkCartBtn)

    def setcheckoutBtn(self):
        self.driver.find_element(*CheckoutPage.checkoutBtn).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage

