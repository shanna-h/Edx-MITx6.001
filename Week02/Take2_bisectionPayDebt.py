# Using bisection search 
# Find smallest monthly payment to pay debt in 1 year

# Lower bound - 1/12 of balance (if no int)
# Upper bound - 1/12 of balance after interest compounded for 1 year

# -----------------


balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate/12

counter = 0

new_bal = balance

lower_payment = new_bal/12.0
print('lower bound: ' + str(lower_payment))

upper_payment = (new_bal * (1 + monthlyInterestRate)**12)/12.0
print('upper bound: ' + str(upper_payment))
		
while new_bal >= 0.01:

	for i in range(1, 13):
		
		payment = (upper_payment + lower_payment)/2

		unpaid = new_bal - payment
		print('unpaid balance is: ' + str(unpaid))
		
		print('payment is: ' + str(payment))
		new_bal = unpaid + monthlyInterestRate*unpaid
		print('balance is: ' + str(new_bal))
		print('\n')
		
	if new_bal > 0:
		upper_payment = new_bal
		payment = (payment + upper_payment)/2
		new_bal = balance
		print('using upper payment: ' + str(payment))
	elif new_bal < 0:
		lower_payment = new_bal
		payment = (payment + lower_payment)/2
		new_bal = balance
		print('using lower payment ')
	else:
		print('Lowest Payment: ' + str(payment))
	
	print('\n')
	counter += 1
		
		
		

	
	
	