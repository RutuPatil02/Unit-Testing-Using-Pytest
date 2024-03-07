from selenium.webdriver import Chrome
import logging

# Step 2 : Generate logger
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

# Step 3 :
warn = logging.FileHandler('Warning_Logs.txt')
warn.setLevel(logging.WARNING)

info = logging.FileHandler('Info_Logs.txt')
info.setLevel(logging.INFO)

# Step 4 : Create a log format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Step 5 :
warn.setFormatter(formatter)
info.setFormatter(formatter)

driver = Chrome()
driver.get("http://www.thetestingworld.com/testings")

log.info("[ The URL is open ]")
log.warning("[ There is delay in opening the browser ]")

