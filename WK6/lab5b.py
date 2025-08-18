def binary_search(tTarget):
    tLow = 0
    tHigh = len(names) - 1
    guess = (tLow + tHigh) // 2 #// is a floor division operator

    while tLow <= tHigh and names[guess] != tTarget:
        if names[guess] > tTarget:
            tHigh =  guess - 1
        else:
            tLow  = guess + 1

        guess = (tLow + tHigh) // 2

   
    if tLow <= tHigh:
        return guess
    else:
        return -5.2


#============ Main Program ===============

names = ["Adam","Bob","Carole","Donna","Ed", "Edith","Frank","Karen"]

target = input("Enter a name ... ")

found = binary_search(target)

if found == -5.2:
    print("Not on the list!!!")
else:
    print("Found it: ", names[found], "Position:", found)





            

