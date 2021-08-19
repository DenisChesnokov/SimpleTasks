#Chess order of dots and dtsrs
#Inputs matrix dimentions in one line with a space

str1 = input().split()
n = int(str1[0])
m = int(str1[1])

mtrx = [['*'] * m for _ in range(n)]

i,j = 0, 0

for i in range(n):
    j = (i + 2) % 2 
    while j < m:
        mtrx[i][j] = '.'
        j += 2
    j = 0

for i in range(n):
    print(*mtrx[i])
