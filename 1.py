n = int(input("Введите количество экспонатов "))
m = int(input("Введите количество заходов "))
k = int(input("Введите максимальный вес который он может унести за 1 раз "))
w = list(map(int, input("Введите массы всех экспонатов ").split()))
c = list(map(int, input("Введите цены всех экспонатов ").split()))

weightcost = [[w[i], c[i]] for i in range(n)]

maxcost = [[0, [], 0] for i in range(m * k + 1)]

for j in range(m*k + 1):
    for i in range(n):
        cnt = j // k
        #print("j", j)
        if j - weightcost[i][0] < 0:
           # print(0, j - weightcost[i][0])
            continue
        if (j - weightcost[i][0]) % k == 0 and j - weightcost[i][0] > 0:
            #maxcost[j][2] += 1
            for q in range(j - weightcost[i][0] - k, j - weightcost[i][0] + 1):
                if maxcost[j][0] < maxcost[q][0] + weightcost[i][1] and (i not in maxcost[q][1]):
                    if maxcost[q][2] >= m:
                        continue
                    maxcost[j][0] = maxcost[q][0] + weightcost[i][1]
                    maxcost[j][1] = maxcost[q][1].copy()
                    maxcost[j][1].append(i)
                    maxcost[j][2] = maxcost[q][2] + 1
            continue
        if j - weightcost[i][0] == 0:
            maxcost[j][0] = weightcost[i][1]
            maxcost[j][1] = [i]
            maxcost[j][2] = 1
            continue
        if not (i in maxcost[j - w[i]][1]):
            if (j - weightcost[i][0]) // k != cnt:
                #print("k", j, j - weightcost[i][0])
                continue
            if maxcost[j][0] < maxcost[j - weightcost[i][0]][0] + weightcost[i][1]:
                #print("Hi")
                maxcost[j][0] = maxcost[j - weightcost[i][0]][0] + weightcost[i][1]
                maxcost[j][1] = maxcost[j - weightcost[i][0]][1].copy()
                maxcost[j][1].append(i)


print(max(maxcost)[0], "- максимальная стоимость украденного")
print(*max(maxcost)[1], "- номера украденных экспонатов")
print(maxcost)

