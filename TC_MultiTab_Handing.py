from selenium.webdriver import Chrome

driver = Chrome()
driver.get("http://www.thetestingworld.com/testings")
driver.maximize_window()

# Go to Log in
driver.find_element("xpath", "//label[text()='Login']").click()

# Enter Login details
driver.find_element("name", "_txtUserName").send_keys('Rutuja')
# driver.find_element("xpath", "//input[@placeholder ='Username']").send_keys('Rutuja')
# driver.find_element("name", "_txtPassword").send_keys('rutu')
# driver.find_element("xpath", "//input[@placeholder='mypassword']").send_keys('rutu')
driver.find_element("xpath", "//input[@name='_txtPassword']").send_keys('rutu')

# Click on Login button
driver.find_element("xpath", "//input[@value ='Login' and @type='submit']").click()

# Go to Delete menu in  My Accounts menu
driver.find_element('xpath', "//a[contains(text(), 'My Account')]").click()
driver.find_element('xpath', "//a[contains(text(), 'Delete')]").click()


all_windows = driver.window_handles
print(all_windows)

for win in all_windows:
    driver.switch_to.window(win)
    if driver.current_url == "https://www.thetestingworld.com/testings/manage_customer.php":
        driver.find_element('xpath', "//button[text()='Start Download']").click()

# input('wait')
