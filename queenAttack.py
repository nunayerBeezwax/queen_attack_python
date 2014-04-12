def horizontalCheck(x, i):
    if i == x:
        return True

def verticalCheck(y, j):
    if j == y:
        return True

def diagonalCheck(x, y, i, j):
    x = x, y
    i = i, j
    if abs(x[0] - i[0]) == abs(x[1] - i[1]):
        return True
    else:
        return False

def queenAttack(x, y, i, j):
    if  horizontalCheck(x, i) or verticalCheck(y, j) or diagonalCheck(x, y, i, j):
        print ('Yes, the Queen can attack that Piece')
    else:
        print ('Sorry, it\'s protected')
        
while True:
    x = input('X coordinate of Queen please: ')
    y = input('Y coordinate of Queen please: ')
    i = input('X coordinate of Piece to be attacked please: ')
    j = input('Y coordinate of Piece to be attacked please: ')
    queenAttack(x, y, i, j)
    
