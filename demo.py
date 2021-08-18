



# logger = log_Details.logen()
#
# logger.info('**********************Web form filling process is started*********************')
# for i in range(10):
#     print(i)
#     logger.info(str(i)+' updated')
# logger.info('***************Record is updated successfully******************')


header = ["Event_Id","Quality/Velocity","Problem Origin","Event Type","Product Family","New/Found/Missing","Serial Prefix","Serial Number","Part Number" ,"ID Area","Course Area","PD Name","Problem Description","Problem Symptom Comment","Status","Priority","Stop time"]
number = []
data = ['Afghanistan', 652090, 'AF', 'AFG','asf']
for i in range(10):
    number = data.append(i)
from csv import writer

# with open('./output.csv', 'w', encoding='UTF8') as f:
#         writer = csv.writer(f)
#         writer.writerow(header)
#         writer.writerow(data)
header = ["Event_Id","Quality/Velocity","Problem Origin","Event Type","Product Family","New/Found/Missing","Serial Prefix","Serial Number","Part Number" ,"ID Area","Course Area","PD Name","Problem Description","Problem Symptom Comment","Status","Priority","Stop time"]
List = [7, 'devaraja', 5532, 1, 'UAE']
with open('event.csv', 'a') as f_object:
    writer_object = writer(f_object)
    if f_object.tell() == 0:
        writer_object.writerow(header)
    writer_object.writerow(List)
    f_object.close()
