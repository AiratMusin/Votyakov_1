# for i in range(1, 11):
#     for j in range(1, 11):
#         if (i * j) // 10 == False:
#             print(f" {i * j}", end=" ")
#         else:
#             print(i * j, end=" ")
#     print("\n")

# task2
# count = 0
# l = int(input())
# r = int(input())
# for i in range(l, r + 1):
#     for j in range(l, r + 1):
#         root = int((j ** 2 + i ** 2) ** 0.5)
#         if (i ** 2 + j ** 2 <= r ** 2) and (root * root == i ** 2 + j ** 2):
#             count += 1
# print(count)

# n = int(input())
# sum_of_divisors1 = 0
# sum_of_divisors2 = 0
# arr = []
# for i in range(1, n + 1):
#     for j in range(1, n // 2 + 1):
#         if i % j == 0 and i != j:
#             sum_of_divisors1 += j
#     for k in range(1, n // 2 + 1):
#         if sum_of_divisors1 % k == 0 and sum_of_divisors1 != k:
#             sum_of_divisors2 += k
#     if sum_of_divisors2 == i and sum_of_divisors1 != i:
#         arr.append(i), arr.append(sum_of_divisors1)
#     sum_of_divisors1 = 0
#     sum_of_divisors2 = 0
# k = 1
# for item in list(dict.fromkeys(arr)):
#     if k % 2:
#         print(item, end=" ")
#         k += 1
#     else:
#         print(item, end=" \n")
#         k += 1

# n = int(input())
# sum_n = 0
# for i in range(10 ** (n - 1), 10 ** n - 1):
#     string_n = str(i)
#     for j in string_n:
#         sum_n += (int(j)) ** n
#     if i == sum_n:
#         print(f"{i} - Armstrong's number")
#     sum_n = 0
#     str_n = ""