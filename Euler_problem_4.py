# Euler problem 4:

list1 = []
for a in range (100,1000):
    for b in range (100,1000):
        c = a*b
        if (str(c)[0] == str(c)[-1]) and (str(c)[1] == str(c)[-2]) and (str(c)[2] == str(c)[-3]):
            list1.append(c)

print(max(list1))


