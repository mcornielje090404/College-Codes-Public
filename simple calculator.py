##Simple calculator

def callForNumber1():
    num = int(input("What is your first number?"))
    return(num)

def callForNumber2():
    num = int(input("What is your second number?"))
    return(num)

def addition(num1, num2):
    total = num1 + num2
    print(num1, "+", num2, "=", total)

def subtraction(num1, num2):
    total = num1 - num2
    print(num1, "-", num2, "=", total)

def multiply(num1, num2):
    total = num1 * num2
    print(num1, "x", num2, "=", total)

def divide(num1, num2):
    total = num1 / num2
    print(num1, "/", num2, "=", total)

userInput = input("What function would you like to use?")

if userInput == "1":
    num1 = callForNumber1()
    num2 = callForNumber2()
    addition(num1, num2)
elif userInput == "2":
    num1 = callForNumber1()
    num2 = callForNumber2()
    subtraction(num1, num2)
elif userInput == "3":
    num1 = callForNumber1()
    num2 = callForNumber2()
    multiply(num1, num2)
elif userInput == "4":
    num1 = callForNumber1()
    num2 = callForNumber2()
    divide(num1, num2)
    
    

                    
