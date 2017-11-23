#Loop for number of bottles and print number of bottles
for n in range(99, -1, -1):
    print("99 bottles of beer on the wall, 99 bottles of beer.")
    print(f"Take one down, pass it around, {n} bottles of beer on the wall…\n")
    #If number bottles equal to 1 print this message
    if(n == 1):
        print("1 bottle of beer on the wall, 1 bottle of beer!")
        print("So take it down, pass it around, no more bottles of beer on the")
        print("wall!")
    #If number bottles less than zero print this message
    elif(n == 0):
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print("Go to the store and buy some more, 99 bottles of beer on the wall…")
