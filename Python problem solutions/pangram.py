'''
A pangram is a sentence that contains all the letters of the English alphabet at least once,
for example: The quick brown fox jumps over the lazy dog. Your task here is to write a
function to check a sentence to see if it is a pangram or not.
'''

# Approach 1
def is_pangram(s):
	all_alphabets = 'abcdefghijklmnopqrstuvwxyz'
	for alphabet in all_alphabets:
		if alphabet not in s:
			return False
	return True

# print(is_pangram('abcdefghijklmnopqrstuvwxyz'))


# Approach 2
def is_pangram_2(s):
	unique_chars = []
	all_alphabets = 'abcdefghijklmnopqrstuvwxyz'
	for char in s:
		if char not in unique_chars and char in all_alphabets:
			unique_chars.append(char)
	return True if len(unique_chars) == 26 else False

print(is_pangram_2('abcdefghijklmnopqrstuvwxyz'))