# Using bisection search 
# Find smallest monthly payment to pay debt in 1 year

# Lower bound - 1/12 of balance (if no int)
# Upper bound - 1/12 of balance after interest compounded for 1 year

# -----------------

# Function to calculate balance after one year 
# Input: monthly payment & original starting balance
# Returns: balance after one year of payments
def oneYrPay(payment, original_balance):
	for i in range(1, 13):
		unpaid = original_balance - payment
		original_balance = unpaid + (monthlyIntRate*unpaid)
	return original_balance

# Function to calculate the lowest possible payment
# Input: monthly payment, upper bound, lower bound, original balance
# Returns: lowest possible payment
def calculate_minPay(payment, upperBound, lowerBound, balance):
	print('Payment: ' + str(payment) + ' upper: ' + str(upperBound) + ' lower: ' + str(lowerBound) + ' balance: ' + str(balance))
	
	balance_oneYr = oneYrPay(payment, balance)
	
	print('balance after a year: ' + str(balance_oneYr))
	
	if balance_oneYr < -0.1:
		upperBound = round(payment, 2)
		payment = round((upperBound + lowerBound)/2, 2)
		return calculate_minPay(payment, upperBound, lowerBound, balance)
	elif balance_oneYr > 0.1:
		lowerBound = round(payment, 2)
		payment = round((upperBound + lowerBound)/2, 2)
		return calculate_minPay(payment, upperBound, lowerBound, balance)
	elif (upperBound - lowerBound) < 0.9 or balance_oneYr < 0.5:
		print('Lowest Payment: ' + str(payment))
	
balance = 370627
annualInterestRate = 0.22

original_balance = balance
monthlyIntRate = annualInterestRate/12.0

lowerBound = round((balance/12), 2)
upperBound = round(((balance * (1 + monthlyIntRate)**12)/12.0), 2)
# Calculate payment as midway point between lower and upper bound
payment = round(((lowerBound + upperBound)/2), 2)

initial_payment = payment
initial_lowbound = lowerBound
initial_highbound = upperBound
final_answer = calculate_minPay(initial_payment, initial_highbound, initial_lowbound, balance)