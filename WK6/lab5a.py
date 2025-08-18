# Using the “sequential search” write a program that changes the email address for all employees who work in the MIS Department. 
# Currently all employees  “top-level-domain (TLD) is .com.  .com should be changed to .net for all employees in the MIS Deplartment.  
# You must use a sequential search.  You may use a for loop or a while loop when searching.  

import csv, os
#============ Functions ===============
def sequential_search():
    for i in range(len(email)):
        if dept[i] in "MIS":
            change_email[i]
            count += 1
    return count


def change_email(i):
    email[i] = email[i].replace(".com", ".net") 
    return email[i]

#============ Global Variables ===============

fname = []
lname = []
phone = []
email = []
dept = []
employeePosition = []
records = 0 
mis_count = 0

#============ Main Program ===============
with open("C:/Lab5A.txt") as f:
    data = csv.reader(f)
    for row in data:
        fname.append(row[0])
        lname.append(row[1])
        phone.append(row[2])
        email.append(row[3])
        dept.append(row[4])
        employeePosition.append(row[5])
        records += 1

newEmail = sequential_search()
print(f" The total number of records changed {records}\nTotal Number of changes made: {mis_count}")

        