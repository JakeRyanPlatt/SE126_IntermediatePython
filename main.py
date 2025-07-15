# Import Modules
import os
import random
#=============Functions============#
def roll_dice():  #function returns some of 2d6
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    sum = d1 + d2
    return sum

def win_loss_ratio():
        winloss =  (win/count)
        return winloss
#=============Global Variables============#
count = 0# Couynts number of rounds
win = 0 # Counts number of wins
point = 0 # Holds the point value if a point is established

#==================MAIN===================#
print("")
print("")
print("")
print("     ▄████████    ▄████████    ▄████████  ▄█  ███▄▄▄▄    ▄██████▄ ")
print("    ███    ███   ███    ███   ███    ███ ███  ███▀▀▀██▄ ███    ███")
print("    ███    █▀    ███    ███   ███    █▀  ███▌ ███   ███ ███    ███")
print("    ███          ███    ███   ███        ███▌ ███   ███ ███    ███")
print("    ███        ▀███████████ ▀███████████ ███▌ ███   ███ ███    ███")
print("    ███        ▀███████████ ▀███████████ ███▌ ███   ███ ███    ███")
print("    ███    ███   ███    ███    ▄█    ███ ███  ███   ███ ███    ███")
print("    ████████▀    ███    █▀   ▄████████▀  █▀    ▀█   █▀   ▀██████▀ ")
print("")
print("")
print("   ▄████████    ▄████████    ▄████████    ▄███████▄    ▄████████")
print("   ███    ███   ███    ███   ███    ███   ███    ███   ███    ███")
print("   ███    █▀    ███    ███   ███    ███   ███    ███   ███    █▀ ")
print("   ███         ▄███▄▄▄▄██▀   ███    ███   ███    ███   ███       ")
print("   ███        ▀▀███▀▀▀▀▀   ▀███████████ ▀█████████▀  ▀███████████")
print("   ███    █▄  ▀███████████   ███    ███   ███                 ███")
print("   ███    ███   ███    ███   ███    ███   ███           ▄█    ███")
print("   ████████▀    ███    ███   ███    █▀   ▄████▀       ▄████████▀ ")
print("                ███    ███                                       ")
print("")
print("")
print("")
#=================Game Logic=================#

while count < 10000:
    roll_one = roll_dice()

    if roll_one == 7 or roll_one == 11:
        count += 1
        win += 1
    elif roll_one == 2 or roll_one == 3 or roll_one == 12:
        count += 1
        win -= 1
    else:  # Point condition
        point = roll_one
        flag = 1
        while flag == 1:
            roll_two = roll_dice()
            if roll_two == point:
                count += 1 
                win += 1
                flag = 0
            elif roll_two == 7:
                count += 1
                win -= 1     
                flag = 0

print("Total Rounds:", count)
print(f"Win/Loss Ratio: {win_loss_ratio()*100:.2f}%")





