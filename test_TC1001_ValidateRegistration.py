from selenium.webdriver import Chrome
import pytest


def inc(x):
    return x + 1


def test_answer():
    assert inc(4) == 5


@pytest.mark.sanity
def test_registration_data():
    driver = Chrome()
    driver.get("http://www.thetestingworld.com/testings")


@pytest.mark.smoke
def test_registration_valid_data():
    driver = Chrome()
    driver.get("http://www.thetestingworld.com/testings")


@pytest.mark.smoke
def test_registration_invalid_data():
    driver = Chrome()
    driver.get("http://www.thetestingworld.com/testings")
    driver.maximize_window()
