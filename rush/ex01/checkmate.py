def checkmate(board):
    boardlist = validateboard(board.splitlines())
    
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
            if j != "\n" or j != " " or j != "":
                freetext += j
        newboard.append(freetext.strip())
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
                if pawnMove(board,i,j):
                    return True
            elif board[i][j] == "B":
                if bishopMove(board,i,j):
                    return True
            elif board[i][j] == "R":
                if rookMove(board,i,j):
                    return True
            elif board[i][j] == "Q":
                if queenMove(board,i,j):
                    return True
    return False

def pawnMove(board,x,y):
    if x-1 >= 0 :
        if y-1 >= 0 and board[x-1][y-1] == "K":
            return True
        if y+1 < len(board[x]) and board[x-1][y+1] == "K":
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
            
            if piece == "K":
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