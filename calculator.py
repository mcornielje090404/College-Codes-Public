import os

def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x / y


def square(x):
    return x * x


def cube(x):
    return x * x * x


def calculator(choice):
    if choice == 0:
        print('Thank you for using my calculator')
        exit()
    elif choice in (1, 2, 3, 4):
        try:
            input2 = float(input('Enter your first number'))
            input3 = float(input('Enter your second number'))
        except ValueError:
            print('That input is not a  number')
            return calculator(input1)
        else:
            if choice == 1:
                return addition(input2, input3)
            elif choice == 2:
                return subtraction(input2, input3)
            elif choice == 3:
                return multiplication(input2, input3)
            elif choice == 4:
                return division(input2, input3)
    elif choice in (5, 6):
        try:
            input4 = float(input('Enter your number'))
        except ValueError:
            print('That input is not a  number')
            return calculator(input1)
        else:
            if choice == 5:
                return square(input4)
            elif choice == 6:
                return cube(input4)


def calculatorDisplay():
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Square')
    print('6. Cube')
    print('0. Exit')


while True:
    calculatorDisplay()
    try:
        input1 = int(input('Choose an option'))
    except ValueError:
        print('Input must be a number')
        input('Press any button to choose another option')
    else:
        print('The answer is', calculator(input1))
        input('Press any button to choose another option')
        os.system('cls')
