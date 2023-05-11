import time
import traceback
import random, string
import utilities.custom_logger as cl
import logging

class Util(object):

    log = cl.customLogger(logging.INFO)

    def sleep(self, sec, info= ""):
        if info is not None:
            self.log.info("Wait :: '"+ str(sec) + "' seconds for " + info)
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def getAlphaNumeric(self, lenght, type='letters'):
        """
        Get random string of characters

        :param lenght: Lenght of string, number of characters string should have
        :param type: Type of characters, string should have. Default is letters
        :return: lower/upper/digits for different types
        """
        alpha_num = ''
        if type == 'lower':
            case = string.ascii_lowercase
        elif type == 'upper':
            case = string.ascii_uppercase
        elif type == 'digits':
            case = string.digits
        elif type == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(lenght))

    def getUniqueName(self, charCount= 10):
        """
        Get a unique name
        """
        return self.getAlphaNumeric(charCount, 'lower')

    def getUniqueNameList(self, listSize = 5, itemLength=None):
        """
        Get a list of valid email ids
        :param listSize: Number of names ids. Default is 5 names in a list
        :param itemLength: It should be a list containing number of items equal to the listSize
                           This determines the length of the each item in the list[1,2,3,4,5]
        """
        nameList = []
        for i in range(0, listSize):
            nameList.append(self.getUniqueName(itemLength[i]))
        return nameList

    def verifyTextContains(self, actualText, expectedText):
        """
        Verify actual text contains expected text string
        :param actualText:
        :param expectedText:
        :return:
        """
        self.log.info("Actual Text From Application Web UI --> :: "+ actualText)
        self.log.info("Expected Text From Application Web UI --> ::"+ expectedText)
        if expectedText.lower() in actualText.lower():
            self.log.info("### VERIFICATION CONTAINS!!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT CONTAINS!!!")
            return False

    def verifyTextMatch(self, actualText, expectedText):
        """
        Verify text Match
        :param actualText:
        :param expectedText:
        :return:
        """
        self.log.info("Actual Text From Application Web UI --> :: " + actualText)
        self.log.info("Expected Text From Application Web UI --> ::" + expectedText)
        if expectedText.lower() == actualText.lower():
            self.log.info("### VERIFICATION MATCHED!!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT MATCHED!!!")
            return False

    def VerifyListMatch(self, expectedList, actualList):
        """
        Verify two lists matches
        """
        return(set(expectedList)==set(actualList))

    def verifyListContains(self, expectedList, actualList):
        """
        Verify actual list contains elements of expected list
        """
        length = len(expectedList)
        for i in range(0, length):
            if expectedList[i] not in actualList:
                return False
            else:
                return True