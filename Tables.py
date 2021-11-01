from prettytable import PrettyTable

Table = PrettyTable(["", "List", "Array", "Tuple"])

Table.add_row(["Is it mutable?", "Yes", "Yes", "No"])
Table.add_row(["----------------------------------------------", "---------","---------","---------",])
Table.add_row(["Can we change the size after creation?", "Yes", "Yes", "No"])
Table.add_row(["----------------------------------------------", "---------","---------","---------",])
Table.add_row(["Can items in the liste be changed?", "Yes", "Yes", "No"])
Table.add_row(["----------------------------------------------", "---------","---------","---------",])
Table.add_row(["How many different types of data can be stored?", "All Types", "Similar Types", "All Types"])

print(Table)
