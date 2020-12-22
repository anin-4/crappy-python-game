# making a sudoku solver

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
def solve( bo ):
    find = get_positions(bo)
    if not find:
        return True

    else:
        row, col = find

        for i in range(1,10):
         if check_valid(bo,i,(row, col)):
                bo[row][col] = i

                if solve(bo):
                    return True

                bo[row][col] = 0

    return 


def check_valid(bo, num, pos):
    #row checker
    i = pos[0]
    for j in range(len(bo[0])):
        if bo[i][j] == num and j != pos[1]:
            return False
    #column checker
    j=pos[1]
    for i in range(len(bo[0])):
        if bo[i][j] == num and i != pos[0]:
            return False
    
    #grid checker
    irow = pos[0]
    jcol = pos[1]
    starter_row = irow-(irow % 3)
    starter_column = jcol-(jcol % 3)
    for i in range(starter_row, starter_row+3):
        for j in range(starter_column,starter_column+3):
            if bo[i][j] == num and i != irow and j != jcol:
                return False

    return True


def display_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=" ")
        print()

def get_positions(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if(board[i][j] == 0):
                return (i,j) # row then column
    return None

display_board(board)
print("-"*20)
solve(board)
display_board(board)
