repeat = True

while repeat == True:
    highestNumber = []
    num1 = int(input("Your first number: "))
    num2 = int(input("Your second number: "))
    num3 = int(input("Your third number: "))
    highestNumber.append(num1)
    highestNumber.append(num2)
    highestNumber.append(num3)
    print("The highest number you chose is", max(highestNumber))
    
