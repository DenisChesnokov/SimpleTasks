#Fills the square matrix with 1,..,n numbers by a circle 

str1 = input().split()
n = int(str1[0])
m = int(str1[1])

mtrx = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        mtrx[i][j] = (i + j) % m + 1

str1.clear()

for i in range(n):
    for j in range(m):
        str1.append(str(mtrx[i][j]).ljust(3))  
    print(*str1)
    str1.clear()
