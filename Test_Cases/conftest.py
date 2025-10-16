import pytest
from selenium import webdriver

@pytest.fixture()
def Setup(browser):
    if browser=="chrome":
        driver=webdriver.Chrome()
    elif browser=="edge":
        driver=webdriver.Edge()
    else:
        driver=webdriver.Chrome()
        pass
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    request.config.getoption("--browser")
