import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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

    def store_result_to_output(self):
        cwd = os.path.dirname(__file__)
        file_path = os.path.join(cwd, 'Ouput_file')
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

    # def get_webform_url(self):
    #     paths = get_paths()
    #     self.driver.get(paths.get_application_url())
    #     time.sleep(2)

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

    def get_webform_url(self):
        paths = get_paths()
        locator = selenium_locators()
        self.driver.maximize_window()
        self.driver.implicitly_wait(50)
        self.driver.get(paths.get_application_url())
        while self.driver.current_url == 'https://logint.cat.com/CwsLogin/cws/sso.htm' or self.driver.current_url == 'https://logint.cat.com/CwsLogin/cws/login.htm':
            time.sleep(1)
            self.driver.find_element_by_name(locator.username).send_keys(paths.get_username())
            self.driver.find_element_by_name(locator.password).send_keys(paths.get_password())
            self.driver.find_element_by_id(locator.login_btn).send_keys(Keys.ENTER)
            time.sleep(3)
            if self.driver.current_url == 'https://logint.cat.com/CwsLogin/cws/processlogin.htm':
                self.driver.get('https://aqe-qa.cat.com/aqe/index.do')
                while self.driver.current_url == 'https://aqe-qa.cat.com/aqe/index.do':
                    time.sleep(2)
                    self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/table/tbody/tr[2]/td[2]/ul[14]/a').click()
                while self.driver.current_url == 'https://aqe-qa.cat.com/aqe/saveFacilityCode.do?facilityCode=WK':
                    time.sleep(1)
                    self.driver.find_element_by_link_text('New Event').click()
                    time.sleep(2)








