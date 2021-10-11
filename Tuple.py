
tuplelist = ("2","3","4","5")
tupleinput = tuple(input("Enter an input"))

print("".join(tuplelist))
print(tupleinput)

inputcheck = input("What element would you like to check")
if inputcheck in tuplelist:
    print("That element is in the tuple")
else:
    print("That element is not in the tuple")
