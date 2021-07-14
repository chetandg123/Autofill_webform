import os
import time

from selenium import webdriver


class functions():

    def get_driver_path(self):
        cwd = os.path.dirname(__file__)
        driver_path = os.path.join(cwd, 'Driver/chromedriver')
        return driver_path

    def get_form_data_dir(self):
        cwd = os.path.dirname(__file__)
        file_path = os.path.join(cwd, 'form_data')
        return file_path

    def get_chrome_driver(self):
        loc = functions()
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options, executable_path=loc.get_driver_path())
        return self.driver

    def get_webform_url(self):
        self.driver.get("file:///home/chetan/Desktop/webform/form.html")
        time.sleep(2)
