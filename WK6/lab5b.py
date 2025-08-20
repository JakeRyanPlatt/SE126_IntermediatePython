import csv

def binary_search(target):
    tLow = 0
    tHigh = len(lname) - 1
    guess = (tLow + tHigh) // 2 #// is a floor division operator

    while tLow <= tHigh and lname[guess] != target:
        if lname[guess] > target:
            tHigh =  guess - 1
        else:
            tLow  = guess + 1

        guess = (tLow + tHigh) // 2
   
    if tLow <= tHigh:
        return guess
    else:
        return -5.2


#============ Global Variables ===============

fname = []
lname = []
phone = []
email = []
dept = []
employeePosition = []
records = 0 


#============ Main Program ===============
with open("C:\\Lab5b-2.csv") as f:
    data = csv.reader(f)
    for row in data:
        fname.append(row[0])
        lname.append(row[1])
        phone.append(row[2])
        email.append(row[3])
        dept.append(row[4])
        employeePosition.append(row[5])
        records += 1

target = input("Enter a last name to search ... ")

found = binary_search(target)

if found == -5.2:
    print("Not on the list!!!")
else:
    print("Found it: ", lname[found], "Position:", found)
    print("Email: ", email[found])
    print("Phone: ", phone[found])







            

