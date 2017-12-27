# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoSuchElementException
import requests
import random
import time
import os
import sys

class AustriaChromeScheidung(unittest.TestCase):

    def setUp(self):

        # Put your username and authey below
        # You can find your authkey at cross browser testing.com/account
        self.username = "reak@gefen.online"
        self.authkey = "udf0108060cd35ad"

        self.api_session = requests.Session()
        self.api_session.auth = (self.username, self.authkey)

        self.test_result = None

        caps = {}

        caps['name'] = 'Austria Chrome Scheidung'
        caps['browserName'] = 'Chrome'
        caps['version'] = '61'
        caps['platform'] = 'Mac OSX 10.12'
        caps['screenResolution'] = '1920x1200'

        # start the remote browser on our server
        self.driver = webdriver.Remote(
            desired_capabilities=caps,
            command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub" % (self.username, self.authkey)
        )

        self.driver.implicitly_wait(10)

    def test_at_scheidung_chrome(self):
        # We wrap this all in a try/except so we can set pass/fail at the end
        try:
            # load the page url
            self.driver.get("http://www.mywebtoolz.com")
            time.sleep(20)

        except (AssertionError, WebDriverException, NoSuchElementException):

            self.test_result = 'fail'
            raise

    def tearDown(self):
        self.driver.quit()
        # Here we make the api call to set the test's score.
        # Pass it is passes, fail if an assertion fails, unset if the test didn't finish
        if self.test_result is not None:
            self.api_session.put('https://crossbrowsertesting.com/api/v3/selenium/' + self.driver.session_id,
                                 data={'action': 'set_score', 'score': self.test_result})


if __name__ == '__main__':
    unittest.main()
