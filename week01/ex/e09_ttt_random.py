import random
def horizontal(board,player):
    return (board[0][0]==board[0][1]==board[0][2]==player or board[1][0]==board[1][1]==board[1][2]==player or board[2][0]==board[2][1]==board[2][2]==player)
def virtical(board,player):
    return (board[0][0]==board[1][0]==board[2][0]==player or board[0][1]==board[1][1]==board[2][1]==player or board[0][2]==board[1][2]==board[2][2]==player)
def diagonal(board,player):
    return (board[0][0]==board[1][1]==board[2][2]==player or board[0][2]==board[1][1]==board[2][0]==player)
def checkWin(board,player):
    return (horizontal(board,player) or virtical(board,player) or diagonal(board,player))
def checkDifference(board):
    one = 0
    two = 0
    for i in range(0,3):
        one += board[i].count(1)
        two += board[i].count(2)
    return (abs(one-two)==1 or two==one)
def winBoard(result):
    player = 1 if result == "P1 WIN" else 2
    start = True
    res = []
    while(start):
        temp = []
        for i in range(0,3):
            temp.append([random.randint(0,2),random.randint(0,2),random.randint(0,2)])
        if(checkWin(temp,player) and checkDifference(temp)):
            res.append(temp)
            start = False
    return res[0]
def drawBoard():
    start = True
    res = []
    while(start):
        temp = []
        for i in range(0,3):
            temp.append([random.randint(1,2),random.randint(1,2),random.randint(1,2)])
        if((not(checkWin(temp,1))) and (not(checkWin(temp,2))) and checkDifference(temp)):
            res.append(temp)
            start = False
    return res[0]
def ttt_random(result):
    if (result == "P1 WIN" or result == "P2 WIN"):
        return winBoard(result)
    elif(result == "DRAW"):
        return drawBoard()
    else:
        return "Invalid input"