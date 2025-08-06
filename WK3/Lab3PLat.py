#WK2D1
# Jacob Platt
# SE216 Intermediate Python 
#07/28/2025

# Explain What the Program Does:
#   
# Determine how much it would cost the company to replace all computers that are more than 3 years old and upgrade all computers running Windows 10 to 11
# When processing the file all data must be read into lists before processing the data.  You may count the records when reading data into the lists.
#=======================================================================
#Module Imports
import csv
import datetime
from ctypes import sizeof

#============Functions=================================

#============Main Program=============================

#============Global Variables==========================

make = []
vender = []
processor = []
cores = []
ssd = []
winVersion = []
curYear = 25  # Current year for comparison
year = []


records = 0
numberOfDesktops = 0
deskTopCost = 0
numberOfLaptops = 0
lapTopCost = 0
numberOfUpgrades = 0
upgradeCost = 0

#=======================================================================

with open("C:/Lab3.csv", "r") as file:
    person = csv.reader(file)
    for row in person:  
        make.append(row[0]) 
        vender.append(row[1])  
        processor.append(row[2])  
        cores.append(int(row[3]))
        ssd.append(row[4])
        winVersion.append(row[5])
        year.append(int(row[6]))  
        records += 1
    
sizeoflist = len(make)

print(sizeoflist) # 


for i in range (sizeoflist):
    diff = curYear - year[i] 
    if diff >= 3:
        if make[i] == "D":
            numberOfDesktops += 1
            deskTopCost += 2500
        else:
            numberOfLaptops += 1
            lapTopCost += 1800


    if winVersion[i] == "W10":
        upgradeCost += 150
        numberOfUpgrades += 1


print(f"You will need to replace {numberOfLaptops} costing {lapTopCost}")
print(f"You will need to replace {numberOfDesktops} costing {deskTopCost}")
print(f"You will need to upgrade {numberOfUpgrades} costing {upgradeCost}")
print(f"The total cost to replace all computers is {deskTopCost + lapTopCost}")

