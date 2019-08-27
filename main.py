#main
import tictac
import sweeper

def listGames():
	print("** Available Games **")
	for num in numToGames.keys():
		print("\t [" + str(num) + "] " + numToGames[num])
	print("")

ticTacName = "Tic-Tac-Toe"
sweeperName = "Minesweeper"

numToGames = {
	1: ticTacName, 
	2 : sweeperName
}
gamesToFunc = {
	ticTacName: tictac.play,
	sweeperName: sweeper.play
}

print("*** Welcome to PyGames I guess ***\n")
listGames()

choosing = True
while (choosing):
	print("Enter one of the following: \n " + 
		"\t- The number of the game you would like to play\n" 
		"\t- 'List' to show list of games again\n" + 
		"\t- 'Exit' to end the program\n")
	inp = input("Enter here: ")
	if (inp == "List"):
		listGames()
	elif (inp == "Exit"):
		choosing = False
	elif not inp.isdigit():
		print("Invalid option.")
	else:
		inpNum = int(inp)
		if (inpNum <= 0 or inpNum > len(numToGames)):
			print("Invalid option.")
		else:
			#startGame
			game = numToGames[inpNum]
			gamesToFunc[game]()
			print("\n** Returning to Main Menu. **\n")
