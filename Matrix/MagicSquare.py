n = int(input())
sqr = [[0] * n for _ in range(n)]

status = 'YES' 

# Get square
for i in range(n):
    str = input().split()
    for j in range(n):
        sqr[i][j] = int(str[j])

#create standart Sum 
sum1 = sum(sqr[0])

i, j = 0, 0
sum_row, sum_colm = 0, 0
sum_m_d, sum_s_d = 0, 0

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
