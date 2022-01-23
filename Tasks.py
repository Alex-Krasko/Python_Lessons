from array import *
import random

# Задать массив из 8 элементов и вывести их на экран
# data = [0]*8
# for i in range(len(data)):
#     data[i] = random.randint(0,100)

# for i in data:
#     print(i)

# Задать массив из 8 элементов, заполеннный нулями и единицами
# data = [0]*8
# for i in range(len(data)):
#     data[i] = random.randint(0,1)

# for i in data:
#     print(i)

# Задать массив из 12 элементов, заполненных числами из [0,9]. Найти сумму положительных/отрицательных элементов массива
data = [0]*12
def Rndfill():
    for i in range(len(data)):
        data[i] = random.randint(-9,9)

def SummPol(array):
    a=0
    for i in array:
        if i>=0: a=a+i
    return a

def SummOtr(array):
    a=0
    for i in array:
        if i<0: a=a+i
    return a

Rndfill()
for i in data:
    print(i)
print('Сумма положительных: ', SummPol(data))
print('Сумма отрицательных: ', SummOtr(data))