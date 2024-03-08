from selenium.webdriver import Chrome
import pytest

# fixture to set pre-requisites example browser opening, database connection
# executes code before each testcase execution

# set scope as module to open browser for only once

# Assertion to compare actual result and expected result


@pytest.fixture(scope="module")
def setpath():
    global driver
    driver = Chrome()

    # executes after each test case execution
    yield
    driver.close()


def test_registration_data(setpath):
    driver.get("http://www.thetestingworld.com/testings")
    driver.maximize_window()
    assert driver.title == "Login & Sign Up Forms"


def test_registration_valid_data(setpath):
    driver.get("http://www.thetestingworld.com/testings")
    driver.maximize_window()
    assert driver.current_url == "https://www.thetestingworld.com/testings/"


def test_registration_invalid_data(setpath):
    driver.get("http://www.thetestingworld.com/testings")
    driver.maximize_window()
    assert driver.title == "Login & Sign Up Form's"
