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

balance_lower = balance
balance_upper = balance

payment = (upper_payment + lower_payment)/2

epsilon = 0.01

# Find Balance using lower bound:
# for i in range(1, 13):
	# unpaid = balance_lower - lower_payment
	# balance_lower = unpaid + monthlyInterestRate*unpaid
	# print('Balance after 1 year for lower: ' + str(balance_lower))


# Find Balance using upper bound:
# for i in range(1, 13):
	# unpaid = balance_upper - upper_payment
	# balance_upper = unpaid + monthlyInterestRate*unpaid
	# print('Balance after 1 year for upper: ' + str(balance_upper))

new_payment = payment 
while balance >= epsilon:

	# Find Balance using payment between upper and lower:
	for i in range(1, 13):
		unpaid = balance - new_payment
		balance = unpaid + monthlyInterestRate*unpaid
		print('Payment: ' + str(payment))
		print('Balance: ' + str(balance))
		
	if balance == 0:
		print('Lowest payment: ' + str(payment))
	elif balance > balance_lower:
		new_payment = lower_payment
		print(payment)
	else:
		new_payment = upper_payment
		print(payment)
		
		
		