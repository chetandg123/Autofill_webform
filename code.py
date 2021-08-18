


#clear the records in csv file once operation is done
from Locators.selenium_locators import selenium_locators
from logs.loggers import log_Details
from reuse_funs import functions
from csv import writer


def get_clearing_csv_file():
    locator = selenium_locators()
    resue = functions()
    form_data = resue.get_form_data_dir() + locator.filename
    print("Deletion of records in existing csv file")
    f = open(form_data, "w+")
    print('**********File is cleared***********')
    f.close()

def get_event_id_with_records_updated():
    logger = log_Details.logen()
    logger.info('**********************Web form filling process is started*********************')
    record=0
    logger.info(str(record)+' updated')
    logger.info('***************Record is updated successfully******************')

def generate_event_with_records_csv_file():
    header = ["Event_Id", "Quality/Velocity", "Problem Origin", "Event Type", "Product Family", "New/Found/Missing",
              "Serial Prefix", "Serial Number", "Part Number", "ID Area", "Course Area", "PD Name",
              "Problem Description", "Problem Symptom Comment", "Status", "Priority", "Stop time"]
    i=0
    event_id=""
    List = [event_id[i],"......................."]
    with open('event_records.csv', 'a') as f_object:
        writer_object = writer(f_object)
        if f_object.tell() == 0:
            writer_object.writerow(header)
        writer_object.writerow(List)
        f_object.close()