Print("Enter Knight position on a board")
cords = input()
ltrToNbr = ['a','b','c','d','e','f','g','h']
tbl = [['.'] * 8 for _ in range(8)]

x = ltrToNbr.index(cords[0])
y = 8 - int(cords[1])

# Set the knight on a board
tbl[y][x] = "N"
#print('x =', x, 'y =', y)

# Knight hit on a left
if x + 2 < 8:
    if y - 1 >= 0:
        tbl[y - 1][x + 2] = '*'
    if y + 1 < 8:
        tbl[y + 1][x + 2] = '*'

# Knight hit on a right
if x - 2 >= 0:
    if y - 1 >= 0:
        tbl[y - 1][x - 2] = '*'
    if y + 1 < 8:
        tbl[y + 1][x - 2] = '*'

# Knight hit up
if y - 2 >= 0:
    if x - 1 >= 0:
        tbl[y - 2][x - 1] = '*'
    if x + 1 < 8:
        tbl[y - 2][x + 1] = '*'

# Knight hit down
if y + 2 < 8:
    if x - 1 >= 0:
        tbl[y + 2][x - 1] = '*'
    if x + 1 < 8:
        tbl[y + 2][x + 1] = '*'

for i in range(8):
    print(*tbl[i])
