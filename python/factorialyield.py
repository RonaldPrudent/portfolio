import math  # statement that allows use of Python's prod function.


def fyhelper(num):
    for x in range(1, num+1):  # Loop until you reach the indicated stopping point
        yield x  # "return" the number/add it to the list


def factorialy(num):
    if num < 0:  # If the parameter is negative
        return "undefined"  # Negative numbers don't have factorials
    return math.prod(list(fyhelper(num)))  # Multiply all the numbers in the list together


firsttime = True
while True:  # Loop until valid input is entered
    try:
        if firsttime:  # if this is your first time through the loop
            uinp = int(input("Find the factorial of what number?: "))  # Prompt the user for input
            break  # Escape loop if input is valid
        else:  # If this is not your first time through the loop
            uinp = int(input("Please enter an integer: "))  # Prompt the user again with more specific instructions
            break
    except:  # if input is invalid
        firsttime = False  # The next time through the loop is not your first


print(str(uinp) + "! = " + str(factorialy(uinp)))  # Print the factorial of the number entered by the user
