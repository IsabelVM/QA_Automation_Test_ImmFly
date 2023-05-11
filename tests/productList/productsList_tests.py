from pages.productsList.productsList_page import ProductsListPage
from utilities.testStatus import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class SearchBookTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.sbp = ProductsListPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validSortByProductName(self):
        self.sbp.dropDownOrder("value", "name")
        result1 = self.sbp.checkOrderedList('name')
        self.ts.mark(result1, "Detail verified")
        self.ts.markFinal("Test Finished", result1, "Result List Ordered by Product Name")

    @pytest.mark.run(order=1)
    def test_validSortByPrice(self):
        self.sbp.dropDownOrder("value", "price")
        result1 = self.sbp.checkOrderedList('price')
        self.ts.mark(result1, "Detail verified")
        self.ts.markFinal("Test Finished", result1, "Result List Ordered by price")



