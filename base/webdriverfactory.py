"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager


class WebDriverFactory():

    def __init__(self, browser, baseUrl):
        """
        Inits WebDriverFactory class

        :param browser:
        :returns None
        """
        self.browser = browser
        self.baseUrl = baseUrl


    def getWebDriverInstance(self):
        """
        Get WebDriver Instance based on the browser configuration
        :return:
            'WebDriver Instance'
        """
        #baseUrl = "https://demoqa.com/books"

        if self.browser == "iexplorer":
            driver = webdriver.Ie(IEDriverManager().install())
        elif self.browser == "firefox":
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif self.browser == "chrome":
            driver = webdriver.Chrome(ChromeDriverManager().install())
        else:
            driver = webdriver.Firefox()

        # Setting Driver Implicit Time out for an Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(self.baseUrl)
        return driver

   # def getTitleToSearch(self):
   #     return self.titleToSearch