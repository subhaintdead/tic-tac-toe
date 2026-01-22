board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
currentPlayer = "X"
winner = None
isGameRunning = True


#main objectives: to make a working tic tac toe game. at fisrt the prototype will be in the console, later it will be upgraded to a GUI version.

#the steps are:

# create/print the board

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])
printBoard(board)

# take player inputs
def playerInput(board):
    inp = int(input("enter a number, i.e.: any from 1-9: "))
    if inp >= 1 and inp <=9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("oops, that spot is already occupied.")
# check for win or draw
def checkHorizontal(board):
    global winner
if board[0] == board[1] == board[2] and board[1] != "-":
    winner = board[0]
    return True
elif board[3] == board[4] == board[5] and board[3] != "-":
    winner = board[3]
    return True
elif board[6] == board[7] == board[8] and board[6] != "-":
    winner = board[6]
    return True


def checkRow(board):
    global winner
if board[0] == board[3] == board[6] and board[0] != "-":
    winner = board[0]
    return True
elif board[1] == board[4] == board[7] and board[1] != "-":
    winner = board[1]
    return True
elif board[2] == board[5] == board[8] and board[2] != "-":
    winner = board[2]
    return True




def checkDiag(board):
    global winner
if board[0] == board[4] == board[8] and board[0] != "-":
    winner = board[0]
    return True
elif board[2] == board[4] == board[6] and board[2] != "-":
    winner = board[2]
    return True




def checkTie(board):
   global isGameRunning
   if "-" not in board:
       printBoard(board)
       print("it is a tie!")
       isGameRunning =False


# switch player

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

 def checkWin():
    global isGameRunning
    if checkHorizontal(board) or checkRow(board) or checkDiag(board):
        printBoard(board)
        isGameRunning = False
        print("the winner is " + winner + "!")




# check for win or tie again

while isGameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchplayer() 