#!python3
"""
Create a function to check the winner in a Tic Tac Toe game.
Game data is stored in a list:
[0,0,0,0,0,0,0,0,0,0]

The index shows the position of the X's and O's in the following gameboard
using the references:
Position 0 is always empty, to help the numbering start at 1

123
456
789

So [0,"X",0,"O",0,"X",0,0,"X","O"]
would correspond to:
X.O
.X.
.XO


Create a function called winner(game) that receives the entire list as an
input parameter. It's return value is either:
0 (no winner)
"X" (X is a winner)
"O" (O is a winner)

"""
"""
def winner(game):
    # input: list that contains 10 elements
    # output: either 0, "X", "O" to indicate who the winner is.

                                                                    I make a whole game instead have fun


TIC TAC TOE
x.o
.x.
.xo
Input number for where you want your piece
                123
                456
                789
"""
board = ["empty",".",".",".",".",".",".",".",".","."]

def dis():
    print(board[1] + board[2] + board[3] + "\n" + board[4] + board[5] + board[6] + "\n" + board[7] + board[8] + board[9])

def xTurn():
    x = int(input("X turn: "))
    if  x > 0 and x < 10 and board[x] == ".":
        board[x] = "X"
        dis()
        if check("X") == False:
            yTurn()
    else:
        print("Invalid space")
        xTurn()

def yTurn():
    y = int(input("Y turn: "))
    if  y > 0 and y < 10 and board[y] == ".":
        board[y] = "O"
        dis()
        if check("O") == False:
            xTurn()
    else:
        print("Invalid space")
        yTurn()

def win(winner):
    print("Game over")
    print(winner + " won the game!")

def check(n):
    if board[1] == n and board[2] == n and board[3] == n:
        win(n)
        return True
    elif board[4] == n and board[5] == n and board[6] == n:
        win(n)
        return True
    elif board[7] == n and board[8] == n and board[9] == n:
        win(n)
        return True
    elif board[1] == n and board[4] == n and board[7] == n:
        win(n)
        return True
    elif board[2] == n and board[5] == n and board[8] == n:
        win(n)
        return True
    elif board[3] == n and board[6] == n and board[9] == n:
        win(n)
        return True
    elif board[1] == n and board[5] == n and board[9] == n:
        win(n)
        return True
    elif board[3] == n and board[5] == n and board[7] == n:
        win(n)
        return True
    elif "." not in board:
        win("Nobody")
        return True
    else:
        return False

dis()
xTurn()