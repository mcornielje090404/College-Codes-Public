bill = int(input())
discount = bill * 10.0/100 if bill >= 1000 else bill * 5.0/100
print(bill - discount)
