def max_of_three(x,y,z):
    max = x
    if max < y: max = y
    if max < z: max = z
    return max
# print(max_of_three(1,3,7))

import random

# print(random.randint(1,22))

a = int(input("Введите число: "))
print(a%7==0 & a%23==0)

