def checkmate(board):
    boardlist = validateboard(board.split(" "))
    
    valdatesqare(boardlist)
    if not valdatesqare(boardlist):
        print("Error")
        return False
    if not moveThePiece(boardlist):
        print("Fail")
        return False
    
    print("Success")
    return True



def validateboard(board):
    listboard = []
    newboard = []
    for i in board:
        if len(i) == 0:
            pass
        else:
            listboard.append(i)
    for i in listboard:
        freetext = ""
        for j in i:
            if j != "\n":
                freetext += j
        newboard.append(freetext)
    return newboard

def valdatesqare(board):
    count = len(board)
    for i in board:
        if len(i) != count:
            return False
    return True
        
def moveThePiece(board):
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "P":
                if not pawnMove(board,i,j):
                    return False
            elif board[i][j] == "B":
                if not bishopMove(board,i,j):
                    return False
            elif board[i][j] == "R":
                if not rookMove(board,i,j):
                    return False
    return True

def pawnMove(board,x,y):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "P":
                if i-1 >= 0:
                    if j-1 >= 0 and board[i-1][j-1] == "K":
                        return True
                    if j+1 < len(board[i]) and board[i-1][j+1] == "K":
                        return True
    return False

def bishopMove(board, x, y):
    directions = [(-1, 1), (-1, -1), (1, 1), (1, -1)]
    
    for x_delta, y_delta in directions:
        current_x = x + x_delta
        current_y = y + y_delta
        
        while (0 <= current_x < len(board) and 
               0 <= current_y < len(board[current_x])):
            
            piece = board[current_x][current_y]
            
            if piece == "K" or piece == "k":
                return True
            
            if piece != "." and piece != " " and piece != "":
                break

            current_x += x_delta
            current_y += y_delta
    
    return False
        
def rookMove(board,x,y):
    for i in range(len(board)):
        if board[i][y] == "K":
            return True
        if i == x:
            for j in range(len(board[i])):
                if board[i][j] == "K":
                    return True
    return False

def queenMove(board,x,y):
    if not rookMove(board,x,y):
        return False
    if not bishopMove(board,x,y):
        return False
    return True 