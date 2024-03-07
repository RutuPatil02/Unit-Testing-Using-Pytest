from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as ec
import time
import pytest
import Take_PageScreenShot


@pytest.fixture()
def environment_setup():
    global driver
    driver = Chrome()
    driver.get("http://www.thetestingworld.com/testings")
    driver.maximize_window()
    yield

    # *******************Take runtime screenshot **************************
    # ********** before screenshot, scroll up using javascript **********
    driver.execute_script("window.scrollTo(0,220);")
    # driver.get_screenshot_as_file("C:/Users/shara/PycharmProjects/LearnPyTest/Registration.png")
    Take_PageScreenShot.screen_shot(driver, "Registration")
    driver.close()


def test_registration_validate(environment_setup):
    # locating element by CCS locator
    driver.find_element(by='name', value='fld_username').send_keys('username')

    # locating element by xpath locator
    driver.find_element(by='xpath', value="//input[@name='fld_email']").send_keys('username@gmail.com')
    driver.find_element(by='name', value='fld_password').send_keys('abcd123')

    driver.find_element(by='name', value='fld_cpassword').send_keys('abcd123')
    driver.find_element(by='name', value='add_type').send_keys('xyz')
    driver.find_element(by='name', value='phone').send_keys('123456789')

    # work on radio button
    driver.find_element(by='xpath', value="//input[@value='home']").click()

    # work on Dropdown
    obj = Select(driver.find_element(by='name', value='sex'))
    obj.select_by_index(1)

    # *********** Implicit wait till text in dropdown to appear ***************
    wait = WebDriverWait(driver=driver, timeout=100)
    wait.until(ec.text_to_be_present_in_element((By.ID, 'countryId'), 'India'))
    obj2 = Select(driver.find_element(by='id', value='countryId'))
    obj2.select_by_value('101')
    # obj2.select_by_visible_text('India')

    wait.until(ec.text_to_be_present_in_element((By.ID, 'stateId'), 'Maharashtra'))
    obj3 = Select(driver.find_element(by='name', value='state'))
    obj3.select_by_value('22')
    # obj3.select_by_visible_text('Maharashtra')

    # work on sign-up button
    driver.find_element(by='xpath', value="//input[@type='submit']").click()

    # work on link
    # driver.find_element(by='link text', value='Read Detail').click()

    # ************ Explicit wait ************
    time.sleep(5)
