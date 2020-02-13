# Euler problem 7:

n = 10001
x = 2
lst = []
while (len(lst) < n):
    if all(x % i != 0 for i in lst):
        lst.append(x)
    x += 1
print(lst[-1])











