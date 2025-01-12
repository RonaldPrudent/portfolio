def fibo(num):
    fiblist = [0, 1]  # The first two fibonacci numbers
    count = 2  # Current size of the list.  The list already has two numbers so the count is 2
    if num < 0:  # Input can't be negative
        raise ValueError  # Raise an error so user is prompted to enter a positive integer
    elif num == 0:  # If input is zero/a sequence with nothing in it
        print("")
    elif num == 1:  # A fibonacci sequence that is only one element long is 0
        print(0)
    elif num == 2:  # A fibonacci sequence that is only two elements long is 0 and 1
        print(*fiblist, sep=', ')  # Print the list (only 0 and 1 at this point)
    else:
        while count < num:  # Loop continues until list is the size that was input
            fiblist.append(fiblist[-1] + fiblist[-2])  # The next item in the list is the sum of the previous two
            count = count + 1  # Update variable since list just got one element bigger
        print(*fiblist, sep=', ')  # Print the list


firsttime = True
while True:  # Loop until code reaches a break statement
    try:
        if firsttime:  # If this is your first time being prompted...
            # ...prompt user to input the length of the list
            fibo(int(input("How many numbers in this sequence?: ")))
            break  # Leave while loop if input is valid
        else:  # If this is not your first time through the loop
            fibo(int(input("Please enter a positive integer: ")))
            break  # Leave while loop if input is valid
    except ValueError:  # If input is invalid...
        firsttime = False  # ...go through the loop again
