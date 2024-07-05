def bottles(num):
    if num > 99:
        print("The wall can fit, at most, 99 bottles of beer.")
    elif 2 < num < 100:
        print(str(num)+" bottles of beer on the wall,")
        print(str(num)+" bottles of beer,")
        print("Take one down, pass it around,")
        print(str(num-1)+" bottles of beer on the wall.")
        print("...")
        bottles(num-1)
    elif num == 2:
        print(str(num) + " bottles of beer on the wall,")
        print(str(num) + " bottles of beer,")
        print("Take one down, pass it around,")
        print(str(num - 1) + " bottle of beer on the wall.")
        print("...")
        bottles(num - 1)
    elif num == 1:
        print("1 bottle of beer on the wall,")
        print("1 bottle of beer,")
        print("Take one down, pass it around,")
        print("No more bottles of beer on the wall.")
        print("...")
        bottles(num-1)
    elif num < 1:
        print("No more bottles of beer on the wall,")
        print("No more bottles of beer")
        print("Go to the store and buy some more,")
        print("99 Bottles of beer on the wall.")


firsttime = True
while True:  # Loop until code reaches a break statement
    try:
        if firsttime:  # If this is your first time being prompted...
            # ... ask user how many bottles of beer are on the wall
            bottles(int(input("How many bottles of beer are on the wall?: ")))
            break  # Leave while loop if input is valid
        else:  # If this is not your first time through the loop
            bottles(int(input("Please enter an integer: ")))
            break
    except:  # If input is invalid...
        firsttime = False  # ...go through the loop again
