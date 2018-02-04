s = 'azcbobobegghakladfadbobadsfadafda'

count = 0
inc = 0
match = 'bob'

while inc < len(s):
	# Going through string in chunks of 3
	string_slice = s[inc: inc + len(match)]
	print(string_slice)
	if 'bob' in string_slice:
		count+= 1
		print('count')
	inc += 1

print('Number of times bob occurs is: ' + str(count))