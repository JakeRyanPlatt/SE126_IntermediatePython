def seatMap():
    for r in range(1,8):
        print(r," ",end="")
        for s in range(1,5):
            if s == 3: #aisle seat spacing
                print(" ", row[r][s]," ",end="")
            else:
                print(row[r][s], " ", end="")
        print()
    return


def seatReserve(r,s):
    print(r,s)
    print(r + 4)
    if row[r][s] != "X":
        row[r][s] = "X"
        return(0)
    else:
        return 1

row = [
    ["Z", "Z", "Z", "Z", "Z"],
    ["0", "A", "B", "C", "D"],
    ["0", "A", "B", "C", "D"],
    ["0", "A", "B", "C", "D"],
    ["0", "A", "B", "C", "D"],
    ["0", "A", "B", "C", "D"],
    ["0", "A", "B", "C", "D"],
    ["0", "A", "B", "C", "D"]
    ]

seatMap()
anyMoreData = "Y"
while anyMoreData == "Y":
    seatMap()
    row = int(input("Which row"))        
    seat = input(f"Which seat in row {row} would you like to sit in ? ")

    seatNumber = ord(seat) - 64
    reservation = seatReserve(row, seatNumber)

     
    if reservation == 0:
        print("Seat has been reserved")
    else:
        print("Seat Unavailable")

    #reserveSeat(row,seat)

    anyMoreData = input("Would you like to reserve another seat?")
print("Program is finished!")
