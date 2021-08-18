n = int(input())
sqr = [[0] * n for _ in range(n)]
sqr_line = [(i + 1) for i in range(n * n)]
str1 = []
status = 'YES' 
i, j = 0, 0

# Get square and check all numbers
for i in range(n):
    str1 = input().split()
    while status == 'YES' and j < n:
        sqr[i][j] = int(str1[j])
        if sqr_line.count(sqr[i][j]) > 0:
            sqr_line[sqr_line.index(sqr[i][j])] = 0
        else: status = 'NO'
        j += 1
    j = 0

#check that matrix contain all nubers from 1 to n * n
if sum(sqr_line) != 0: status = 'NO'

#create standart Sum 
sum1 = sum(sqr[0])

i, j = 0, 0
sum_row, sum_colm = 0, 0
sum_m_d, sum_s_d = 0, 0

#check sum of row, column, maind and secondary diagonal
while status == 'YES' and i < n:
    for j in range(n): 
        sum_row += sqr[i][j]
        sum_colm += sqr[j][i]
        
    if sum1 != sum_row or sum_colm != sum1:
        status = 'NO'
    
    sum_row, sum_colm = 0, 0
    
    sum_m_d += sqr[i][i]
    sum_s_d += sqr[n - i - 1][i]
    
    i += 1

if sum1 != sum_m_d or sum1 != sum_s_d:
    status = 'NO'


print(status)
