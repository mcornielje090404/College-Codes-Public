list1 = [1, 2, 3]
list2 = ["Hello", "Goodbye", "How are you?"]


#Prints list1
print (list1)

#Combines list1 and list2
print (list1 + list2)

#Squares all the elements of list1 and prints them
for i in list1:
    print(i ** 2)

#Combines list1 and list2 using the zip function
listtogether = zip(list1, list2)
print(list(listtogether))

#Reverse list1
list1.reverse()
print(list1)

input()

    

