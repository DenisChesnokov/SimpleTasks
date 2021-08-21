# Fills the square matrix with zerro and 1 on mine and secondary diagonals
n = int(input())
str1 = []
mtrx = [[0] * n for _ in range(n)]

for i in range(n):
    mtrx[i][i] = 1
    mtrx[n - i - 1][i] = 1

for i in range(n):
    for j in range(n):    
        str1.append(str(mtrx[i][j]).ljust(3))
    print(*str1)
    str1.clear()
