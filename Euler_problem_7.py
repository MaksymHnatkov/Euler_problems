# Euler problem 7:

def primes():
    n = 10001
    x = 2
    lst = []
    while (len(lst) < n):
        if all(x % i for i in lst):
            lst.append(x)
        x += 1
    print(lst[-1])

primes()









