'''
Define a function that takes two lists as input and returns True if they have atleast one element
in common, False otherwise
'''

def overlapping(one, two):
	for elem in one:
		if elem in two:
			return True
	return False

print(overlapping([1,2,3], [3,4,5]))
