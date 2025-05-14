import copy
import sys
from reprlib import recursive_repr

# №2
# def function():
#     arr = []
#     for i in range(5):
#         arr.append(int(input()))
#     arr1 = arr[:]
#     arr2 = arr.copy()
#     arr3 = copy.copy(arr)
#     arr4 = copy.deepcopy(arr)
#     arr5 = list(arr)
#     return 0
# function()
# №4
# def repetition_of_elements(arr, obj):
#     count = 0
#     for j in arr:
#         if j == obj:
#             count += 1
#     return count
#
#
# animals = ["cat", "cat", "dog", "dog", "bird",
#            "capybara", "capybara", "capybara"]
# dict1 = {obj: repetition_of_elements(animals, obj) for obj in animals}
# print(dict1)
# sum1 = 0
# for k in animals:
#     print(f"{sys.getrefcount(k)} - {k}")
# for r in range(3):
#     sum1 += sys.getrefcount(r)
# print(sum1)

# №5
# sum1 = 0
# sum2 = 0
# backpack = ["capybara", "capyraba", "capyba", "capyba", "capybara",
# 2999, 2999, "capybara", [7, 7, 7], [7, 7, 7], [7, 7, 7],
# [7, 7, 7]] + [[8, 8]] * 5
# for i in range(len(backpack)):
#     for j in range(i + 1, len(backpack)):
#         if backpack[i] is backpack[j]:
#             sum1 += 1
# for i in range(len(backpack)):
#     for j in range(i + 1, len(backpack)):
#         if backpack[i] == backpack[j]:
#             sum2 += 1
#
# print(sum1, sum2)

# №6

recursive_salad = ["lettuce", "chicken", "cheese", "sauce", "tomatoes", "croutons"]
recursive_salad.append(recursive_salad)
recursive_salad[6].append("salt")
recursive_salad[6].append("pepper")
print(recursive_salad[4])
print(recursive_salad[-1])

