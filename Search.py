import random
import time


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = random.choice(range(1, 10))
print("Choice is", x)
def randomSearch(selection, x):
    start_time = time.time()
    count = 1
    print("Random Search")
    repeat = True
    while repeat == True:
        choice = random.choice(range(1, len(selection)-1))
        if choice == x:
            print(x, "Success")
            repeat = False
        else:
            print(choice, count)
            count += 1
    end_time = time.time()
    print("Time taken is", end_time - start_time, "seconds")
    print("")

def linearSearch(selection, x):
    start_time = time.time()
    count = 1
    print("Linear Search")
    for i in selection:
        if i == x:
            print(x, "Success")
            break
        else:
            print(i, count)
            count += 1
    end_time = time.time()
    print("Time taken is", end_time - start_time, "seconds")
    print("")


minimum = 0
maximum = len(list1)

def binarySearch(minimum, maximum, selection, x):
    if maximum >= minimum:
        mid = round((maximum + minimum) / 2)
        if mid == x:
            return(mid, "Success")
        elif mid > x:
            print(mid)
            return binarySearch(minimum, mid - 1, selection, x)
        elif mid< x:
            print(mid)
            return binarySearch(mid + 1, maximum, selection, x)

    else:
        return -1
randomSearch(list1, x)
linearSearch(list1, x)
start_time = time.time()
print(binarySearch(minimum, maximum, list1, x))
end_time = time.time()
print("The amount of time taken is", end_time - start_time, "seconds")
