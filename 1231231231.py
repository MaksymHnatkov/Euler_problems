list1 = []
a = 2
k = 0

while len(list1) != 10001:
    for a in range(a-1, a+1):
        if a % 2 == 0:
            a += 1
        elif a % 3 == 0:
            a += 1
        elif a % 4 == 0:
            a += 1
        elif a % 5 == 0:
            a += 1
        elif a % 6 == 0:
            a += 1
        elif a % 7 == 0:
            a += 1
        elif a % 8 == 0:
            a += 1
        elif a % 9 == 0:
            a += 1
        elif a % 10 == 0:
            a += 1
        elif a % 11 == 0:
            a += 1
    for i in range(1, a):
        if a % i == 0:
            k += 1
    if k > 1:
        a += 1
    else:
        list1.append(a)
        a += 1

print(list1[-1])