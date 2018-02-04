print('Please think of a number between 0 and 100!')

l = 0
h = 100
guess = h/2

print('Is your secret number ' + str(int(guess)) + '?')

answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guess correctly. ")
	
while True:
	new_guess = guess
	# new_guess = 50
	
	if answer == 'l':
		new_guess = (h-l) + l/2
		print(guess)
		# print(int(new_guess))
		new_guess = guess
		l = new_guess
		
	if answer == 'h':
		l = new_guess
		guess = guess/2
		print(guess)
		new_guess = guess
	
	if answer == 'c':
		print('Game over. Your secret number was: ' + str(int(guess)))
		break
	
	print('Is your secret number ' + str(int(new_guess)) + '?')
	answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guess correctly. ")
	
	# too low: (high - low) + low/2