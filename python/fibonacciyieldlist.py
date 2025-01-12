def fibyield(num):
    a, b = 0, 1  # Start with the first two numbers of the sequence
    for i in range(0, num):  # Loop until you reach the indicated stopping point
        yield a  # "return" the variable/Add it to a list.
        a, b = b, a + b  # Update the variables so that the next number is the sum of the previous 2


firsttime = True
while True:  # Loop until code reaches a break statement/loop until there is valid input
    try:
        if firsttime:  # if this is your first time through the loop
            fiblen = int(input("How many numbers in this sequence?: "))  # Prompt user for input (sequence length)
            if fiblen < 0:  # If user inputs a negative number
                raise ValueError  # Raise an error so user is prompted again
            break  # Escape loop if input is valid
        else:  # if this is not your first time through the loop
            fiblen = int(input("Please enter an integer: "))  # Prompt user again with specific instructions
            if fiblen < 0:
                raise ValueError
            break
    except ValueError:  # If input is invalid...
        firsttime = False  # ...go through the loop again


fylist = list(fibyield(fiblen))  # Put the sequence into a list
print(*fylist, sep=", ")
