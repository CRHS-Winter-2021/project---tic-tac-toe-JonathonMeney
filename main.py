##Tic Tac Toe
#Name: Jonathon Meney
#Date: Feb. 11/21

import sys 
import time


#1. (Var) Setup the empty board as a list
theBoard = ['',
            ' ',' ',' ',
            ' ',' ',' ',
            ' ',' ',' ']

#2. (fun) Print the board.
#in: a 10 item list (either x, o or ' ')
#do: print a graphic for the board
#out: none

def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[7] + '|' + board[8] + '|' + board[9])

printBoard(theBoard)

#3a. (fun) Determine if player is X or O
player1 = ''
player2 = ''

#in: None
#do: get user choice, assign X/O to player1 and 2
#out: None

def chooseLetter():
    
    letterchoice = input('What letter would you like to play as?\n> ')
    global player1
    global player2

    if letterchoice.upper() == 'X':
      player1 = 'X'      
      player2 = 'O'

    elif letterchoice.upper() == 'O':
      player1 = 'X'
      player2 = 'O'

#3b. (fun) Choose starting player 1 or 2
playermove1 = ''
playermove2 = ''

def chooseStart():
    movechoice = int(input('Player 1, would you like first or second move?\n(1 or 2)\n> '))
    global playermove1
    global playermove2
    if movechoice == 1:
      playermove1 = 'first'
      playermove2 = 'second'
    elif movechoice == 2:
      playermove1 = 'second'
      playermove2 = 'first'

#4. (fun) Get player move
#in: board as list, player as X or O
#do: get user choice (1-9),
#    check if the space is empty,
#    update the board with the X or O at the user location
#out: none

def playerMove(board, player):
    global player1
    global player2
    playersmove = int(input('What is your move?\n> '))
    if board[playersmove] == ' ':
      if player == player1:
        board[playersmove] = player1
      elif player == player2:
        board[playersmove] = player2
    else:
      return False


#5. (fun) Check Winner
#in: board as list, player as X or O
#do: check all possible win scenarios
#out: True for win, False otherwise



def checkWin(board, player):
    VicCons = [
      #Horizontal wins [0,1,2]
      [1,2,3],
      [4,5,6],
      [7,8,9],
      #Vertical wins [3,4,5]
      [1,4,7],
      [2,5,8],
      [3,6,9],
      #Diagonal wins [6,7]
      [1,5,9],
      [3,5,7]
    ]

    for i in VicCons:
      


#6. (fun) Check if board is full
#Because there are 10 list items for 9 spots,
#the first item theBoard[0] will always be ' '
#in: board as list
#do: count number of empty spaces, if there is no more spaces
#out: return True if board is full, False otherwise

def checkFull(board):
    pass

#7. Main function

def main():
    #print Welcome
    #print instructions

    #game play
    #get player letter choice
    
    #while board is not full
    ###first player move
        #player chooses move
        #print board
        #check win
        #check board full

    ###second player move
        #player chooses move
        #print baord
        #check win
    
    
    pass

