# n = int(input())
# m = int(input())
# arr = []
# arr.append(n)
# arr.append(m)
# print(arr)
# print(sum(arr))

# list_ = input()
# arr = []
# space_count = 0
# word = ""
# for i in list_:
#     if i != " ":
#         word += i
#     else:
#         arr.append(word)
#         word = ""
# arr += [word]
# print(arr[0], arr[-1])

# n = int(input())
# list_ = []
# for i in range(n):
#     if (i + 1) % 3 == 0 or (i + 1) % 5 == 0:
#         list_.append(i + 1)
# print(sum(list_))

line = input()
word = ""
arr_word = []
popular_word = ""
popular_word_count = 0
maybe_popular_word = ""
maybe_popular_word_count = 0
for i in line:
    if i != " ":
        word += i
    else:
        arr_word.append(word)
        word = ""
arr_word.append(word)
arr_numbers = [0] * len(arr_word)
for i in range(len(arr_word)):
    for j in range(len(arr_word)):
        if arr_word[i] == arr_word[j]:
            arr_numbers[i] += 1
print(arr_word[arr_numbers.index(max(arr_numbers))])
