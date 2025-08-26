import csv
#* Lab 6: Sorting Data from a CSV File
#  Jake Platt
#   A.  List the 10 highest salaries in order.
#        a. When listing the salaries include, on the same line, the salary, last name and department
#    B. Determine the average annual salary for all employees in the MIS Department. No Binary Search. Seq Search
    C. List the 10 lowest salaries in order.
#        a. When listing the salaries include, on the same line, the salary, last name and department
#    D. What would it cost the company if every employee received a 5% raise.
#    E. Sort the data in Alphabetical order 
#      a. List the first 5 and the last 5 records.'''


#====================================================== Functions ======================================================

# Function to swap strings in a list
def string_Swap():
    temp = list1[pos]
    list1[pos] = list1[pos + 1]
    list1[pos + 1] = temp

#====================================================== Main Code ======================================================
with open("C:\Lab6.csv") as file:
    reader = csv.reader(file)
    fname = []
    lname = []
    department = []
    position = []
    salary = []
    for row in reader:
        fname.append(row[0])
        lname.append(row[1])
        department.append(row[2])
        position.append(row[3])
        salary.append(row[4])

n = len(lname)
for i in range(n-1):
    for j in range(n-i-1):
        if lname[j] > lname[j+1]:                       #Alpthabetical order
            
            string_Swap(lname, j)                       #Swap last names
            string_Swap(fname, j)                       #Swap first names
            string_Swap(department, j)                  #Swap departments
            string_Swap(position, j)                    #Swap positions
            string_Swap(salary, j)                      #Swap salaries


print("The 10 highest salaries are:")                   #Highest salaries
    print("Salary\tLast Name\tDepartment")
for i in range(n-1, n-11, -1):
    print(f"{salary[i]}\t{lname[i]}\t{department[i]}")

print("\nThe average annual salary for all employees in the MIS department are:")   #Average MIS salary
total_salary = 0
count = 0
for i in range(n):
    if department[i] == "MIS":
        total_salary += float(salary[i])
        count += 1
        if count > 0:
            average_salary = total_salary / count
            print(f"${average_salary:.2f}")

print("\nThe 10 lowest salaries are:")                                              #Lowest salaries
print("Salary\tLast Name\tDepartment")
for i in range(10):
    print(f"{salary[i]}\t{lname[i]}\t{department[i]}")

print("\nThe cost to the company if every employee received a 5% raise is:")      #5% raise cost
total_cost = 0
for i in range(n):
    total_cost += float(salary[i]) * 1.05
    print(f"${total_cost:.2f}")
print("\nThe first 5 and last 5 records in alphabetical order are:")               #First and last 5 records
print("First 5 Records:")
for i in range(5):
    print(f"{fname[i]} {lname[i]} - {department[i]} - {position[i]} - ${salary[i]}")
print("\nLast 5 Records:")
for i in range(n-5, n):
    print(f"{fname[i]} {lname[i]} - {department[i]} - {position[i]} - ${salary[i]}")



