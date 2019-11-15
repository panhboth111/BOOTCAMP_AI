import random
import time
import numpy as np
import copy
class TTT:
    def __init__(self):
        self.board = np.full((3,3),0)
        self.available = [0,1,2,3,4,5,6,7,8]
    def start(self):
        gameMode = input("""
Welcome to Tic Tac Toe game!
Let’s SETUP:
Choose the game MODE:
   1. Player VS Computer
   2. Player VS Player
   3. Computer VS Computer
""")
        print()
        if(gameMode=='1'):
            self.PVC()
        elif(gameMode=='2'):
            self.PVP(self.board,1,self.available)
            
        elif(gameMode=='3'):
            print("CVC")
        else:
            print("Invalid Option")
            self.start()
        self.again()
    def PVP(self,board,turn,available):
        thisBoard = copy.deepcopy(board)
        thisAvailable = available[:]
        isPlayer1 = True if turn == 1 else False
        initialTurn = turn
        positionFinder = 0
        print(f"It's turn to Player{initialTurn}")
        print("Available moves: ",end="")
        for i in thisAvailable:
            if(i!=8):
                print(i,end=",")
            else:
                print(i)
        move = int(input())
        if(move<0 or move>8):
            print("Invalid Option")
            time.sleep(0.7)
            print("Try again")
            time.sleep(0.5)
            self.PVP(thisBoard,thisAvailable,initialTurn)
        else:
            for row in range(len(thisBoard)):
                for col in range(len(thisBoard[row])):
                    if(positionFinder==move):
                        thisBoard[row][col] = 1 if isPlayer1 else 2
                    positionFinder+=1
            thisAvailable.remove(move)
        print(thisBoard)
        nextPlayer = 2 if isPlayer1 else 1
        if(thisAvailable and not self.checkWin(thisBoard,initialTurn)):
            self.PVP(thisBoard,nextPlayer,thisAvailable)
        else:
            if(self.checkWin(thisBoard,initialTurn)):
                print(f"Player{initialTurn} WIN!")
            else:
                print("DRAW")
    def PVC(self):
        diff = input("""
Choose the game DIFFICULTY:
    1. Easy
    2. Medium
    3. Hard
""")
        choice = input("""
Who will go start first ?
    1. Player
    2. Computer    
        """)
        if(diff=='1'):
            name = str(input("Enter your name: "))
            turn = 1 if(choice=='1') else 2
            self.Easy(self.board,turn,self.available,name)
        elif(diff=='2'):
            print("Medium")
        elif(diff=='3'):
            print("Hard")
        else:
            print("Invalid Option")
    def Easy(self,board,turn,available,name):
        time.sleep(0.6)
        thisName = name
        thisAvailable = available[:]
        thisBoard = copy.deepcopy(board)
        positionFinder = 0
        isPlayer = True if turn==1 else False
        initialTurn = turn
        print(f"It's turn to {thisName}" if isPlayer else "It's turn to Computer")
        for i in thisAvailable:
            if(i!=8):
                print(i,end=",")
            else:
                print(i)
        print()
        if(isPlayer):
            move = int(input())
        else:
            move = random.choice(thisAvailable)
        if(move>8 or move not in thisAvailable):
            print("Invalid Option")
            self.Easy(thisBoard,initialTurn,thisAvailable)
        else:
            for row in range(len(thisBoard)):
                for col in range(len(thisBoard[row])):
                    if(positionFinder==move):
                        thisBoard[row][col] = 1 if isPlayer else 2
                    positionFinder+=1
        print(thisBoard)
        thisAvailable.remove(move)
        nextTurn = 2 if isPlayer else 1
        if(thisAvailable and not self.checkWin(thisBoard,initialTurn)):
            self.Easy(thisBoard,nextTurn,thisAvailable,thisName)
        else:
            if(self.checkWin(thisBoard,1)):
                print(f"{thisName} wins")
            elif(self.checkWin(thisBoard,2)):
                print("Computer wins")
            else:
                print("DRAW")
    def checkWin(self,board,player):
        return (any(all(board[row][col]==player for col in range(3)) for row in range(3)) or any(all(board[row][col]==player for row in range(3)) for col in range(3)) or all(board[i][i]==player for i in range(3)) or all(board[i][2-i]==player for i in range(3)))
    def again(self):
        playAgain = input("Play again? [Y/N]")
        if(playAgain.lower()=='y'):
            self.start()
        else:
            print()
                    

game = TTT()
game.start()