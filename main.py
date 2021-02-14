##Tic Tac Toe
#Name: Jonathon Meney
#Date: Feb. 12/21

import time
import os

#1. (Var) Setup the empty board as a list
theBoard = ['null',
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

#3a. (fun) Determine if player is X or O
player1 = ''
player2 = ''

#in: None
#do: get user choice, assign X/O to player1 and 2
#out: None

def chooseLetter():
	letterchoice = input('What letter would you like to play as?\n(X or O)\n> ')
	global player1
	global player2
		
	if letterchoice.upper() == 'X':
		player1 = 'X'
		player2 = 'O'
		
	elif letterchoice.upper() == 'O':
		player1 = 'X'
		player2 = 'O'
	
	else:
		os.system('clear')
		print('Invalid')
		chooseLetter()

#3b. (fun) Choose starting player 1 or 2
playermove1 = ''
playermove2 = ''

def chooseStart():
	try:
		movechoice = int(input('Player 1, would you like first or second move?\n(1 or 2)\n> '))
		global playermove1
		global playermove2
		if movechoice == 1:
			playermove1 = 'first'
			playermove2 = 'second'
		elif movechoice == 2:
			playermove1 = 'second'
			playermove2 = 'first'
		else:
			os.system('clear')
			print('Invalid')
			chooseStart()
	except:
		os.system('clear')
		print('Invalid')
		chooseStart()

#4. (fun) Get player move
#in: board as list, player as X or O
#do: get user choice (1-9),
#    check if the space is empty,
#    update the board with the X or O at the user location
#out: none

def playerMove(board, player):
	global player1
	global player2
	playersmove = int(input(player + ' what is your move?\n> '))
	try:
		if board[playersmove] == ' ':
			if player == player1:
				board[playersmove] = player1
			elif player == player2:
				board[playersmove] = player2
		else:
			print('That space is taken.')
			playerMove(board,player)
	except:
		print('Invalid')
		playerMove(board,player)

#5. (fun) Check Winner
#in: board as list, player as X or O
#do: check all possible win scenarios
#out: True for win, False otherwise

def checkWin(board, player):
	toWin = 0

	VicCons = [
      #Horizontal wins
      [1,2,3],
      [4,5,6],
      [7,8,9],
      #Vertical wins
      [1,4,7],
      [2,5,8],
      [3,6,9],
      #Diagonal wins
      [1,5,9],
      [3,5,7]
    ]
	
	for WinSet in VicCons:
		for index in WinSet:
			if board[index] == player:
				toWin += 1
			
			else:
				toWin = 0

		if toWin == 3:
			return True
	
	else:
		return False        

#6. (fun) Check if board is full
#Because there are 10 list items for 9 spots,
#the first item theBoard[0] will always be ' '
#in: board as list
#do: count number of empty spaces, if there is no more spaces
#out: return True if board is full, False otherwise

def checkFull(board):
    if board.count(' ') == 0:
      return True
    else:
      return False


def mainMenu():
		global runGame
		def titlescreen():
			print ()
			print ('         -Tic Tac Toe-          ')
			print ()
			print ('--------------------------------')
			print ('             -Play-             ')
			print ('             -Help-             ')
			print ('             -Quit-             ')
			print ('--------------------------------')
			print ()
			print ('Copyright © 2019 by Jonathon Meney')
			print ()
		
		def showInstructions():
			print('Use the numpad to choose your move.')
  
		titlescreen()
		choice = input('What would you like to do?\n> ')
		choice = choice.lower()
		
		#Menu selector
		global runGame
		if choice == 'play':
			os.system('clear')
			runGame = True
		
		elif choice == 'help':
			os.system('clear')
			showInstructions()
			back = input ('\nType menu to go back\n> ')
			if back == 'menu':
				os.system('clear')
				mainMenu()
			
			elif choice == 'quit':
				os.system('clear')
				print ('Leaving so soon? Are you sure you don\'t want to play my epic game?')
				quitchoice = input('Yes or No?\n> ')
			
			if quitchoice == 'yes':
				print ('Thanks for playing.')
			
			elif quitchoice == 'no':
				os.system('clear')
				print ('You came back! Thats great just choose your option and be on your way.')
				mainMenu()
		
		else:
			os.system('clear')
			print ('My operating systems can\'t seem to understand that try again')
			mainMenu()

runGame = False
#7. Main function
def main():
	global runGame
	global player1
	global player2
	global playermove1
	global playermove2

	#print Welcome
	mainMenu()
  #get player letter choice
	chooseLetter()
	os.system('clear')	
	#get player to start choice
	chooseStart()
	os.system('clear')

	#game play
	while runGame == True:
		
		if playermove1 == 'first':
		#Player 1's Move
			#print board
			os.system('clear')
			printBoard(theBoard)
			
			#player chooses move
			playerMove(theBoard,player1)
			
			#print board
			os.system('clear')
			printBoard(theBoard)
			
			#check win
			if checkWin(theBoard,player1) == True:
				runGame = False
				print(player1 + ' has won!')
				break

			#check board full
			if checkFull(theBoard) == True:
				runGame = False
				print('The Board is full!\nGame Over!')
				break
			
		#Player 2's Move
			#print board
			os.system('clear')
			printBoard(theBoard)
			
			#player chooses move
			playerMove(theBoard,player2)
			
			#print board
			os.system('clear')
			printBoard(theBoard)
			
			#check win
			if checkWin(theBoard,player2) == True:
				runGame = False
				print(player2 + ' has won!')
				break

			#check board full
			if checkFull(theBoard) == True:
				runGame = False
				print('The Board is full!\nGame Over!')
				break

		elif playermove2 == 'first':
		#Player 2's Move
			#print board
			os.system('clear')
			printBoard(theBoard)
			
			#player chooses move
			playerMove(theBoard,player2)
			
			#print board
			os.system('clear')
			printBoard(theBoard)
			
			#check win
			if checkWin(theBoard,player2) == True:
				runGame = False
				print(player2 + ' has won!')
				break

			#check board full
			if checkFull(theBoard) == True:
				runGame = False
				print('The Board is full!\nGame Over!')
				break
			
		#Player 1's Move
			#print board
			os.system('clear')
			printBoard(theBoard)
			
			#player chooses move
			playerMove(theBoard,player1)
			
			#print board
			os.system('clear')
			printBoard(theBoard)
			
			#check win
			if checkWin(theBoard,player1) == True:
				runGame = False
				print(player1 + ' has won!')
				break

			#check board full
			if checkFull(theBoard) == True:
				runGame = False
				print('The Board is full!\nGame Over!')
				break

main()
