from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = Chrome()
driver.get("http://www.thetestingworld.com/testings")
driver.maximize_window()

driver.find_element("xpath",'//img[@src="banner/64625f639e96b.png"]').click()

main_window = ""
all_windows = driver.window_handles
print(all_windows)

# **************Close all other windows *********************
for win in all_windows:
    driver.switch_to.window(win)
    print(driver.current_url)
    if driver.current_url == "https://www.facebook.com/groups/1319017341783803":
        print('Window')
        # Chrome browser controls, for cookies, popup closing
        act = ActionChains(driver)
        # Perform tab key
        for i in range(0,15):
            act.send_keys(Keys.TAB).perform()

        act.send_keys(Keys.ENTER).perform()
        time.sleep(5)
        act.send_keys(Keys.ENTER).perform()
        time.sleep(5)
        driver.close()
    else:
        main_window = win

# **************** Switch to main window **********************
driver.switch_to.window(main_window)
input('wait')
