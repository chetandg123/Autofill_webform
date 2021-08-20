import logging
import time
from pandas import read_csv
from selenium.webdriver.support.select import Select

from Locators.selenium_locators import selenium_locators
from logs.loggers import log_Details
from reuse_funs import functions
from csv import writer


class web_form_auto_fillup():

    def __init__(self,driver):
        self.driver=driver
    logger = log_Details.logen()

    def webform_fields(self):
        self.locator = selenium_locators()
        self.resue = functions()
        # dropdowns
        self.logger.info('**********************Web form filling process is started*********************')
        self.quality = Select(self.driver.find_element_by_id(self.locator.Quality))
        self.prob_origin = Select(self.driver.find_element_by_id(self.locator.Problem_Origin))
        self.new_found = Select(self.driver.find_element_by_id(self.locator.new_found))
        self.id_area = Select(self.driver.find_element_by_id(self.locator.ID_Area))
        self.cause_Area = Select(self.driver.find_element_by_id(self.locator.CauseArea))
        self.event_status = Select(self.driver.find_element_by_id(self.locator.Status))
        self.Priority_Description = Select(self.driver.find_element_by_id(self.locator.Priority_Description))
        self.Product_Family = Select(self.driver.find_element_by_id(self.locator.Product_Family))
        self.serial_pref = Select(self.driver.find_element_by_id(self.locator.Serial_Prefix))
        self.PD_name = Select(self.driver.find_element_by_id(self.locator.PD_Name))

        # input texts
        self.eventtype = self.driver.find_element_by_id(self.locator.Event_Type)
        self.part_number = self.driver.find_element_by_id(self.locator.PartNumber)
        self.Problem_Symptom = self.driver.find_element_by_id(self.locator.Problem_Symptom)
        self.Stop_Time = self.driver.find_element_by_id(self.locator.Stop_Time)
        self.Serial_num = self.driver.find_element_by_id(self.locator.Serial_Number)
        self.Problem_desc = self.driver.find_element_by_id(self.locator.Problem_Description)

        form_data = self.resue.get_form_data_dir() + self.locator.filename
        data = read_csv(form_data)
        # converting column data to list

        event_type = data['Event Type'].tolist()
        quality = data['Quality/Velocity'].tolist()
        problem_origin = data['Problem Origin'].tolist()
        new_found = data['New/Found/Missing'].tolist()
        ID_Area = data['ID Area'].tolist()
        Cause_Area = data['Course Area'].tolist()
        PD_Name = data['PD Name'].tolist()
        Problem_Description = data['Problem Description'].tolist()
        Product_Family = data['Product Family'].tolist()
        Serial_Prefix = data['Serial Prefix'].tolist()
        Serial_Number = data['Serial Number'].tolist()
        Part_Number = data['Part Number '].tolist()
        Priority = data['Priority'].tolist()
        Problem_Symptom = data['Problem Symptom Comment'].tolist()
        Status = data['Status'].tolist()
        Stop_time = data['Stop time'].tolist()

        count =0
        i=0
        for i in range(len(data)):
            self.quality.select_by_visible_text(quality[i])
            self.prob_origin.select_by_visible_text(problem_origin[i])
            self.eventtype.send_keys(event_type[i])
            time.sleep(2)

            if self.driver.current_url == 'https://aqe-qa.cat.com/aqe/processEvent.do':
                self.Product_Family.select_by_visible_text(Product_Family[i])
                self.new_found.select_by_visible_text(new_found[i])
                time.sleep(2)

            if self.driver.current_url == 'https://aqe-qa.cat.com/aqe/processEvent.do':
                self.serial_pref.select_by_visible_text(Serial_Prefix[i])
                self.Serial_num.send_keys(Serial_Number[i])

                self.part_number.send_keys(Part_Number[i])
                self.event_status.select_by_visible_text(Status[i])
                self.id_area.select_by_visible_text(ID_Area[i])
                time.sleep(2)

            if self.driver.current_url == 'https://aqe-qa.cat.com/aqe/processEvent.do':
                self.Problem_desc.send_keys(Problem_Description[i])
                self.Problem_Symptom.send_keys(Problem_Symptom[i])
                time.sleep(2)

            if self.driver.current_url == 'https://aqe-qa.cat.com/aqe/processEvent.do':
                self.id_area.select_by_visible_text(ID_Area[i])
                self.cause_Area.select_by_visible_text(Cause_Area[i])
                time.sleep(4)
                self.PD_name.select_by_visible_text(PD_Name[i])

                self.Priority_Description.select_by_visible_text(Priority[i])
                self.Stop_Time.send_keys(Stop_time[i])
                time.sleep(2)

            event_id = self.driver.find_element_by_id(self.locator.Event_Number).get_attribute("value")
            output = [event_id, quality[i], problem_origin[i], event_type[i], Product_Family[i], new_found[i],
                      Serial_Prefix[i], Serial_Number[i], Part_Number[i], ID_Area[i], Cause_Area[i], PD_Name[i],
                      Problem_Description[i], Problem_Symptom[i], Status[i], Priority[i], Stop_time[i]]

            header = ["Event_Id", "Quality/Velocity", "Problem Origin", "Event Type", "Product Family","New/Found/Missing",
                      "Serial Prefix", "Serial Number", "Part Number", "ID Area", "Course Area", "PD Name",
                      "Problem Description", "Problem Symptom Comment", "Status", "Priority", "Stop time"]

            with open('Event_Records.csv', 'a') as f_object:
                writer_object = writer(f_object)
                if f_object.tell() == 0:
                    writer_object.writerow(header)
                writer_object.writerow(output)
                f_object.close()

            # self.driver.find_element_by_id(self.locator.save_submitbtn).click()
            time.sleep(4)
            count = count + 1

            # logic to clear input csv file once operation is completes
            # print("Deletion of records in existing input csv file")
            # f = open(form_data, "r+")
            # f.truncate(228)
            # print('**********File is cleared***********')
            # f.close()


