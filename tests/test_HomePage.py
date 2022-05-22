import pytest
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestPCHomePage(BaseClass):

    def test_homePage(self, getData):
        log = self.getlogger()
        homepage = HomePage(self.driver)

        homepage.setName().send_keys(getData["name"])
        homepage.setEmail().send_keys(getData["email"])
        homepage.setPassword().send_keys(getData["password"])
        homepage.checkicecream().click()
        self.selectOptionsByText(homepage.getgender(), getData["gender1"])
        homepage.setemployStatus(getData["status"])
        # give arguments, Student - option1, employed - option2, Enterpreneur - option3

        homepage.submitBtn().click()
        # homepage.getTwowaytextbox()
        alertMsg = homepage.getsuccessMsg().text
        log.info("alert message: " + alertMsg)
        assert "success" in alertMsg

        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getExcelData("Testcase1"))
    def getData(self, request):
        return request.param
