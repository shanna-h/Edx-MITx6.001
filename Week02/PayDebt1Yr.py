# Minimum fixed payment to pay debt in 1 year

# Assume interest is compounded according to balance at end of month after 
# payment is made

# Monthly payment multiple of 10
# Okay to become negative

balance = 3926
original_balance = balance
annualInterestRate = 0.2
# Start with 10 and increase in increments by 10 each time
payment = 10

while balance > 0:
	
	# Code to compute balance at end of one year:
	for i in range(1, 13):
		unpaid = balance - payment
		#print('Unpaid balance: ' + str(unpaid))
		balance = unpaid + (annualInterestRate/12.0)*unpaid
		#print('Balance: ' + str(balance))
				
	if balance > 0:
		payment += 10
		balance = original_balance
		#print('Payment: ' + str(payment))
	else:
		print('Lowest Payment: ' + str(payment))
		break
	

	