# Задача 2
# password1 = input()
# password2 = input()
# if password1 == password2:
#     print("True")
# else:
#     print("False")

# Задача 3
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# print(min(a, b, c, d))

# Задача 4

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# print(max(a, b, c, d))

# Задача 5

# a = int(input())
# b = int(input())
# c = int(input())
# if a + b <= c or a + c <= b or b + c <= a:
#     print("False")
# else:
#     print("True")

# Задача 6

# a = int(input())
# b = int(input())
# c = int(input())
#
# if a + b >= c or a + c >= b or b + c >= a:
#     print("Вырожденный")
# elif a == b == c:
#     print("Равносторонний")
# else:
#     print("Разносторонний")

# Задача 7
# На вход с клавиатуры подаются 4 числа: a, b, c и d. Даны два отрезка на числовой
# прямой [a, b] и [c, d], соответственно a ≤ b и c ≤ d. Напишите программу, которая
# считает количество целых точек, являющихся пересечением этих отрезков с учётом
# границ. В ответе запишите результат работы программы для a = 3, b = 13, c = 7
# и d = 1

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# if a > b or c > d:
#     print("Error data")
# else:
#     if b < c:
#         print("0")
#     if b == c:
#         print("1")
#     if b > c:
#         if a < d:
#             print(b - c + 1)
#         if a == d:
#             print("1")
#         if a > d:
#             print(a - d + 1)

