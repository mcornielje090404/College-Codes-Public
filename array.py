import array as arr

while True:
    array = arr.array('i', [2, 3, 7, 5, 2, 2])

    counter = 0

    for i in range(0, len(array)):
        for j in range (i+1, len(array)):
            if (array[i] == array[j]):
                counter += 1

    removeelement = int(input("What number would you like to remove?"))
    try:
        array.remove(removeelement)
    except ValueError:
        print("That number is not in the array")
    print("The memory address of the array is", array.buffer_info())

    print("The number of duplicates in the array is", counter)

    print(array)

    array.reverse()

    print(array)
