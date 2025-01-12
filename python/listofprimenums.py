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


def listofprimes(num):
    if num < 2:
        raise ValueError("There are no prime numbers lower than 2.")
    allnum = []  # List will hold every number between 2 and the parameter
    lop = []  # List will hold all the prime numbers found between 2 and the parameter
    for x in range(2, num+1):  # For every number between 2 and the parameter...
        allnum.append(x)  # ...add that number to this list
    for j in range(len(allnum)):  # For every number in the list...
        if isitprime(allnum[j]):  # ...if that number is prime...
            lop.append(allnum[j])  # ...add it to the prime list
    return lop


firsttime = True
while True:  # Loop until code reaches a break statement
    try:
        if firsttime:  # If this is your first time being prompted...
            # ...prompt user to input the upper limit of the list
            print(listofprimes(int(input("List every Prime between 2 and what number?: "))))
            break  # Leave while loop if input is valid
        else:  # If this is not your first time through the loop
            print(listofprimes(
                int(input("Please enter an integer no lower than 2: "))))
            break  # Leave while loop if input is valid
    except ValueError:  # If input is invalid...
        firsttime = False  # ...go through the loop again
