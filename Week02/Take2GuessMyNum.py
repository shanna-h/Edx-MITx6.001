print('Please think of a number between 0 and 100!')

low = 0
high = 100
guess = int(high/2)

while True:

	print('Is your secret number ' + str(guess) + '?')
	
	answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guess correctly. ")
	
	# Guess is too low
	if answer == 'l':
		low = guess
		guess = int(high - (high - low)/2.0)
		# print(guess)
		
	elif answer == 'h':
		high = guess
		guess = int(low + (high - low)/2.0)
		# print(guess)
		
	elif answer == 'c':
		print('Game over. Your secret number was: ' + str(int(guess)))
		break
	
	else:
		print('Sorry, I did not understand your input.')

	