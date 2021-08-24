import time
import unittest

from Test_Scripts.demo_test1 import demo_test1
from Test_Scripts.form_fillup import web_form_auto_fillup
from Test_Scripts.script_fillup import script_for_fillup_webpage
from reuse_funs import functions


class Auto_form_filling(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.reuse=functions()
        self.driver = self.reuse.get_chrome_driver()
        self.driver.maximize_window()
        self.reuse.get_webform_url()

    #Run any one test method for test trails


    def test_generate_events(self):
        method = script_for_fillup_webpage(self.driver)
        res = method.webpage_contents()
        time.sleep(3)



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()