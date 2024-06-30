def ctz(num):
    ctzlist = []  # Create a list for holding descending (or ascending) numbers
    if num == 0:  # If user enters 0
        print(0)
    elif num < 0:  # if user enters a number less than 0
        while num < 1:  # Loop until the count reaches 0
            ctzlist.append(num)  # Add the number to the list
            num = num + 1  # increase the number by one
    else:  # If user enters a number greater than 0
        while num > -1:  # Loop until the count reaches zero
            ctzlist.append(num)
            num = num - 1  # decrease the number by one
    # Print the list.  It should start with the entry and go in order until it reaches 0.
    print(*ctzlist, sep=', ')


firsttime = True
while True:  # Loop until code reaches a break statement
    try:
        if firsttime:  # If this is your first time being prompted...
            # ...prompt user to enter a number to start the countdown
            ctz(int(input("Begin countdown from what number?: ")))
            break  # Escape loop if input is valid
        else:  # If this is not your first time through the loop
            ctz(int(input("Please enter an integer: ")))  # Prompt user to enter valid input
            break  # escape loop if input is valid
    except:  # If input is invalid
        firsttime = False  # The next time through the loop is not the first time
