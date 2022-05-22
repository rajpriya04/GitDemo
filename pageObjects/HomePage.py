from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*=shop")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    icecreamChkbx = (By.XPATH, "//input[@class='form-check-input']")
    gender = (By.ID, "exampleFormControlSelect1")
    # employstatusName = (By.XPATH, "//div[@class='form-check form-check-inline']/label")
    employStatus = (By.XPATH, "//div[@class='form-check form-check-inline']/input")
    dob = (By.XPATH, "//input[@class='form-control']")
    submit = (By.CLASS_NAME, "btn-success")
    twoWayTextbox = (By.XPATH, "//h4/input[@name = 'name']")
    successMsg = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")



    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)

    def setName(self):
        return self.driver.find_element(*HomePage.name)

    # def nameComparison(self):
    #     return self.driver.find_element(By.NAME, "name").get_attribute('value')

    def setEmail(self):
        return self.driver.find_element(*HomePage.email)

    def setPassword(self):
        return self.driver.find_element(*HomePage.password)

    def checkicecream(self):
        return self.driver.find_element(*HomePage.icecreamChkbx)

    def getgender(self):
        return self.driver.find_element(*HomePage.gender)

    def setemployStatus(self, value):
        # employstatusNames = self.driver.find_elements(*HomePage.employstatusName)
        employstatuses = self.driver.find_elements(*HomePage.employStatus)

        for employstatus in employstatuses:

            # print(employstatus.get_attribute('value'))

            if employstatus.get_attribute('value') == value:
                employstatus.click()

    def setDOB(self):
        return self.driver.find_element(*HomePage.dob)

    def submitBtn(self):
        return self.driver.find_element(*HomePage.submit)

    def getTwowaytextbox(self):
        twowayMsg = self.driver.find_element(*HomePage.twoWayTextbox).text
        if twowayMsg == self.nameComparison():
            print("Match found")
        else:
            print("match not found")

    def getsuccessMsg(self):
        return self.driver.find_element(*HomePage.successMsg)

