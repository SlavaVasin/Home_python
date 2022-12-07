'''1) Вычислить число c заданной точностью d
Пример:
- при d = 0.001, π = 3.141   
Ввод: 0.01
Вывод: 3.14'''

# from math import pi
# d = input('Введите число с заданной точностью: ')
# d = d[2:len(d)]
# print(f'Вывод: {round(pi, len(d))}')


'''2) Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.'''

# def natural(n, d=2):
#     multipliers = []
#     while n > 1:
#         if n % d == 0:
#             multipliers.append(int(d))
#             n = n / d
#         else: 
#             d += 1
#     print(multipliers)


# n = int(input('Enter a number: '))
# natural(n)


'''3) Задайте последовательность чисел. Напишите программу, 
которая выведет список неповторяющихся элементов исходной последовательности.
Ввод: [1, 1, 2, 3, 4, 4, 4]
Вывод: [2, 3]'''

# def unik_list(list_x:list)->list:
#     list_2 = []
#     sor_list = sorted(list_x)
#     print(f'Дан список: \n {sor_list}')
#     for i in sor_list:
#         if sor_list.count(i) < 2:
#             list_2.append(i)
#     return print(f'Cписок неповторяющихся элементов: \n{list_2}')

# list_1 = list(map(int,input("Enter the numbers : ").strip().split()))
# unik_list(list_1)

'''4) Задана натуральная степень k. Сформировать случайным образом список 
коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
- k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.'''

# from random import randint
# from sympy import symbols
# from math import prod
 
# max_val=100
# k = int(input('Введите натуральную степень k:'))
# koeff=[randint(0 ,max_val) for i in range(k)]+[randint(1,max_val)]
# x = symbols('x')
# print (sum(map(prod,zip(koeff,[x**i for i in range(k+1)]))), '= 0')



'''5) Даны два файла, в каждом из которых находится запись многочлена. 
Задача - сформировать файл, содержащий сумму многочленов 
(складываются числа, у которых "х" в одинаковых степенях).'''