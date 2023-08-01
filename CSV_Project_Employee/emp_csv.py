import csv
from emp_data import get_emp_objs

FILE_PATH = r"C:\Users\vinit\OneDrive\Documents\Softskill\Course python\Handling\Assignment\CSV Project_Employee\emp.csv"

all_emps = get_emp_objs(30)
# print(all_emps)

# write in csv using Dictwriter and writerow
with open(FILE_PATH, 'w', newline='') as file:
    fieldnames = ["EmpID", "EmpName", "EmpSalary"]  # headers
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader() # 
    for row in all_emps:
        writer.writerow(row.__dict__)
# ---------------------------------------------------------------------------------

# write in csv using tuple with writerows

# tuple_list = [(d.EmpID, d.EmpName, d.EmpSalary) for d in all_emps]

# print(tuple_list)

# headers = ["EmpID", "EmpName", "EmpSalary"]  # headers
# with open(FILE_PATH, 'w', newline='') as file:
#     # fieldnames = all_emps[0].keys()
#     writer = csv.writer(file)
#     writer.writerow(headers) # 
#     writer.writerows(tuple_list)

#---------------------------------------------------------------------
# write in csv using list of list with writer & writerows


# data_list =[]

# for d in all_emps:
#    data_list.append([d.EmpID, d.EmpName, d.EmpSalary])

# # print(data_list)


# headers = ["EmpID", "EmpName", "EmpSalary"]  
# with open(FILE_PATH, 'w', newline='') as file:

#     writer = csv.writer(file)
#     writer.writerow(headers) # 
#     writer.writerows(data_list)

#-------------------------------------------------------------------------------------

# write in csv using list of dictionary with DictWriter & writerows

# headers = ["EmpID", "EmpName", "EmpSalary"] 
# dict = { "EmpID": [],
#           "EmpName":[],
#           "EmpSalary" : []}

# for d in all_emps:
#     dict["EmpID"].append(d.EmpID)
#     dict["EmpName"].append(d.EmpName)
#     dict["EmpSalary"].append(d.EmpSalary)
# print(dict)
    

# with open(FILE_PATH, 'w', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames= headers)
#     writer.writeheader() 
#     writer.writerows(dict)
    
#----------------------------------------------------------------------------------------------
# csv file(whatever data written) read using reader

# with open(FILE_PATH, 'r') as file:
#     reader = csv.reader(file)
#     print(reader)
#     for row in reader:
#         print(row) 
            
#----------------------------------------------------------------------------------------------------
# csv file(whatever data written) read using DictReader

# with open(FILE_PATH, 'r') as file:
#     csv_file = csv.DictReader(file)
#     for row in csv_file:
#         print(dict(row))

#-----------------------------------------------------------------------
        
