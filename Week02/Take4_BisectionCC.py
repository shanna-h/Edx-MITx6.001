# Using bisection search 
# Find smallest monthly payment to pay debt in 1 year

# Lower bound - 1/12 of balance (if no int)
# Upper bound - 1/12 of balance after interest compounded for 1 year

# -----------------



def oneYrPay(payment, original_balance):
	for i in range(1, 13):
		#print('Payment: ' +str(payment))
		unpaid = original_balance - payment

		original_balance = unpaid + monthlyInterestRate*unpaid
		#print('Balance: ' + str(round(balance, 2)))
	return original_balance

def minPay(lowerBound, upperBound):
	print('minPay beginning Balance: ' + str(balance))
	
	

	# Begin with average of upper and lower bounds
	payment = (upperBound + lowerBound)/2
	print('Payment is: ' + str(payment))
	
	remaining_balance = oneYrPay(payment, balance)
	print('Balance after oneYrPay: ' + str(remaining_balance))

	if remaining_balance < 0:
		upperBound = payment
		print('upper bound is: '+ str(upperBound))
		return minPay(payment, remaining_balance)

	elif remaining_balance > 0:
		lowerBound = payment
		print('lower bound is: ' + str(lowerBound))	
		return minPay(payment, remaining_balance)
	
balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate/12
payment = 4000

lowerBound = balance/12
print('lower bound is: ' + str(lowerBound))
upperBound = (balance*(1 + monthlyInterestRate)**12)/12.0
print('upper bound is: ' + str(upperBound))
print('oneYrPay Balance: ' + str(oneYrPay(lowerBound, upperBound)))

print('----------')
	
print('minPay ending Balance: ' + str(minPay(payment, balance)))