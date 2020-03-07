'''
Write a function which will take a list of integers as input and returns the max integer from that list
as the output
'''

def max_integer(li):
	final = li[0]
	for num in li[1:]:
		if num > final:
			final = num
	return final

print(max_integer([22,11,3,45,6,17]))