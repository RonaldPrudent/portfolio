def isitprime(num):
    if num < 2:  # If the parameter is not greater than 1...
        return False  # ...it is not a prime number
    numlist = []  # List will hold, at most, every number between 2 and the parameter
    pnum = True  # Assume the parameter is prime until proven otherwise
    for x in range(2, num):  # For every number between 2 and the parameter...
        numlist.append(x)  # ...add the number to the list
        if num % numlist[x-2] == 0:  # If the parameter is divisible by that number...
            pnum = False  # ...it is not a prime number
            break  # Exit the loop
    return pnum  # return true or false; true if the parameter is prime


def listofprimes2(num):
    if num <= 0:
        raise ValueError
    else:
        lop = []  # List that will hold the first n prime numbers (n = parameter)
        count = 0  # Variable will keep track of the size of the list
        start = 2  # The first prime number is 2, so we start filling the list there
        while count < num:  # Loop until the list is the size of the parameter
            if isitprime(start):  # If the number we're on is prime
                lop.append(start)  # Add it to the list
                count = count + 1  # The size of the list has increased by one
                start = start + 1  # Iterate to the next number that may be added to the list
            else:  # If the number we're on is not prime
                start = start + 1  # Iterate to the next number to avoid an infinite loop
    return lop


firsttime = True
while True:  # Loop until code reaches a break statement
    try:
        if firsttime:  # If this is your first time being prompted...
            # ...prompt user to input how many of the first primes they want listed
            print(listofprimes2(int(input("How many prime numbers do you want listed?: "))))
            break  # Leave while loop if input is valid
        else:  # If this is not your first time through the loop
            print(listofprimes2(
                int(input("Please enter a positive integer: "))))  # Prompt the user again
            break  # Leave while loop if input is valid
    except ValueError:  # If input is invalid...
        firsttime = False  # ...go through the loop again
