#Fills the square matrix with zerro over secondary diagonal, 1 on the secondary doagonal and 2 under secondary diagonal

n = int(input())

mtrx = [[0] * n for _ in range(n)]

i, j = 0, 0

while i < n:
    mtrx[n - i - 1][i] = 1
    j = i + 1
    while j < n:
        mtrx[n - i - 1][j] = 2
        j += 1
    i += 1
        
for i in range(n):
    print(*mtrx[i])
