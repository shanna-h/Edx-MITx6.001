# Calculate balance after 1 year if only paid minimum

balance = 484
annInt = 0.2
monthlyPayRate = 0.04

for i in range(1, 13):
	payment = monthlyPayRate * balance
	unpaid = balance - payment

	balance = unpaid + (annInt/12.0)*unpaid
print('Remaining balance: ' + str(round(balance, 2)))