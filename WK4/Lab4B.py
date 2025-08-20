import csv

#============ Functions ===============
def sequential_search():
    for i in range(len(lname)):
        if lname[i] == search_index:
            print("Employee found:")
            print("First Name:", fname[i])
            print("Last Name:", lname[i])
            print("Phone:", phone[i])
            print("Email:", email[i])
            print("Department:", dept[i])
            print("Position:", employeePosition[i])
            return i
    return -1

#============= Global Variables ===============
fname = []
lname = []
phone = []
email = []
dept = []
employeePosition = []
records = 0

#============ Main Program ==================
with open("C:\\Lab4B.txt", "r") as file:
    data = csv.reader(file)
    for row in data:
        fname.append(row[0])
        lname.append(row[1])
        phone.append(row[2])
        email.append(row[3])
        dept.append(row[4])
        employeePosition.append(row[5])
        records += 1

search_index = input("Please enter an employee's last name to search for: ")

sequential_search()

with open("C:\\information.csv", "w", newline='') as file:
    dataWriter = csv.writer(file)
    for i in range(records):
        dataWriter.writerow([fname[i], lname[i], phone[i], email[i], dept[i], employeePosition[i]])