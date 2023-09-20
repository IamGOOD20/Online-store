from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class TestMain(unittest.TestCase):

    def setUp(self):
        '''connection Gmail'''
        self.browser = webdriver.Chrome()

    def tearDown(self):
        '''quit'''
        self.browser.quit()

    def test_home_page(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.assertIn('Home', self.browser.title)
        self.fail('End test!')

        # assert 'Home' == self.browser.title, 'browser title was ' + self.browser.title


if __name__ == '__main__':
    unittest.main()

