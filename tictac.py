import random

#tic tac toe 
tictacName = "Tic-Tac-Toe"
indexes = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
a = [" "] * 9
players = {1 : "O", 2 : "X"}

def generateGrid(a):
	s = "  1 2 3\n"
	s += "A|"
	for i in range(3):
		s += a[i] + "|"
	s += "\nB|" 
	for j in range(3, 6):
		s += a[j] + "|"
	s += "\nC|" 
	for k in range(6, 9):
		s += a[k] + "|"
	s += "\n"
	print(s)

# Makes a move for Computer player based on AI choice 
def getComputerMove(mode):
	# Get available moves 
	availMoves = []
	for ind in indexes: 
		slot = indexes.index(ind)
		if (a[slot] == " "):
			availMoves.append(ind)

	if mode == 2:	#Random
		if (availMoves):
			return random.choice(availMoves)
	elif mode == 3: #Minmax 
		if len(availMoves) == 9:
			# Just shortening calculations for empty board case
			return "B2"
		maxMove = ""
		maxScore = -2
		for move in availMoves:
			slot = indexes.index(move)
			newBoard = list(a) 
			makeMove(newBoard, slot, 2)
			if minmax(newBoard, 2) > maxScore:
				maxMove = move
		return maxMove
	return "" #shouldn't get here

def minmax(board, p):
	#Check for winning state 
	if checkForWin(board, p):
		return 1 
	elif checkForWin(board, otherPlayer(p)):
		return -1

	nextMove = -1
	score = -2

	#Get available moves
	availMoves = []
	for ind in indexes: 
		slot = indexes.index(ind)
		if (board[slot] == " "):
			availMoves.append(slot)
	for move in availMoves:
		newBoard = list(board)
		makeMove(newBoard, move, otherPlayer(p))
		newScore = -minmax(newBoard, otherPlayer(p))
		if newScore > score:
			score = newScore
			nextMove = move

	if nextMove == -1:
		return 0 #Draw 

	return score


def otherPlayer(p): 
	if p == 1: 
		return 2
	return 1

def makeMove(board, slot, p):
	if p == 1: 
		board[slot] = "O"
	elif p == 2: 
		board[slot] = "X"

#Return True if current player has won 
def checkForWin(board, p):
	rows = ["A", "B", "C"]

	mark = "O"
	if p == 2:
		mark = "X"

	#check rows
	rowCheck = False
	for row in rows:
		indCheck = True
		for i in range (1, 4):
			square = row + str(i)
			if board[indexes.index(square)] != mark:
				indCheck = False
		rowCheck = rowCheck or indCheck

	#check column
	colCheck = False
	rows = ["A", "B", "C"]
	for col in range(1, 4):
		indCheck = True
		for row in rows: 
			square = row + str(col)
			if board[indexes.index(square)] != mark:
				indCheck = False
		colCheck = colCheck or indCheck

	#check diagonals
	diagCheck = False
	if ((board[indexes.index("A1")] == mark and board[indexes.index("B2")] == mark and board[indexes.index("C3")] == mark) 
		or (board[indexes.index("A3")] == mark and board[indexes.index("B2")] == mark and board[indexes.index("C1")] == mark)):
		diagCheck = True
	return rowCheck or colCheck or diagCheck

#Check if game is at stalemate
def checkForTie(a):
	tie = True 
	for box in a:
		if box == " ":
			tie = False
	return tie

def play():
	player = 2
	play = True
	noMode = True
	gameMode = "1"

	#Reset existing game
	global a
	if (a[0] != " "):
		a = [" "] * 9

	print("\n****************************")
	print("*** Starting Tic-Tac-Toe ***")
	print("****************************\n")

	while (noMode):
		print("** Choose playing mode ** ")
		mode = input("1: vs. Person\n2: vs. Computer (Random) \n3: vs. Computer (MiniMax)\nMode: ")
		if (mode == "1" or mode == "2" or mode == "3"):
			gameMode = int(mode)
			noMode = False
		else:
			print("Invalid Mode")

	while (play):
		generateGrid(a)
		print("Current turn: Player " + str(player) + " (" + players[player] +")")

		if (gameMode == 1):
			move = input("Make a move (e.g. A1) or \"End\" to end round: ")
		else: 
			# if (player == 1):
			# 	move = input("Make a move (e.g. A1) or \"End\" to end round: ")
			# else: 
			move = getComputerMove(gameMode)
			print("Computer's move: " + move)
		if (move == "End"):
			print("*** Ending Game ***")
			play = False
		elif (len(move) != 2 or move[0] not in ["A", "B", "C"] or move[1] not in ["1", "2", "3"]):
			print("** Please enter a valid move. (e.g. A1) **\n")
		else:
			#Make move 
			slot = indexes.index(move)
			if (a[slot] == " "):
				makeMove(a, slot, player)
				#Check for game end 
				if (checkForWin(a, player)):
					generateGrid(a)
					print("*** Player " + str(player) + " wins! ***")
					print("*** GAME OVER *** ")
					play = False
				elif (checkForTie(a)):
					generateGrid(a)
					print("*** Draw. ***")
					print("*** GAME OVER *** ")
					play = False
				else:
					#Next turn 
					player = otherPlayer(player)
			else: 
				if (player == 1):
					print("** That move is invalid. **")
				elif (player == 2): 
					print("** Computer has made invalid move, ending game. **")
					play = False

# play()