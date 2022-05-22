from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    country = (By.XPATH, "//input[@id='country']")
    selCountry = (By.LINK_TEXT, "India")
    agreeTermsCheck = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchaseBtn = (By.XPATH, "//input[@class='btn btn-success btn-lg']")
    successMsg = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def getcountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def setCountry(self):
        return self.driver.find_element(*ConfirmPage.selCountry)

    def agreeTermsCond(self):
        return self.driver.find_element(*ConfirmPage.agreeTermsCheck)

    def setpurchaseBtn(self):
        return self.driver.find_element(*ConfirmPage.purchaseBtn)

    def getSuccessMsg(self):
        return self.driver.find_element(*ConfirmPage.successMsg)
