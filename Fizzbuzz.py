## FizzBuzz

integers = 1


##While loop that decides wether to print "Fizz", "Buzz", "FizzBuzz" or integers
while integers <= 50:
    fizz = integers % 3
    buzz = integers % 5
    fizzbuzz = fizz + buzz
    if fizzbuzz == 0:
        print("FizzBuzz")
    elif buzz == 0:
        print("Buzz")
    elif fizz == 0:
        print("Fizz")
    else:
        print(integers)
    integers = integers + 1

    
    

