inf = 10 ** 9 + 7


def MinScalMatrix(dims, i, j):
    if j <= i + 1:
        return 0

    minim = inf

    for k in range(i + 1, j):
        left_min = MinScalMatrix(dims, i, k)
        right_min = MinScalMatrix(dims, k, j)
        cost = left_min + right_min + dims[i] * dims[k] * dims[j]
        if cost < minim:
            minim = cost
    return minim


dims = list(map(int, input("Введите через пробел количество ячеек в каждой матрице: ").split()))
print("Минимальное количество скалярных операций равно:", MinScalMatrix(dims, 0, len(dims) - 1))
