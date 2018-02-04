# num = 0
# while num <= 5:
	# print(num)
	# num += 1
	
# print("Outside of loop")
# print(num)

# -------------

# num = 10
# while num>3:
	# num -=1
	# print(num)
	
# -------------

# num = 100
# while not False:
	# if num < 0:
		# break
# print('num is: ' + str(num))

# -------------

# answer = 0
# end = 6
# counter = 1

# while counter <= end:
	# for i in range(0, int(end+1)):
	# print('counter is :' + str(counter))
	# answer += counter
	# print(answer)
	# counter += 1
	
# print(answer)

# -------------

# num = 0
# for i in range(0, 5):
	# num += 2
	# print(num)
	
# -------------

# num = 10
# for i in range(0, 5):
	# print(num)
	# num -=2
	
# -------------

answer = 0
end = 6
counter = 1

for i in range(end):
	answer += counter
	counter += 1
	print(answer)
