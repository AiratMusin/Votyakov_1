# def sum_numbers_in_arr(arr):
#     sum_ = 0
#     for i in arr:
#         sum_ += i;
#     return sum_

# def func(a, t1, t2):
#     if a >= t1 and a <= t2:
#         return "Да!"
#     else:
#        return "Нет!"
# print(func(int(input()), int(input()), int(input())))

# def is_perfect(a):
#     sum_ = 0
#     for i in range(1, a // 2 + 1):
#         if a % i == 0:
#             sum_ += i
#     if sum_ == a:
#         return True
#     else:
#         return False
# print(is_perfect(int(input())))

# def is_palindrom(a):
#     b = str(a)[::-1]
#     if a == int(b):
#         print("True")
#     else:
#         print("False")
# is_palindrom(int(input()))

# def is_prime(a):
#     for i in range(2, a // 2 + 1):
#         if a % i == 0:
#             return 0
#     return 1
# n = int(input())
# if is_prime(n):
#     print("True")
# else:
#     print("False")

# def fibonaci_(n):
#     f1 = 0
#     f2 = 1
#     if n == 1:
#         return f1
#     if n == 2 or n == 3:
#         return f2
#     else:
#         return fibonaci_(n - 2) + fibonaci_(n - 1)
# m = int(input())
# print(fibonaci_(m))