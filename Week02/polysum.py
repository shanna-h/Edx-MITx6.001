import math

def polysum(n, s):

	''' 
		n = number of sides
		s = length
		sums the area and square of perimeter
		returns sum rounded to 4 decimal places
		
	'''

	perimeter = n*s
	area = (0.25*n*s**2)/(math.tan(math.pi/n))
	
	answer = (perimeter**2) + area
	return round(answer, 4)
	
print(polysum(36,3))