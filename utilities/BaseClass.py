import inspect

import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyLinkText(self, text):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))


    def selectOptionsByText(self,locator,text):
        dropdown = Select(locator)
        return dropdown.select_by_visible_text(text)

    def getlogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)

        filehandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)

        return logger