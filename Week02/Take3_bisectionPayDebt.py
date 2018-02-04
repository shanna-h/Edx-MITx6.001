# Using bisection search 
# Find smallest monthly payment to pay debt in 1 year

# Lower bound - 1/12 of balance (if no int)
# Upper bound - 1/12 of balance after interest compounded for 1 year

# -----------------


balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate/12


lower_payment = balance/12.0
print('lower bound: ' + str(lower_payment))

upper_payment = (balance * (1 + monthlyInterestRate)**12)/12.0
print('upper bound: ' + str(upper_payment))

#payment = 29157
original_bal = balance

# Average of upper and lower bounds
payment = (upper_payment + lower_payment)/2
		
def oneYrBal(lower_payment, upper_payment, balance):

	for i in range(1, 13):
		print('Payment: ' +str(payment))
		unpaid = balance - payment

		balance = unpaid + monthlyInterestRate*unpaid
		print('Balance: ' + str(round(balance, 2)))
		return balance
	
	
	if balance < 0:
		print('balance is less than zero')
		#lower payment bound stays same
		lower_payment = original_bal/12.0
		upper_payment = payment
		print('lower bound: ' + str(round(lower_payment,2)) + ' upper bound: ' + str(round(upper_payment, 2)))

		return oneYrBal(lower_payment, upper_payment, original_bal)
	
	elif balance > 0:
		#upper bound stays the same
		upper_payment = (balance * (1 + monthlyInterestRate)**12)/12.0
		lower_payment = payment
		print('lower bound: ' + str(round(lower_payment,2)) + ' upper bound: ' + str(round(upper_payment, 2)))
	
		return oneYrBal(lower_payment, upper_payment, original_bal)
		
print(oneYrBal(lower_payment, upper_payment, balance))


	
	# else:
		# print('Lowest Payment: ' + str(round(payment, 2)))
		# print('Remaining balance: ' + str(round(balance, 2)))
		

