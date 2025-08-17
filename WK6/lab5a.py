# Using the “sequential search” write a program that changes the email address for all employees who work in the MIS Department. 
# Currently all employees  “top-level-domain (TLD) is .com.  .com should be changed to .net for all employees in the MIS Deplartment.  
# You must use a sequential search.  You may use a for loop or a while loop when searching.  
# Before the progrqam exits display the number of addresses that were changed. 
# You must use a function that searches for the email address and a function that changes the email address.

def change_email(email): #function to change email address
    if email.endswith('.com'):
        return email[:-4] + '.net'
    return email


with open('C:\Users\jakep\Downloads\Lab5A.txt', 'r') as file: 
    lines = file.readlines()

mis_count = 0
for i in range(len(lines)):
    if lines[4].strip() == 'MIS':
        email = lines[i].strip().split(',')[3] # Assuming email is the 4th item in the line
        new_email = change_email(email)
        lines[i] = lines[i].replace(email, new_email)
        mis_count += 1
    else:
        print(f"Employee {i+1} is not in the MIS Department.")

