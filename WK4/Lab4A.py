def seatMap():
    print("\t\t 1,")


def seatReserve():
    if row[r][s] != "X":
        row[r][s] = "X":
        return(0)
    else:
        return 1

row1 = ["0", "A", "B", "C", "D"]
row2 = ["0", "A", "B", "C", "D"]
row3 = ["0", "A", "B", "C", "D"]
row4 = ["0", "A", "B", "C", "D"]
row5 = ["0", "A", "B", "C", "D"]
row6 = ["0", "A", "B", "C", "D"] 
row7 = ["0", "A", "B", "C", "D"]

anyMoreData = "Y"
while anyMoreData == "Y":
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
    elif row1[4] == "X":
        occupied = 1

     if row2[1] == "X":
        occupied = 1
    elif row2[2] == "X":
        occupied = 1
    elif row2[3] == "X":
        occupied = 1
    elif row2[4] == "X":
        occupied = 1
    
     if row3[1] == "X":
        occupied = 1
    elif row3[2] == "X":
        occupied = 1
    elif row3[3] == "X":
        occupied = 1
    elif row3[4] == "X":
        occupied = 1

    if row3[1] == "X":
        occupied = 1
    elif row3[2] == "X":
        occupied = 1
    elif row3[3] == "X":
        occupied = 1
    elif row3[4] == "X":
        occupied = 1

      if row4[1] == "X":
        occupied = 1
    elif row4[2] == "X":
        occupied = 1
    elif row4[3] == "X":
        occupied = 1
    elif row4[4] == "X":
        occupied = 1

    if row4[1] == "X":
        occupied = 1
    elif row4[2] == "X":
        occupied = 1
    elif row4[3] == "X":
        occupied = 1
    elif row4[4] == "X":
        occupied = 1

      if row5[1] == "X":
        occupied = 1
    elif row5[2] == "X":
        occupied = 1
    elif row5[3] == "X":
        occupied = 1
    elif row5[4] == "X":
        occupied = 1
        
      if row6[1] == "X":
        occupied = 1
    elif row6[2] == "X":
        occupied = 1
    elif row6[3] == "X":
        occupied = 1
    elif row6[4] == "X":
        occupied = 1
  
      if row6[1] == "X":
        occupied = 1
    elif row6[2] == "X":
        occupied = 1
    elif row6[3] == "X":
        occupied = 1
    elif row6[4] == "X":
        occupied = 1

    if occupied == 0:
        reserveSeat(row,seat)
    else:
           print(f"Seat is taken")

    reserveSeat(row,seat)

    anyMoreData = input("Would you like to reserve another seat?")
print("Program is finished!")