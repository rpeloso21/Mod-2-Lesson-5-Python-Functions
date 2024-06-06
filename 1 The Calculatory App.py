# Tasks 1

def addition():

    sum = 0

    while True:
        try:
            number = int(input("Please, type a single number that you would like to add to the sum.  When you are finished, please type DONE"))
            sum += number
        except ValueError:
            break
    print(f"The sum of your numbers is {sum}.")

def subtraction():
    minuend = int(input("Please enter your minuend: "))
    subtrahend = int(input("Please enter your subtrahend: "))
    difference = minuend - subtrahend

    print(f"Your difference is {difference}.")

def multiplication():

    numbers = input("Please enter the numbers that you would like to multiply seperated by a space: ").split()

    x = 1
    for number in numbers:
        x *= int(number)
    
    print(f"The product of your factors is {x}.")

def division():
    dividend = float(input("Please enter the dividend: "))
    divisor = float(input("Please enter the divisor: "))
    quotient = dividend/divisor

    print(f"The answer is {quotient}")

while True:
    # Task 2
    operation = input("What operation would you like to perform? (addition, subtraction, multiplication, division)")

    if operation == "addition":
        addition()
    elif operation == "subtraction":
        subtraction()
    elif operation == "multiplication":
        multiplication()
    elif operation == "division":
        # Task 3
        try:
            division()
        except ZeroDivisionError:
            print("You cannot divide by zero.")
    else:
        print("That is not a valid operation.")
        break

        
#addition()
#subtraction()
#multiplication()
#division()