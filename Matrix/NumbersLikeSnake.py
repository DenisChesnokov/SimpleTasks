#Fills the matrix n * m with a numbers from 1 to m like a snake
n, m = map(int, input().split())

mtrx = [[0] * m for _ in range(n)]


count = 1
i, j = 0, 0

for i in range(n):
    if i % 2 > 0:
        j = m - 1
        while j >= 0:
            mtrx[i][j] = count
            count += 1
            j -= 1
    else:
        for j in range(m):
            mtrx[i][j] = count
            count += 1
            
for i in range(n):
    for j in range(m):
        print(str(mtrx[i][j]).ljust(3), end = ' ')
    print()
