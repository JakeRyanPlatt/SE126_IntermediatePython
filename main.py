# Import Modules
import random
#=============Functions============#
def roll_dice():  #function returns some of 2d6
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    sum = d1 + d2
    return sum

def win_loss_ratio():
        winloss =  (win+loss) / games
        return winloss
#=============Global Variables============#
loss = 0 # Counts number of rounds
win = 0 # Counts number of wins
games = 0
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

while games < 10001:
    
    roll_one = roll_dice() # 1 location to roll the dice

    if roll_one == 7 or roll_one == 11:
        win += 1
    elif roll_one == 2 or roll_one == 3 or roll_one == 12:
        loss += 1  # This might be ruining the win loss ratio
    else:  # Point condition
        point = roll
        roll = roll_dice()
        while roll != point and roll != 7:
                roll = roll_dice() # second location to roll the dice
        if roll == point:
                win += 1
        elif roll == 7:
                win -= 1     
    games = games + 1
 
#=================End of Game Logic=================#
print("win = ", win, "Games = ", games)
print("Total Rounds:", point)
print(f"Win/Loss Ratio: {win_loss_ratio():.2%}")





