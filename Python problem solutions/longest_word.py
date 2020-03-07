'''
Write a function that takes a list of words as input and returns the longest word as the output
'''

def longest_word(li):
	final = li[0]
	for word in li[1:]:
		if len(word) > len(final):
			final = word
	return final

print(longest_word(['ubuntu', 'abc', 'xy', 'programming', 'python']))