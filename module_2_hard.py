n = int(input())
r = []
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if n % (i + j) == 0:
            t = [i, j]
            t1 = [j, i]
            if t1 not in r and i != j:
                r.append(t)
result = []
for i in r:
    result.extend(i)
print(*result, sep='')



