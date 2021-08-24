import time
from _csv import writer

from pandas import read_csv
from selenium.webdriver.support.select import Select

from Locators.selenium_locators import selenium_locators
from logs.loggers import log_Details
from reuse_funs import functions


class script_for_fillup_webpage():

    def __init__(self,driver):
        self.driver = driver
    logger = log_Details.logen()

    def webpage_contents(self):
        self.locator = selenium_locators()
        self.resue = functions()
        self.driver.implicitly_wait(50)
        # dropdowns
        self.logger.info('**********************Web form filling process is started*********************')
        output_file = self.resue.store_result_to_output()+ self.locator.outputfile
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
            # Select Quality/Velocity
            self.locator = selenium_locators()
            select = Select(self.driver.find_element_by_id(self.locator.Quality))
            select.select_by_visible_text(str(quality[i]))
            time.sleep(1)

            # Select Problem Origin
            select = Select(self.driver.find_element_by_id(self.locator.Problem_Origin))
            select.select_by_visible_text(problem_origin[i])
            time.sleep(3)

            # Select New/Missed/Found
            select = Select(self.driver.find_element_by_id(self.locator.new_found))
            select.select_by_visible_text(new_found[i])
            time.sleep(1)

            # Select Product Family
            select = Select(self.driver.find_element_by_id(self.locator.Product_Family))
            select.select_by_visible_text(Product_Family[i])
            time.sleep(1)

            # Select serialPrefix
            select = Select(self.driver.find_element_by_id(self.locator.Serial_Prefix))
            select.select_by_visible_text(Serial_Prefix[i])

            # Enter Serial number
            element = self.driver.find_element_by_id(self.locator.Serial_Number)
            element.send_keys(str(Serial_Number[i]))


            # Enter Part Number
            element = self.driver.find_element_by_id(self.locator.PartNumber)
            element.send_keys(int(Part_Number[i]))

            # Select Event Status
            select = Select(self.driver.find_element_by_id(self.locator.Status))
            select.select_by_visible_text(Status[i])

            if self.driver.current_url == 'https://aqe-qa.cat.com/aqe/processEvent.do':
                # Select Event ID Area
                select = Select(self.driver.find_element_by_id(self.locator.ID_Area))
                select.select_by_visible_text(ID_Area[i])
                time.sleep(2)
            # #Enter problem description

            if self.driver.current_url == 'https://aqe-qa.cat.com/aqe/processEvent.do':
                ele = self.driver.find_element_by_id(self.locator.Problem_Description)
                ele.send_keys(Problem_Description[i])

                # #Enter problem Symptom
                ele = self.driver.find_element_by_id(self.locator.Problem_Symptom)
                ele.send_keys(Problem_Symptom[i])
                time.sleep(2)

            if self.driver.current_url == 'https://aqe-qa.cat.com/aqe/processEvent.do':
                # Select Supplier
                # if problem_origin[i] != 'Facility':
                #     select = Select(self.driver.find_element_by_id('supplierCode'))
                #     select.select_by_visible_text('HYDAC INDIA PVT LTD-B5369R0')

                #     # Select Supplier Notification group
                #     select = Select(self.driver.find_element_by_id('supplierNotificationGroupId'))
                #     select.select_by_visible_text('B5369R0 - HEX')

                # Select Event ID Area
                select = Select(self.driver.find_element_by_id(self.locator.ID_Area))
                select.select_by_visible_text(ID_Area[i])

                # Select Cause ID Area
                select = Select(self.driver.find_element_by_id(self.locator.CauseArea))
                select.select_by_visible_text(Cause_Area[i])

                # Select Priority description
                select = Select(self.driver.find_element_by_id(self.locator.Priority_Description))
                select.select_by_visible_text(Priority[i])

                # Select PD code
                select = Select(self.driver.find_element_by_id(self.locator.PD_Name))
                select.select_by_visible_text(PD_Name[i])

                # #Enter Stop time
                ele = self.driver.find_element_by_id(self.locator.Stop_Time)
                ele.send_keys(int(Stop_time[i]))
                time.sleep(2)

            event_id = self.driver.find_element_by_name(self.locator.Event_Number).get_attribute("value")

            output = [event_id, quality[i], problem_origin[i], event_type[i], Product_Family[i], new_found[i],
                      Serial_Prefix[i], Serial_Number[i], Part_Number[i], ID_Area[i], Cause_Area[i], PD_Name[i],
                      Problem_Description[i], Problem_Symptom[i], Status[i], Priority[i], Stop_time[i]]

            header = ["Event_Id", "Quality/Velocity", "Problem Origin", "Event Type", "Product Family",
                      "New/Found/Missing",
                      "Serial Prefix", "Serial Number", "Part Number", "ID Area", "Course Area", "PD Name",
                      "Problem Description", "Problem Symptom Comment", "Status", "Priority", "Stop time"]

            with open(output_file, 'a') as f_object:
                writer_object = writer(f_object)
                if f_object.tell() == 0:
                    writer_object.writerow(header)
                writer_object.writerow(output)
                f_object.close()

            print(f"Event number {count} {event_id} successfully created")
            time.sleep(4)
            count = count + 1

            self.driver.find_element_by_id(self.locator.save_submitbtn).click()
            time.sleep(4)
            count = count + 1
            self.logger.info(str(count)+str(event_id)+"********* Event is Created****************")

            #logic to clear input csv file once operation is completes
            print("Deletion of records in existing input csv file")
            f = open(form_data, "r+")
            f.truncate(228)
            print('**********File is cleared***********')
            f.close()
