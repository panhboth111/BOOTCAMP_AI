def row(board):
    return (board[0][0]==board[0][1]==board[0][2] or board[1][0]==board[1][1]==board[1][2] or board[2][0]==board[2][1]==board[2][2])
def col(board):
    return (board[0][0]==board[1][0]==board[2][0] or board[0][1]==board[1][1]==board[2][1] or board[0][2]==board[1][2]==board[2][2])
def diagonal(board):
    return (board[0][0]==board[1][1]==board[2][2] or board[0][2]==board[1][1]==board[2][0])
def ttt_winner(board):
    P1 = "P1 WIN"
    P2 = "P2 WIN"
    DRAW = "DRAW"
    if(row(board)):
        return(P1 if(board[0][0]==1 or board[1][0]==1 or board[2][0]==1) else P2)
    elif(col(board)):
        return(P1 if(board[0][0]==1 or board[0][1]==1 or board[0][2]==1) else P2)
    elif(diagonal(board)):
        return(P1 if(board[0][0]==1 or board[0][2]==1) else P2)
    else:
        return(DRAW)