#For loop to append 1000 numbers to a list
list1 = []
for i in range(1000):
    list1.append(i)
print(list1)

#List comprehension for above loop
list2 = [i for i in range(1000)]
print(list2)

#List that contains every  number divsible by eight from 1 - 1000
list3 = [i for i in range(1000) if i % 8 == 0]
print(list3)

#List that contains every number containing 6 from 1 - 1000
list4 = [i for i in range(1000) if "6" in list(str(i))]
print(list4)
