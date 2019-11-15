#derived from   http://ideone.com/ygfc0I, http://www.se16.info/hgb/tictactoe.htm
one,two,draw = [],[],[]
def horizontal(board,player):
    return (board[0][0]==board[0][1]==board[0][2]==player or board[1][0]==board[1][1]==board[1][2]==player or board[2][0]==board[2][1]==board[2][2]==player)
def virtical(board,player):
    return (board[0][0]==board[1][0]==board[2][0]==player or board[0][1]==board[1][1]==board[2][1]==player or board[0][2]==board[1][2]==board[2][2]==player)
def diagonal(board,player):
    return (board[0][0]==board[1][1]==board[2][2]==player or board[0][2]==board[1][1]==board[2][0]==player)
def checkWin(board,player):
    return (horizontal(board,player) or virtical(board,player) or diagonal(board,player))
def checkDraw(board):
    return all(board[row][col]!=0 for col in range(0,3) for row in range(0,3))
def boards(board, Move=1):
    global one,two,draw
    if(checkWin(board,1)):
        one.append(board)
    elif(checkWin(board,2)):
        two.append(board)
    elif(checkDraw(board)):
        draw.append(board)
    else:
        for row in range(0,3):
            for col in range(0,3):
                if board[row][col]==0:
                    board[row][col]=Move
                    boards(board,2 if Move==1 else 1)
                    board[row][col]=0
    res = [len(one),len(two),len(draw)]
    return res        
def ttt_combos(result):
    res = boards([[0,0,0],[0,0,0],[0,0,0]])
    if(result=="P1 WIN"):
        return res[0]
    elif(result=="P2 WIN"):
        return res[1]
    elif(result=="DRAW"):
        return res[2]
    elif(result=="ALL"):
        return res[0]+res[1]+res[2]
    else:
        return "Invalid input"
print(ttt_combos("P1 WIN"))