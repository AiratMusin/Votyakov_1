# n = int(input())
# for i in range(n + 1):
#     if i % 3 == 0 and i % 6 != 0:
#         print(i)

# n = int(input())
# for i in range(10, n + 1):
#     if (i % 10) % 2 == 0:
#         print(i)

# n = int(input())
# summa = 0
# if n % 2 == 0:
#     print(n // 2)
# else:
#     for i in range(n + 1):
#         if (i % 2) == 1:
#             summa += i
#     print(summa)

# n = int(input())
# counter = 0
# if n % 3 == 0:
#     m = int(input())
#     for i in range(1, n + 1):
#         if i % m == 0:
#             counter += 1
#     print(counter)
# else:
#     for i in range(1, n + 1):
#        print(n ** i, end= " ")

a = int(input())
b = int(input())
n = int(input())
counter = 0
for i in range(n):
    c = int(input())
    if c == (a ** 2 + b ** 2) ** 0.5:
        counter += 1
    if c > 10 and (c % 3 == 0 or c % 4 == 0):
        print(f"{c} - YES!")
    else:
        print(f"{c} - NO!")
print(f"Итоговое количество - {counter}")
