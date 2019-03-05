import os
import sys
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Edit these to match your credentials
USERNAME = os.environ.get('BROWSERSTACK_USERNAME') or sys.argv[3]
BROWSERSTACK_ACCESS_KEY = os.environ.get(
    'BROWSERSTACK_ACCESS_KEY') or sys.argv[4]

if not (USERNAME and BROWSERSTACK_ACCESS_KEY):
    raise Exception("Please provide your BrowserStack username and access key")


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        url = "https://%s:%s@hub.browserstack.com/wd/hub" % (
            USERNAME, BROWSERSTACK_ACCESS_KEY
        )
        capabilities = {
            'browserName': 'Firefox',
            'browserVersion': '65.0',
            'browserstack.use_w3c': 'true',
            'bstack:options': {
                'os': 'Windows',
                'buildName': 'automate-python-samples',
                'osVersion': '10',
                'sessionName': 'nose_test',
                'projectName': 'Sample project',
                'debug': 'true'
            }
        }
        self.driver = webdriver.Remote(
            command_executor=url,
            desired_capabilities=capabilities
        )

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.google.com")
        elem = driver.find_element_by_name("q")
        elem.send_keys("selenium")
        elem.submit()
        self.assertIn("Google", driver.title)

    def tearDown(self):
        self.driver.quit()
