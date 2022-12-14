# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# qqqwwgggg --> 3q2w4g
# 3q2w4g --> qqqwwgggg

# lst = 'qqqwwgggg'
# rle = list(lst)
# lst = []
# count = 1
# counter = 0
# for i in rle:
#     while rle[i] == rle[i+1]:
#         if rle[counter] == rle[counter+1]:
#             count += 1
#             counter += 1
#             if rle[counter] != rle[counter + 1]:
#                 lst.append(rle[i] * count)      # maybe rle[counter]

# print(lst)

input = 'qqqwwgggg'
tpl = set(input)
lst = list(tpl)             # 1 character list
input_lst = list(input)    # full list
print(input_lst)
print(lst)
out = []
for i in range(len(lst)):
    count = input_lst.count(lst[i])
    # lst.pop(int(i))
    out.append(lst[i] + str(count))
x = ''.join(out)
with open('file.txt', 'w') as data:
    data.write(x)
with open('file.txt', 'r') as data:
    decod = data.read()
