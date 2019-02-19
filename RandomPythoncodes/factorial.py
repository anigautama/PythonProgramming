#anil

import math
import time


def auto(number):
    return math.factorial(number)

n = int(input("Enter number:"))
fact_n = auto(n)
print(fact_n)

fact = n

print("Factorial of " + str(n) + "is: " + str(fact))


def rec(num):
    if num == 0:
        return 1
    else:
        return num * rec(num-1)


s_rec = time.time()
fact = rec(n)
e_rec = time.time()
t_rec = e_rec - s_rec
print("Time taken to solve recursively: %s" % (t_rec))

s_time = time.time()
for i in range(n, 0, -1):
    fact = fact * i
e_time = time.time()
t_time = e_time - s_time
print("Time taken to solve for loop: " + str(e_time - s_time))

if t_time < t_rec:
    print("loop is faster")
else:
    print("Recursive is faster")
