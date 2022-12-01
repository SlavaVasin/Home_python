'''1) Задайте список из нескольких чисел. 
Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.
Пример:
[2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12'''

# list_num = list(map(int, input('Введите числа через пробел: ').split()))
# print('\nСписок: ', list_num)

# def odd_indexes(list_x: list):
#     sum_list = []
#     for i in range(1, len(list_x), 2):
#         sum_list.append(list_x[i])
#     print(f"Сумма чисел, на нечётных идексах: {sum(sum_list)}")

# odd_indexes(list_num)

'''2) Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]'''

# list_num = list(map(int, input('Введите числа через пробел: ').split()))
# print('\nСписок: ', list_num)

# def multiplication_of_a_pair(list_x: list):
#     res_list = []
#     for i in range(int((len(list_x) + 1) / 2)):
#         mlt_n = list_x[i] * list_x[-1 - i]
#         res_list.append(mlt_n)
#     return res_list

# mult_list = multiplication_of_a_pair(list_num)
# print('Произведение пар чисел списка: ', mult_list)

'''3) Задайте список из вещественных чисел. Напишите программу, 
которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 10.01] => 0.19'''

# float_list = [1.1, 1.2, 3.1, 10.01]

# def result(list_x):
#     res_list =[]
#     for i in range(len(list_x)):
#         a = list_x[i] % 1
#         res_list.append(a)
#     result = max(res_list) - min(res_list)
#     print('Max значение', "%.2f" % max(res_list))
#     print('Min значение', "%.2f" % min(res_list))
#     print("Разница между max и min значением дробной части","%.2f" % result)

# result(float_list)

'''4) Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10'''

# number = int(input('Введите число: '))
# def bin_n(n:str):
#     b = ''
#     while n > 0:
#         b = str(n % 2) + b
#         n = n // 2
#     return b

# bin_num = bin_n(number)
# print(bin_num)

'''4) 2-ой вариант решения'''

# number = int(input('Введите число: '))
# def bin_n(n:str):
#     return bin(n).replace('0b','')
# print(bin_n(number))

'''5) Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: 
[-21 ,13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]'''


# def fibo(n):
#     if n >= 0:
#         idx = range(n + 1)
#         x = [0, 1]
#         for k in idx[2:]:
#             x.append(x[k - 1] + x[k - 2])

#         return x[n]
#     else:
#         n = -(n - 1)
#         idx = range(n + 1)
#         x = [1, 0]
#         for k in idx[2:]:
#             x.append(x[k - 2] - x[k - 1])
#         x.reverse()
#     return x[0]


# k = int(input('\nВведите число: '))
# fib_list = []

# for i in range(-k, k + 1):
#     fib_list.append(fibo(i))

# print(f'\nдля k = {k} список будет выглядеть так:\n')
# print(fib_list, '\n')
