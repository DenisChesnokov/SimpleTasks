#Fills the square matrix with 0 and 1 as sandglass

n = int(input())
str1 = []

i,j = 0, 0

mtrx = [[0] * n for _ in range(n)]

for i in range(n):
    j = i
    while j < n - i:
        mtrx[i][j] = 1
        j += 1
    
    j = n - i - 1
    while j < i + 1:
        mtrx[i][j] = 1
        j += 1
        
for i in range(n):
    for j in range(n):
        str1.append(str(mtrx[i][j]).ljust(3))
    print(*str1)
    str1.clear()
