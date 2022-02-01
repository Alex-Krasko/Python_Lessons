# def f(x):
#     return x**2

# g = f
# print(type(g))

# def calc(x):
#     return x*10

# print(calc(10))

# def math(op, x):
#     print(op(x))

# math(calc,10)

# def sum(x,y):
#     return x+y

# def mylt(x,y):
#     return x*y

# def calc(op,a,b):
#     print(op(a,b))
#     return op(a,b)

# sum = lambda x, y: x+y+1  ## Лямбда

# calc(lambda x, y: x+y+1,4,5)

# list = []

# for i in range(1,101):
#     # if(i%2==0):
#     list.append(i)

# def f(x):  ## List comprehension
#     return x**3
# list = [(i, f(i)) for i in range(1,21) if i%2==0]

# print(list)

# def select(f, col):  ## Лямбда + List comprehension
#     return [f(x) for x in col]

# def where(f,col):
#     return [x for x in col if(f(x))]

# data = '1 2 3 5 8 15 23 38'.split()

# res = select(int,data)
# res = where(lambda x: not x%2, res)
# res = select(lambda x:(x, x**2), res)
# print(res)

# li = [x for x in range(1,20)]
# li = list(map(lambda x: x+10,li))

# print(li)

# data = list(map(int,'1 2 3 4 555 6'.split()))
# print(data)

# for e in data:
#     print(e)

# print('--')

# for e in data:
#     print(e)

# data = [x for x in range(10)]
# res = list(filter(lambda x: not x%2, data))
# print(res)