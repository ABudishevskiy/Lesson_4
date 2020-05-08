# Дан массив целых чисел. Нужно найти сумму элементов с индексами подходящими под правило.
# Правило такое - сумма бит двоичного представления четна.
# Затем перемножить эту сумму и предпоследний элемент исходного массива.
import random
a = []
for i in range(100):
    a.append(random.randint(0, 10000))
print(a)
countelemen = 0
for i in range(len(a)):
    countbit = 0
    for l in bin(i)[2:]:
        countbit = countbit + int(l)
    if countbit % 2 == 0:
        countelemen = countelemen + a[i]
print(countelemen*a[-2])



#     countbit = 0
#     for l in bin(a.index(i, countindex))[2:]:
#         countbit = countbit + int(l)
#     if countbit % 2 == 0:
#         countelemen = countelemen + i
#         print(countelemen)
#     countindex = countindex + 1
# print(countelemen*a[-2])