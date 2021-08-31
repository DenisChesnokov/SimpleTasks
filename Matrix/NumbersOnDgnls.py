#Fills diagonals of the matrix n * m with numbers from 1 to n * m.

n, m = map(int, input().split())

d_len = min(n, m)

count = 1 

diagonals = []

mtrx = [[0] * m for _ in range(n)]

#Fills list of diagonals

for k in range(n + m -1):
    if k < d_len: #Fills diagonals less than maximum diagonal lenth
        diagonals.append([count])
        count += 1
        for i in range(k):
            diagonals[k].append(count)
            count += 1 
            
    elif d_len <=k and k < m: #Fills diagonals equal maximum diagonal lenth
        diagonals.append([count])
        count += 1
        for i in range(d_len - 1):
            diagonals[k].append(count)
            count += 1 
            
    elif m <= k and k < n + m: #Fills diagonals less than maximum diagonal lenth in end of the matrix
        diagonals.append([count])
        count += 1
        for i in range(1, min(d_len, n + m - k - 1)):
            diagonals[k].append(count)
            count += 1 

#Fills diagonals of the matrix
for i in range(n):
    for j in range(m):
        mtrx[i][j] = diagonals[j][0]
        diagonals[j].pop(0)
    diagonals.pop(0)

#Print the matrix
for i in range(n):
    for j in range(m):
        print(str(mtrx[i][j]).ljust(3), end=' ')
    print()
