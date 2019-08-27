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

#Return True if current player has won 
def checkForWin(a, move, player):
	row = move[0]
	col = move[1]

	mark = "O"
	if player == 2:
		mark = "X"

	#check row 
	rowCheck = True
	for i in range (1, 4):
		square = row + str(i)
		if a[indexes.index(square)] != mark:
			rowCheck = False

	#check column
	colCheck = True
	rows = ["A", "B", "C"]
	for i in range (3):
		square = rows[i] + col
		if a[indexes.index(square)] != mark:
			colCheck = False

	#check diagonals
	diagCheck = False
	if ((a[indexes.index("A1")] == mark and a[indexes.index("B2")] == mark and a[indexes.index("C3")] == mark) 
		or (a[indexes.index("A3")] == mark and a[indexes.index("B2")] == mark and a[indexes.index("C1")] == mark)):
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
	player = 1
	play = True

	print("\n****************************")
	print("*** Starting Tic-Tac-Toe ***")
	print("****************************\n")

	while (play):
		generateGrid(a)
		print("Current turn: Player " + str(player) + " (" + players[player] +")")
		move = input("Make a move (e.g. A1) or \"End\" to end round: ")
		print("Move entered: " + move)
		if (move == "End"):
			print("*** Ending Game ***")
			play = False
		elif (len(move) != 2 or move[0] not in ["A", "B", "C"] or move[1] not in ["1", "2", "3"]):
			print("** Please enter a valid move. (e.g. A1) **\n")
		else:
			#Make move 
			slot = indexes.index(move)
			if (a[slot] == " "):
				if player == 1: 
					a[slot] = "O"
				elif player == 2: 
					a[slot] = "X"
				
				#Check for game end 
				if (checkForWin(a, move, player)):
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
					if player == 1:
						player = 2
					elif player == 2:
						player = 1
			else: 
				print("** That move is invalid. **")

# play()