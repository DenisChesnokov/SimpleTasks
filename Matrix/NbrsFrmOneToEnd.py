#Fills the matrix from one to n * m by column
str1 = input().split()

n = int(str1[0])
m = int(str1[1])

mtrx = [[0] * m for _ in range(n)]

count = 1

for j in range(m):
    for i in range(n):
       mtrx[i][j] = count
       count += 1

for i in range(n):
    print(*mtrx[i]) 