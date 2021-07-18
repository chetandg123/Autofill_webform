import time
import unittest

from Test_Scripts.form_fillup import web_form_auto_fillup
from reuse_funs import functions


class Auto_form_filling(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.reuse=functions()
        self.driver = self.reuse.get_chrome_driver()
        self.driver.maximize_window()
        self.reuse.get_webform_url()

    def test_fillup_webforms(self):
        clas =web_form_auto_fillup(self.driver)
        method = clas.webform_fields()
        time.sleep(2)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()