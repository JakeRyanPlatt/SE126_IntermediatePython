# Using the “sequential search” write a program that changes the email address for all employees who work in the MIS Department. 
# Currently all employees  “top-level-domain (TLD) is .com.  .com should be changed to .net for all employees in the MIS Deplartment.  
# You must use a sequential search.  You may use a for loop or a while loop when searching.  
# Before the progrqam exits display the number of addresses that were changed. 
# You must use a function that searches for the email address and a function that changes the email address.
import csv, os
# def change_email(email): #function to change email address
   # if email.endswith('.com'):
   #     return email[:-4] + '.net'
   # return email


# with open('C:\Users\jakep\Downloads\Lab5A.txt', 'r') as file: 
    #lines = file.readlines()

#mis_count = 0
#for i in range(len(lines)):
    #if lines[4].strip() == 'MIS': #.strip method removes any leading or trailing whitespace
      
    #else:
        #print(f"Employee {i+1} is not in the MIS Department.")

def sequentialSearch(list, tTarget):
    for i in range(len(list)):
        if list[i] == tTarget:
            return i

    return -1


#========== Main Program ==========

import csv, os

os.system("cls")

fname = []
lname = []
email = []

noRecords = 0

with open("D:\SE126\people3.csv") as f:
    data = csv.reader(f)
    for row in data:
        fname.append(row[0])
        lname.append(row[1])
        email.append(row[2])

        noRecords = noRecords + 1

target = input("Enter last name ... ")

found = sequentialSearch(lname, target)

if found == -1:
    print("Name not found!!!")
else:
    print(fname[found], " ", lname[found], " ", email[found])
          
                     

