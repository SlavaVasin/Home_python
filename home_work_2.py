'''1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
0,56 -> 11'''
# number = float(input("Enter a number: "))
# sum = 0
# for i in str(number):
#     if i != '.':
#         sum += int(i)
# print(sum)

'''2 - Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Пример:
пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)'''
# n = int(input("Eneter a number: "))
# lis = []
# fact = 1
# for i in range(1, n + 1):
#     if i == 1:
#         lis.append(i)
#     else:
#         fact = i * fact
#         lis.append(fact)
# print(lis)

'''3 - Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
Пример:
Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06'''
# n = int(input('Enter a number: '))
# sum_num = 0
# result = 0
# d = {}
# for i in range(1, n + 1):
#     sum_num = round((1 + 1 / i)**i, 2)
#     result += sum_num
#     d[i] = sum_num
# print(d)
# print('Сумма ' + str(round(result, 2)))

'''4 - Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
n = 3
[-3, -2, -1, 0, 1, 2, 3]
--> 0 2 3
-3 * -1 * 0 = 0
Вывод: 0'''
# n = int(input("Enter a number: "))
# list_num = []
# prod = 1
# for i in range(-n, n + 1):
#     list_num.append(i)
# print(list_num)

# find = input('index --> ').split()

# for value in range(len(find)):
#     sr = int(find[value])
#     prod *= list_num[sr]
# print(f"Total: {prod}")

'''5 - Реализуйте алгоритм перемешивания списка.'''
# import random

# list_x = list(map(int, input().split()))
# print(f"First: {list_x}")
# length = len(list_x)
# for i in range(length):
#     index = random.randint(0, length - 1)
#     temp = list_x[i]
#     list_x[i] = list_x[index]
#     list_x[index] = temp
    
# print(f"Second: {list_x}")
