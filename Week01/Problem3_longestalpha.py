s = 'azcbobobegghakl'
# alphabet = 'abcdefghijklmnopqrstuvwxyz'

# This will be the sub-string in alphabetical order
alphaSubstr = ''


# need to increment where I am in the alphabet and string
# alphaIndex = 0
sIndex = 0
currentSpot = 1

while sIndex <= len(s):
	for char in s:
		if char < s[currentSpot]:
			# print(char)
			alphaSubstr += char
			print(alphaSubstr)
			currentSpot += 1
		sIndex += 1

print('Longest substring in alphabetical order is: ' + alphaSubstr)


'''
compare index that is one greater than current to see if it is larger. if yes, add to substring. then compare next index to one less than it, if also larger, add to substring


'''

# s = 'azcbobobegghakladfadbobadsfadafda'

# count = 0
# inc = 0
# match = 'bob'

# while inc < len(s):
	# Going through string in chunks of 3
	# string_slice = s[inc: inc + len(match)]
	# print(string_slice)
	# if 'bob' in string_slice:
		# count+= 1
		# print('count')
	# inc += 1