"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]




def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if terminal(board):
        return None
    xCount = 0
    oCount = 0
    for row in board:
        for cell in row:
            if cell == "X":
                xCount += 1
            elif cell == "O":
                oCount += 1
    if xCount > oCount:
        return O
    if oCount >= xCount:
        return X

    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible.append((i,j))
            
    return possible

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    resultBoard = [row[:] for row in board]
    # print( "the player is " ,player(board))
    # print("the action is " ,action)
    if action== None:
        return resultBoard

    else:    
        i,j = action
        # resultBoard = [row[:] for row in board]
        resultBoard[i][j] = player(board)
        return resultBoard

    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Xinput = []
    # Oinput  = []
    possibleW =[
                [(0,0) , (0,1) , (0,2)] , [(1,0) , (1,1) , (1,2)] , [(2,0) , (2,1) ,(2,2)] , #horizontal
                [(0,0) , (1,0) , (2,0)] , [(0,1) , (1,1) , (2,1)] , [(0,2) , (1,2) , (2,2)] , #vertical
                [(0,0) , (1,1) , (2,2)] , [(0,2) , (1,1) , (2,0)] #diagonal
                        ]
    for win in possibleW:
        if board[win[0][0]][win[0][1]] == board[win[1][0]][win[1][1]] == board[win[2][0]][win[2][1]] :
            return board[win[0][0]][win[0][1]]
    
    return None
    # for i in range(3):
    #     for j in range(3):
    #         if board[i][j] == X:
    #             Xinput.append((i,j))
    #         if board[i][j] == O:
    #             Oinput.append((i,j))
    # print("Xinput " , Xinput)
    # print("Oinput " , Oinput)

    # if (Xinput in possibleW) :
    #         return X
    # elif (Oinput in possibleW):
    #         return O
    # else:
    #     return EMPTY


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        # print("utility 1")
        return 1
    elif winner(board)==O:
        # print("utility -1")
        return -1
    else:
        # print("utility 0")
        return 0



def terminal(board):
    """
    return a boolean value indicating whether the game is over
    """    
    return winner(board) is not None or not any(EMPTY in row for row in board)
 
    # if (winner(board)==X) or (winner(board)==O) :
    #     print("True X or O or full")
    #     return True
        
    # if (len(actions(board))==0):
    #     print("True Full")
    #     return True
    
    # print("False")
    # return False


def minimax_score(board):
    if terminal(board):
        return utility(board)

    current_player = player(board)
    scores = [minimax_score(result(board, action)) for action in actions(board)]
    
    return max(scores) if current_player == X else min(scores)

def minimax(board):
    if terminal(board):
        return None

    current_player = player(board)
    best_score = -float('inf') if current_player == X else float('inf')
    best_move = None

    for action in actions(board):
        new_board = result(board, action)
        score = minimax_score(new_board)
        
        if current_player == X:
            if score > best_score:
                best_score = score
                best_move = action
        else:
            if score < best_score:
                best_score = score
                best_move = action

    return best_move
