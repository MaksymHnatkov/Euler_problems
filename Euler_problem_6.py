# Euler problem 6:

sumSqrt = 0
sqrtSum = 0

for i in range (1,101):
    sumSqrt += i**2

for z in range (1,101):
    sqrtSum += z

sqrtSum = sqrtSum ** 2

answer = sqrtSum - sumSqrt

print(answer)
