def max_of_three(x,y,z):
    max = x
    if max < y: max = y
    if max < z: max = z
    return max
# print(max_of_three(1,3,7))

from array import array
import random

# print(random.randint(1,22))
def Input():
    n = int(input("Введите число: "))
    return n
# print(a%7==0 & a%23==0)

# for i in range(-n, n+1):
#    print(i)

# a=Input()
# b=Input()
# print(a*a==b or b*b==a)

def Square(n):
    for i in range(1,n+1):
        print(i,i*i)

def Coub(n):
    for i in range(1,n+1):
        print(i,i*i*i)

def Coub_even(n):
    for i in range(1,n+1):
        a=i*i*i
        if a%2==0: print(a)

# n=Input()
# Square(n)
# Coub(n)
# Coub_even(n)
