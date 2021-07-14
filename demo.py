import csv
from _csv import reader

import pandas as pd
from pandas import read_csv

from reuse_funs import functions

reuse = functions()
form_data = reuse.get_form_data_dir() +'/form_details.csv'
print(form_data)
# data = []
# with open(form_data)as csvfile:
#     datareader = csv.reader(csvfile, delimiter=',')
#     for row in datareader:
#         data.append(row[0])
# # print(data)

# with open(form_data, 'r') as read_obj:
#     csv_dict_reader = csv.DictReader(read_obj)
#     for row in csv_dict_reader:
#         # print(row)
#         print(row['Quality/Velocity'], row['Problem Origin'],row['Event Type'],row['Product Family'],row['New/Found/Missing'],
#               row['Serial Prefix'],row['Part Number '],row['ID Area'],row['Course Area'],row['PD Name'],row['Problem Description'])

# pd.set_option('display.max_colwidth', None)
# df = pd.read_csv(form_data)
# row_data = df.loc[ 'Part Number ' , : ]
#
# import csv
#
# with open(form_data) as f:
#     csv = csv.reader(f)
#     for row in csv:
#         print(" ".join(row))
#
# from pandas import *
#
# # reading CSV file
# data = read_csv(form_data)
#
# # converting column data to list
# month = data['Event Type'].tolist()
# fc = data['Quality/Velocity'].tolist()
#
# # printing list data
# print(month[0],fc[0])

data = read_csv(form_data)
# converting column data to list
event_type = data['Event Type'].tolist()
quality = data['Quality/Velocity'].tolist()
problem=data['Problem Origin'].tolist()
        # Product_Family=data['Product Family'].tolist()
        # cases =data['New/Found/Missing'].tolist()
        # Serial_Prefix=data['Serial Prefix'].tolist()
        # Serial_Number=data['Serial Number'].tolist()
        # Part_Number=data['Part Number'].tolist()
        # ID_Area=data['ID Area'].tolist()
        # Course_Area=data['Course Area'].tolist()
        # PD_Name=data['PD Name'].tolist()
        # Problem_Description=data['Problem Description'].tolist()

# print(quality[0],problem[0],event_type[0],)
# print(event_type)
# print(quality)


Part_Number=data['Part Number'].tolist()
print(Part_Number)