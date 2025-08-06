def seatMap():
    print("\t\t 1,")


row1 = ["0", "A", "B", "C", "D"]
row2 = ["0", "A", "B", "C", "D"]
row3 = ["0", "A", "B", "C", "D"]
row4 = ["0", "A", "B", "C", "D"]
row5 = ["0", "A", "B", "C", "D"]
row6 = ["0", "A", "B", "C", "D"] 
row7 = ["0", "A", "B", "C", "D"]


seatMap()
row = int(input("Which "))        
seat = input(f"Which seat in row {row} would you like to sit in ? ")


occupied = 0
if row1[1] == "X":
    occupied = 1
elif row1[2] == "X":
    occupied = 1
elif row1[3] == "X":
    occupied = 1
elif row[4] == "X":
    occupied = 1


reserveSeat(row,seat)