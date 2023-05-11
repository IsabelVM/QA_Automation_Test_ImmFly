import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time

class ProductsListPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        #we're calling the init method of superclass and we are providing the driver
        super().__init__(driver)
        self.driver = driver


    # Locators
    _articles ="//ol[@class='products list items product-items'][1]"
    _nextPage ="//li[@class='item pages-item-next']"
    _lastPage ="//li[@class='item pages-item-next']/div[@class='action  next disabled']"
    _orderDropDown = "sorter"

    def getProductsList(self):
        initialList  = self.getElementList(self._articles, "xpath")
        return initialList

    def dropDownOrder(self, Mode, Data):
        messageElement = self.waitForElement(locator=self._orderDropDown, locatorType="id")
        result = self.isElementDisplayed(locator=self._orderDropDown, locatorType="id", element=messageElement)
        if result:
            self.log.info("Drop Down Order Founded")
            self.dropDownSelect(locator=self._orderDropDown, locatorType="id",mode= Mode, data=Data)

    #def getSortSelected (self):
#
    #        messageElement = self.waitForElement(locator=self._orderDropDown, locatorType="id")
    #        result = self.isElementDisplayed(locator=self._orderDropDown, locatorType="id", element=messageElement)
    #        if result:
    #            self.log.info("Drop Down Order Founded")
    #            selectedVal = self.getSelectedValueDropDown(locator=self._orderDropDown, locatorType="id")
    #            return selectedVal
#
    #def VerifyInitialStatus(self, initialList, initialSelectionSort):
    #    actualList= self.getProductsList()
    #    selectSort = self.getSortSelected()
    #    if(initialList == actualList and initialSelectionSort == selectSort):
    #        return True
    #    else:
    #        return False

    #def backButtonClick(self):
    #    self.driver.back()

    #def verifyListOrdered(self,OrderedList):
    #    #while True:
    #    while not self.isElementDisplayed(self._lastPage):
    #        if (OrderedList != sorted(OrderedList)):
    #            print("La lista no está ordenada");
    #            break
    #        #if( not self.isElementDisplayed(self._lastPage) and self.isElementEnabled(self._nextPage, "xpath")):
    #        if (self.isElementEnabled(self._nextPage, "xpath")):
    #            nextPage = self.getElement(self._nextPage, "xpath")
    #            nextPage.click()
    #            messageElement = self.waitForElement(locator=self._articles, locatorType="xpath")
    #            result = self.isElementDisplayed(locator=self._orderDropDown, locatorType="id", element=messageElement)
    #            if not result:
    #                time.sleep(2)
    #        else:
    #            return False

    def checkOrderedList(self,typeOrder):
        result = True
        while True:
            initialList = self.getProductsList()
            initialListAux = initialList[0].text.split('\n')
            auxListProductName = []
            auxListProductPrice = []

            for i in range(0, len(initialListAux)-1, 2):
                auxListProductName.append(initialListAux[i])
                auxListProductPrice.append(initialListAux[i+1])

            if (typeOrder == 'name'):
                if (auxListProductName != sorted(auxListProductName)):
                    print("The list is not ordered by Product Name");
                    result = False
                    break
                if (not self.isElementDisplayed(self._lastPage, "xpath") and self.isElementEnabled(self._nextPage,"xpath")):
                    nextPage = self.getElement(self._nextPage, "xpath")
                    nextPage.click()
                    messageElement = self.waitForElement(locator=self._articles, locatorType="xpath")
                    result = self.isElementDisplayed(locator=self._articles, locatorType="xpath",
                                                     element=messageElement)
                else:
                    break

            elif(typeOrder == 'price'):
                if (auxListProductPrice != sorted(auxListProductPrice)):
                    print("The list is not ordered by Price");
                    result = False;
                    break
                if (not self.isElementDisplayed(self._lastPage,"xpath") and self.isElementEnabled(self._nextPage, "xpath")):
                    nextPage = self.getElement(self._nextPage, "xpath")
                    nextPage.click()
                    messageElement = self.waitForElement(locator=self._articles, locatorType="xpath")
                    result = self.isElementDisplayed(locator=self._articles, locatorType="xpath",
                                                     element=messageElement)
                    if not result:
                        time.sleep(2)
                elif(self.isElementDisplayed(locator=self._lastPage, locatorType="xpath")):
                    #print("hemos llegado con la lista bien a la última página");
                    break
        return result
