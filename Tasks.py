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
# data = [0]*12
# def RndFill():
#     for i in range(len(data)):
#         data[i] = random.randint(-9,9)

# def SummPol(array):
#     a=0
#     for i in array:
#         if i>=0: a=a+i
#     return a

# def SummOtr(array):
#     a=0
#     for i in array:
#         if i<0: a=a+i
#     return a

# Rndfill()
# for i in data:
#     print(i)
# print('Сумма положительных: ', SummPol(data))
# print('Сумма отрицательных: ', SummOtr(data))

# Определить, присутствует ли в заданном массиве, некоторое число
# data = [0]*20
# def RndFill():
#     for i in range(len(data)):
#         data[i] = random.randint(-10,20)
# RndFill()
# def Input():
#     a = int(input('Введите искомое число: '))
#     return a

# def Find(array, a):
#     b=False
#     for i in array:
#         if i==a: b=True
#     print(b)

# a = Input()
# print(data)
# Find(data, a)

# В одномерном массиве из 123 чисел найти количество элементов из отрезка [10,99]
# data = [0]*123
# def RndFill():
#     for i in range(len(data)):
#         data[i] = random.randint(-100,300)
# RndFill()

# def Find(array):
#     b=0
#     for i in array:
#         if i>=10 and i<=99: b+=1
#     return b
# print('Количество числе в массиве: ', Find(data))

# data = [0]*10
# def ArrayFill(array):
#     for i in range(len(array)):
#         array[i] = random.randint(-100,100)
#     return array

# def ArrayInvert(array):
#     for i in range(len(array)):
#         array[i] = -array[i]
#     return array

# print(ArrayFill(data))
# print(ArrayInvert(data))

# def CreateRndArray(min, max,lens):
#     array = [0]*lens
#     for i in range(len(array)):
#         array[i] = random.randint(min,max)
#     return array
