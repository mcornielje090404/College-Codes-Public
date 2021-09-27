## A Simple calculator used to carry out simple tasks and functions

## Function to ask the user for the first number in the calculation and put it into the equation
def callForNumber1():
    num = int(input("What is your first number?"))
    return(num)

## Function to ask the user for the second number in the calculation and put it into the calculation
def callForNumber2():
    num = int(input("What is your second number?"))
    return(num)

## Function to add numbers put into the calculation
def addition(num1, num2):
    total = num1 + num2
    print(num1, "+", num2, "=", total)

##Function to subtract numbers put into the calculation
def subtraction(num1, num2):
    total = num1 - num2
    print(num1, "-", num2, "=", total)

## Function to multiply numbers into the calculation
def multiply(num1, num2):
    total = num1 * num2
    print(num1, "x", num2, "=", total)

## Function to divide numbers into the calculation
def divide(num1, num2):
    total = num1 / num2
    print(num1, "/", num2, "=", total)

## Variable used to determine wether the code should repeat
repeat = True

## While loop that repeats everytime the variable 'repeat' is set to true.
while repeat = True
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiply")
    print("4) Divide")
    
    repeat = False
    
## The users input used to determine the function required.
    userInput = input("What function would you like to use?")

## If and else statements to figure out which calculation is required then call for the numbers and use the correct function
    if userInput == "1":
        num1 = callForNumber1()
        num2 = callForNumber2()
        addition(num1, num2)
        repeat = True
    elif userInput == "2":
        num1 = callForNumber1()
        num2 = callForNumber2()
        subtraction(num1, num2)
        repeat = True
    elif userInput == "3":
        num1 = callForNumber1()
        num2 = callForNumber2()
        multiply(num1, num2)
        repeat = True
    elif userInput == "4":
        num1 = callForNumber1()
        num2 = callForNumber2()
        divide(num1, num2)
        repeat = True
    
    

                    
