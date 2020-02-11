# Euler problem 2:

a = []
i = 1
s = 0

while (i + s) < 4000000:
    s += i
    i += s
    a.append(s)
    a.append(i) 

total_sum = 0
for i in a:
    if i % 2 == 0:
        total_sum += i


print(total_sum)


