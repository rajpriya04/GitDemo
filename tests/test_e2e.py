import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getlogger()
        homePage = HomePage(self.driver)
        homePage.shopItems().click()

        checkoutpage = CheckoutPage(self.driver)
        products = checkoutpage.getProducts()
        product_names = checkoutpage.getProductnames()

        confirmPage = ConfirmPage(self.driver)
        # two ways:
        # 1st way:
        # for product_name in product_names:
        #     # print("X")
        #     print(product_name.text)
        #     if product_name.text == "Blackberry":
        #         driver.find_element(By.XPATH, "//div[@class = 'card h-100']/div[2]/button").click()

        # 2nd way:
        for product in products:
            productname = product.find_element(By.XPATH, "div/h4/a").text
            log.info(productname)
            if productname == 'Blackberry':
                product.find_element(By.XPATH, "div/button").click()

        checkoutpage.checkoutCartBtn().click()

        confirmPage = checkoutpage.setcheckoutBtn()

        wait = WebDriverWait(self.driver, 10)

        wait.until(expected_conditions.presence_of_element_located(confirmPage.country))
        confirmPage.getcountry().send_keys("ind")

        self.verifyLinkText("India")
        confirmPage.setCountry().click()

        confirmPage.agreeTermsCond().click()
        confirmPage.setpurchaseBtn().click()

        msg = confirmPage.getSuccessMsg()
        print(msg.text)

        assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in msg.text, "Success msg didn't match"
        print("hello")
        print("Welcome to python testing")
        log.info("Msg is "+msg.text)
        self.driver.get_screenshot_as_file("Screenshot.png")






