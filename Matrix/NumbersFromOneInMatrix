#Fills the matrix n*m with numbers from 1 to n*m
dimentions = input().split() #3 3 or 3 4 for example
n = int(dimentions[0])
m = int(dimentions[1])

mtrx = [[0] * m for _ in range(n)]

count = 1

str1 = []

#Fills the matrix
for i in range(n):
    for j in range(m):
        mtrx[i][j] = count
        count += 1

#Prepare to output
for i in range(n):
    for j in range(m):
        str1.append(str(mtrx[i][j]).ljust(3))
    print(*str1)
    str1.clear()
