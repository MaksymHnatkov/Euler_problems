# Euler problem 5:

a = 0
b = 0
while a != 20:
    a = 0
    b += 2520
    for i in range(1,21):
        if b % i == 0:
            a += 1

print(b)









