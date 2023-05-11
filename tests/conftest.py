import time

import pytest
from base.webdriverfactory import WebDriverFactory

@pytest.fixture()
def setUp():
    print("Running method level setUp")

    yield
    print("Running method level tearDown")


@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser, baseURL):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser, baseURL)
    driver = wdf.getWebDriverInstance()

    # add 'driver' attribute to the class under test -->
    if request.cls is not None:
        request.cls.driver = driver
        _cookiesBtn = "//button[contains(text(),'ALLOW ALL')]"
        driver.find_element_by_xpath(_cookiesBtn).click()
        time.sleep(5)
        #_category = "//div[@class='filter-options-title']//span[contains(text(), 'Category')]"
        #_offers = "//div[@class='filter-options-content']//a[contains(text(), 'Offers')]"
        #driver.find_element_by_xpath(_category).click()
        #driver.find_element_by_xpath(_offers).click()

    yield driver
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--baseUrl")
    parser.addoption("--dirDriver")

#The scope we can put by module, or in this case we're going to test by session
@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def baseURL(request):
    return request.config.getoption("--baseUrl")

@pytest.fixture(scope="session")
def dirDriver(request):
    return request.config.getoption("--dirDriver")