import os
import time

from selenium import webdriver

from Locators.selenium_locators import selenium_locators
from get_directory import get_paths


class functions():



    def get_driver_path(self):
        cwd = os.path.dirname(__file__)
        driver_path = os.path.join(cwd, 'Driver/chromedriver')
        return driver_path

    def get_form_data_dir(self):
        cwd = os.path.dirname(__file__)
        file_path = os.path.join(cwd, 'Excel_Directory')
        return file_path

    def get_log_file_dir(self):
        cwd = os.path.dirname(__file__)
        file_path = os.path.join(cwd, 'logs')
        return file_path

    def get_web_page_dir(self):
        cwd = os.path.dirname(__file__)
        file_path = os.path.join(cwd,'config')
        return file_path

    def get_chrome_driver(self):
        loc = functions()
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options, executable_path=loc.get_driver_path())
        return self.driver

    def get_webform_url(self):
        paths = get_paths()
        self.driver.get(paths.get_application_url())
        time.sleep(2)

    def login_to_application(self):
        locator = selenium_locators()
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_id(locator.username).send_keys()
        time.sleep(2)
        self.driver.find_element_by_id(locator.password).send_keys()
        time.sleep(2)
        self.driver.find_element_by_id(locator.login_btn).click()
        time.sleep(4)

    def navigate_to_event_creator_page(self):
        self.driver.find_element_by_id('').click()
        time.sleep(3)
        self.driver.find_element_by_link_text().click()









