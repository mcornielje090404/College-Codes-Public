import time

def sum_of_n(n):
    start = time.time()
    print(n*(n+1)/2)
    end = time.time()
    Time = end - start
    print(Time)

sum_of_n(10)
