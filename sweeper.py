# minesweeper
# Easy mode: 8x8, 10 mines 
import random
from random import sample
sweeperName = "Minesweeper"

num_found = 0
num_mines = 10
maxX = 8 
maxY = 8
rows = ["A", "B", "C", "D", "E", "F", "G", "H"]
cols = ["1", "2", "3", "4", "5", "6", "7", "8"]

game = [[" "] * maxY for _ in range(maxX)]
gameState = [[" "] * maxY for _ in range(maxX)]

def generateGrid():
	s = "  "
	for col in cols:
		s += col
	s += "\n\n"
	for i in range(maxX):
		s += rows[i] + " "
		for j in range(maxY):
			s += str(game[i][j])
		s += " " + rows[i]
		s += "\n"
	s += "\n  "
	for col in cols:
		s += col
	s += "\n"
	print(s)

def generateMines():
	rand = random.sample(range(maxX*maxY), num_mines)
	mines = []
	for mine in rand:
		grid = numToGrid(mine)
		mines.append(grid)
		gameState[grid[0]][grid[1]] = "x"
	return mines

def gameOverGrid():
	s = "  "
	for col in cols:
		s += col
	s += "\n\n"
	for i in range(maxX):
		s += rows[i] + " "
		for j in range(maxY):
			s += str(gameState[i][j])
		s += " " + rows[i]
		s += "\n"
	s += "\n  "
	for col in cols:
		s += col
	s += "\n"
	print(s)

def processGameState(mines):
	temp = [[0] * maxY for _ in range(maxX)]
	for mine in mines: 
		if (mine[0] > 0):
			temp[mine[0] - 1][mine[1]] += 1
			if (mine[1] > 0):
				temp[mine[0] - 1][mine[1] - 1] += 1
			if (mine[1] < maxY - 1):
				temp[mine[0] - 1][mine[1] + 1] += 1
		if (mine[0] < maxX - 1):
			temp[mine[0] + 1][mine[1]] += 1
			if (mine[1] > 0):
				temp[mine[0] + 1][mine[1] - 1] += 1
			if (mine[1] < maxX - 1):
				temp[mine[0] + 1][mine[1] + 1] += 1
		if (mine[1] > 0):
			temp[mine[0]][mine[1] - 1] += 1
		if (mine[1] < maxY - 1):
			temp[mine[0]][mine[1] + 1] += 1

	for i in range(maxX):
		for j in range(maxY):
			if gameState[i][j] != "x":
				if (temp[i][j] != 0):
					gameState[i][j] = temp[i][j]
				else:
					gameState[i][j] = "-"

# e.g. 0 to [0,0]
def numToGrid(num):
	row = num // maxX
	col = num % maxY
	return [row, col]

# e.g. A1 to [0,0]
def moveToGrid(move):
	return [rows.index(move[0]), cols.index(move[1])]

# Return if game already has grid filled
def alreadyMade(move):
	grid = moveToGrid(move)
	return game[grid[0]][grid[1]] != " "

# Make move 
def makeMove(move):
	grid = moveToGrid(move)
	reveal(grid[0], grid[1])

# Recursive call to reveal squares upon move
# http://kitedeveloper.blogspot.com/2013/04/minesweeper-using-recursion-to-reveal.html
def reveal(x, y):
	if (game[x][y] == " " and gameState[x][y] != "x"):
		game[x][y] = gameState[x][y]

	if(gameState[x][y] == "-"):
		revealNextCell(x - 1, y - 1)
		revealNextCell(x - 1, y)
		revealNextCell(x - 1, y + 1)
		revealNextCell(x + 1, y)
		revealNextCell(x, y - 1)
		revealNextCell(x, y + 1)
		revealNextCell(x + 1, y - 1)
		revealNextCell(x + 1, y + 1)

def revealNextCell(x, y):
	if x < 0 or x >= maxX or y < 0 or y >= maxY:
		return
	if (game[x][y] != " "):
		return
	if (gameState[x][y] == "-"):
		game[x][y] = "-"
		reveal(x, y)
	elif (gameState[x][y] != "x"):
		game[x][y] = gameState[x][y]

# Check for game over states:
#	1. All mines flagged 
#	2. All non-mine grids filled 
def checkGame():
	numFound = 0
	allFound = False
	gridFilled = True
	for i in range(maxX):
		for j in range(maxY):
			if game[i][j] == "!":
				if gameState[i][j] == "x":
					numFound += 1
			if game[i][j] == " " and gameState[i][j] != "x":
				gridFilled = False
	if (numFound == num_mines):
		allFound = True
	return allFound and gridFilled

def play():
	global game
	global gameState

	game = [[" "] * maxY for _ in range(maxX)]
	gameState = [[" "] * maxY for _ in range(maxX)]

	print("\n****************************")
	print("*** Starting Minesweeper ***")
	print("****************************\n")

	mines = generateMines()
	processGameState(mines)
	num_flags = 0

	inProgress = True 
	while (inProgress):
		generateGrid()
		#Prompt move
		print("\nEnter a grid coordinate to reveal that spot (e.g. A1): ")
		print("Add '!' to the coordinate to flag/unflag spot as a mine (e.g. A1!): ")
		print("Or type 'End' to end round: ")
		move = input("\nMake a move: ")
		print("Move made: " + move)

		if move == "End":
			print("*** Ending Game ***")
			inProgress = False
		elif move == "Cheat823":
			# Secret cheat
			gameOverGrid()
		elif (len(move) != 2 and len(move) != 3) or move[0] not in rows or move[1] not in cols:
			print("** Please enter a valid move. (e.g. A1) **\n")
		else:
			# Make the move 
			grid = moveToGrid(move)	# convert move to coordinates
			moveX = grid[0]
			moveY = grid[1]
			if (len(move) == 3):
				# Flag entered 
				if (move[2] == "!"):
					if (game[moveX][moveY] == " "):
						game[moveX][moveY] = "!"
						num_flags += 1
					elif (game[moveX][moveY] == "!"):
						game[moveX][moveY] = " "
						num_flags -= 1
					else: 
						print("** Invalid move **\n")
				else:
					print("** Invalid move **\n")
			elif (alreadyMade(move)):
				# Move already exists
				print("** Invalid move **\n")
			else:
				if gameState[moveX][moveY] == "x":
					# Hit a Mine
					for mine in mines: 
						game[mine[0]][mine[1]] = "x"
					# Game Over
					gameOverGrid()
					print("*** YOU LOSE ***")
					print("*** GAME OVER ***")
					inProgress = False
				else: 
					# Reveal boxes
					makeMove(move)
				# Check for game over 
				if (checkGame()):
					generateGrid()
					print("*** YOU WIN ***")
					print("*** GAME OVER ***")
					inProgress = False

# play()