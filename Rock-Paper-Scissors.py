#This program is a two-player Rock-Paper-Scisors game.



player1_name = input('Please enter your name {Player 1}: ')
player2_name = input('Please enter your name {Player 2}: ')
	
def compare():
	player1_enter = str(input('%s, Please choose your decision: Rock, Scissors, or Paper? '%(player1_name)))
	player2_enter = str(input('%s, Please choose your decision: Rock, Scissors, or Paper? '%(player2_name)))

	if player1_enter in ['Rock','Scissors','Paper'] and player2_enter in ['Rock','Scissors','Paper']:
		print (player1_name+': '+player1_enter)
		print (player2_name+': '+player2_enter)

		if player1_enter == player2_enter:
			print ('Tie.')
		elif player1_enter == 'Rock':
			if player2_enter == 'Scissors':
				print ('Congratulations! '+player1_name+', you win!')
			else:
				print ('Congratulations! '+player2_name+', you win!')
		elif player1_enter == 'Scissors':
			if player2_enter == 'Paper':
				print ('Congratulations! '+player1_name+', you win!')
			else:
				print ('Congratulations! '+player2_name+', you win!')
		elif player1_enter == 'Paper':
			if player2_enter == 'Rock':
				print ('Congratulations! '+player1_name+', you win!')
			else:
				print ('Congratulations! '+player2_name+', you win!')
	else:
		print ('Invalid entry, Please enter your decision again. {Remember, your inputs must have their first letters capitalized}.')
		return compare()
	
compare()
while True:
	restart_game = input('Do you want to restart the game? {Remember, your inputs must have their first letters capitalized}')
	if restart_game == 'Y' or restart_game == 'Yes':
		print('Game restart.')
		compare()
	else:
		print('Game Over.')
		break
