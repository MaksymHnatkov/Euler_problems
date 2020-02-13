# Euler problem 7: NO SOLUTION YET!!!!!!

list1 = []
a = 2

while len(list1) != 30:
    k = 0
    for i in range(1,a):
        if a % i == 0:
            k += 1
            if k > 1:
                a += 1
            else:
                list1.append(a)
                a += 1

print(list1)









