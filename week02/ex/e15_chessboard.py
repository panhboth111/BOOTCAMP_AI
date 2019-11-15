import numpy as np
def gen_chessboard(height=8,width=8):
    if(height<2 or width<2):
        return []
    else:
        board = np.ones((height,width),dtype=int)
        board[1::2,::2] = 0
        board[::2,1::2] = 0
        return board