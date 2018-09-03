"""

    Written @ Nikhil

    If you have any queries or suggestions regaring this concept
    feel free to contact me via nikhil.ss4795@gmail.com
    Thank you for spending your time on this.
    
    Description :
    
    Checking whether two sheets are equal or not,
    if not, then shows the differences b/w two input sheets in two output sheets.

    ie.., it shows the data from sheet_1 and data from sheet_2 in seperate cells with
    a unique reference number with respective headers in a single row.

    *  Even though if the sheets are in unordered form (only rows), then also it works fine.
    *  It works fine for large sheets also.

    Input sheet constraints :

    1. Two sheets must be csv
    2. Two sheets must contain a reference column which is common in both in column 0.(Column A)
    3. Two sheets must contain same Header in same order for all columns in each sheet.
    4. Two sheets must conatin same Number of columns.
    

    Output sheet details :

    ** Total two sheets will be generated.
        1. all_errors_seperated_columns :
            *  contains the errors in seperate cells for both the sheets, one row contains
               only one error, so there may be chance of getting duplicate reference numbers
               which has errors in multiple columns.
            *  So that you can have total number of errors in seperate rows.
            
        2. Unique_reference_column_sheet:
            same as above sheet, but it doesn't contains duplicates reference numbers,
            i.e.., it contains all the errors of a particular reference number in the same row only.

    How to run :
    
        Just change the sheet name in "sheet_1_name" and "sheet_2_name" variables after the functions
        code of the two input sheets and hit run.

    Example :

        I will be providing the sample input sheets and thier respective output sheets,
        please check it out if you have any problem.
    
"""


#############################################################################

import csv
import time
from time import sleep
global col_length

def total_data(temp_sheet):
    data_list = []
    data_dict = {}
    datain = csv.reader(open(temp_sheet+'.csv','rU'))
    for index,each in enumerate(datain):
        if index == 0:
            pass
        else:
            if each[0] in data_dict.keys():
                pass
            else:
                data_dict[each[0]] = []
                for data in range(1,len(each)):
                    if len(each[data]) > 0 :
                        data_dict[each[0]].append(each[data])
                    else:
                        data_dict[each[0]].append("No data found")

        global col_length
        col_length = len(each)

    return data_dict

def find_differences(data_1,data_2):
    diff_dict = {}
    for key,value in data_1.iteritems():
        for dict_value in range(0,len(value)):
            if data_1[key][dict_value] == data_2[key][dict_value]:
                pass
            else:
                if key in diff_dict.keys():
                    diff_dict[key].append(dict_value)
                else:
                    diff_dict[key]=[]
                    diff_dict[key].append(dict_value)

    return diff_dict


#############################################################################
start_time = time.time()
sheet_1_name = "sample_sheet_1"
sheet_2_name = "sample_sheet_2"

header = []

data_in_head = csv.reader(open(sheet_1_name+".csv","rU"))
for index,each in enumerate(data_in_head):
    if index == 0:
        for i in range(0,len(each)):
            header.append(each[i])


#############################################################################

sheet_1_data = total_data(sheet_1_name)
sheet_2_data = total_data(sheet_2_name)

#############################################################################

error_list = find_differences(sheet_1_data,sheet_2_data)

#############################################################################

dataout = open("all_errors_seperated_columns.csv","wb")
datawrite = csv.writer(dataout)

#############################################################################

wanted_header = set()
count = 0
 
for key,value in error_list.iteritems():
    for dict_value in range(0,len(value)):
        count += 1
        wanted_header.add(value[dict_value])

print "Error Count : ",count

#############################################################################

wanted_head = list(wanted_header)

required_header = []

for i in range(0,len(wanted_head)):
    required_header.append(header[wanted_head[i] + 1])


final_header = []
final_header.append("Reference Column")

for i in range(0,len(required_header)):
    final_header.append(required_header[i]+" "+sheet_1_name)
    final_header.append(required_header[i]+" "+sheet_2_name)
    

datawrite.writerow(final_header)

#############################################################################

final_head_len = len(final_header)
final_head_len -=2

for key,value in error_list.iteritems():
    for dict_value in range(0,len(value)):
        head_pos = header[value[dict_value] + 1]
        sheet_head_pos = final_header.index(head_pos+" "+sheet_1_name)
        sheet_head_pos -=1
        row_data = []
        row_data.append(key)
        for i in range(0,final_head_len):
            if i == sheet_head_pos:
                row_data.append(sheet_1_data[key][value[dict_value]])
                row_data.append(sheet_2_data[key][value[dict_value]])
            else:
                row_data.append("-")

        datawrite.writerow(row_data)


dataout.close()
sleep(2)

#############################################################################

datain_other = csv.reader(open("all_errors_seperated_columns.csv","rU"))
second_head = []
data_dict_second = {}
for index,each in enumerate(datain_other):
    if index == 0:
        for i in range(0,len(each)):
            second_head.append(each[i])
    else:
        if each[0] in data_dict_second.keys():
            for i in range(1,len(each)):
                if each[i]!="-":
                    if data_dict_second[each[0]][i] == "-":
                        del data_dict_second[each[0]][i-1]
                        data_dict_second[each[0]].insert(i-1, each[i])
                        del data_dict_second[each[0]][i]
                        data_dict_second[each[0]].insert(i, each[i+1])
                        break
                        

        else:
            data_dict_second[each[0]] = []
            for i in range(1,len(each)):
                data_dict_second[each[0]].append(each[i])

#############################################################################

dataout = open("Unique_reference_column_sheet.csv","wb")
datawrite = csv.writer(dataout)
datawrite.writerow(second_head)

for key,value in data_dict_second.iteritems():
    row_data = []
    row_data.append(key)
    for i in range(0,len(value)):
        row_data.append(value[i])

    datawrite.writerow(row_data)

dataout.close()
        
print("Task Successfully completed")
print("Task took around : %s seconds " % ((time.time() - start_time)-2) )

"""
$$  In the above line "-2" is mentioned because i have given a sleep time of 2 secs...
    so removed that.

"""
#############################################################################
