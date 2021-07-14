import time
from pandas import read_csv
from selenium.webdriver.support.select import Select

from Locators.selenium_locators import selenium_locators
from reuse_funs import functions


class web_form_auto_fillup():
    def __init__(self,driver):
        self.driver=driver

    def webform_fields(self):
        self.locator = selenium_locators()
        self.resue = functions()
        #dropdowns

        self.quality = Select(self.driver.find_element_by_id(self.locator.Quality))
        self.prob_origine= Select(self.driver.find_element_by_id(self.locator.Problem_Origin))
        self.cases = Select(self.driver.find_element_by_id(self.locator.case))
        self.id_area = Select(self.driver.find_element_by_id(self.locator.ID_Area))
        self.cause_Area=Select(self.driver.find_element_by_id(self.locator.CauseArea))
        #input texts
        self.eventtype=self.driver.find_element_by_id(self.locator.Event_Type)
        self.part_number= self.driver.find_element_by_id(self.locator.PartNumber)

        form_data = self.resue.get_form_data_dir() +'/form_details.csv'
        data = read_csv(form_data)
        # converting column data to list

        event_type = data['Event Type'].tolist()
        quality = data['Quality/Velocity'].tolist()
        problem=data['Problem Origin'].tolist()
        case_state =data['New/Found/Missing'].tolist()
        ID_Area=data['ID Area'].tolist()
        Cause_Area=data['Course Area'].tolist()
        # PD_Name=data['PD Name'].tolist()
        # Problem_Description=data['Problem Description'].tolist()
        # Product_Family=data['Product Family'].tolist()
        # Serial_Prefix=data['Serial Prefix'].tolist()
        # Serial_Number=data['Serial Number'].tolist()
        Part_Number=data['Part Number '].tolist()
        count =0
        i=0
        for i in range(len(data)):
            self.part_number.clear()
            self.eventtype.clear()
            self.quality.select_by_visible_text(quality[i])
            self.prob_origine.select_by_visible_text(problem[i])
            self.part_number.send_keys(Part_Number[i])
            self.eventtype.send_keys(event_type[i])
            self.cases.select_by_visible_text(case_state[i])
            self.id_area.select_by_visible_text(ID_Area[i])
            self.cause_Area.select_by_visible_text(Cause_Area[i])

            self.driver.find_element_by_xpath(self.locator.save_submitbtn).click()
            time.sleep(4)
            count = count+1
            records= self.driver.find_element_by_id('demo').text
            print('Details Updated :',count,"-",records)

