from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

desired_cap = {'browser': 'Chrome', 'browser_version': '62.0', 'os': 'Windows', 'os_version': '10', 'resolution': '1024x768'}

driver = webdriver.Remote(
    command_executor='http://reakrakover2:iFi4yYYQk3ozzAaQvTLy@hub.browserstack.com:80/wd/hub',
    desired_capabilities=desired_cap)

driver.get("http://www.mywebtoolz.com")
# time.sleep(2)
driver.quit()
