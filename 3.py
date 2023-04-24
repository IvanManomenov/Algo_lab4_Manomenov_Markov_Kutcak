from random import *

n = int(input("Введите длину массива "))
N = [randint(-100, 100) for i in range(n)]
print("Исходный массив:", *N)
maxps = [0 for j in range(n)]
maxps[0] = 1
endmax = 0
for i in range(1, n):
    if N[i] >= N[i - 1]:
        maxps[i] = maxps[i - 1] + 1
    else:
        maxps[i] = 1
    if maxps[endmax] < maxps[i]:
        endmax = i
print("Максимальная длина неубывающей непрерывной подпоследовательности:", maxps[endmax])
print("Самая длинная неубывающая непрерывная подпоследовательность:", *N[endmax - maxps[endmax] + 1:endmax + 1])
