# Write a function that combines two lists by alternatingly taking elements, 
# e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3] (assuming both lists are of equal lengths)

# def merge_two_lists(one, two):
# 	final = []
# 	for index in range(len(one)):
# 		final.append(one[index])
# 		final.append(two[index])

# 	return final

# print(merge_two_lists([1,2,3], ['a','b','c']))

###################################################################################################################

# Write a function filter_long_words() that takes a list of words and an integer n 
# and returns the list of words that are longer than n.

# def merge_two_lists(one, two):
# 	longer_list = one if len(one) > len(two) else two
# 	shorter_list = one if len(one) < len(two) else two
# 	final = []
# 	for index in range(len(shorter_list)):
# 		final.append(one[index])
# 		final.append(two[index])
# 	final += longer_list[index+1:]

# 	return final

# print(merge_two_lists([1,2,3], ['a','b','c','d','e']))

###################################################################################################################

# aaaaabaaaa = aba (remove redundant elements in a sequence)

# def remove_redundancy(s):
# 	final = '0'
# 	for char in s:
# 		if final[-1] != char:
# 		    final += char
# 	return final[1:]

# print(remove_redundancy('aaaaaaabaaaaccaaa'))

####################################################################################################################


# A pangram is a sentence that contains all the letters of the English alphabet at 
# least once,for example: "The quick brown fox jumps over the lazy dog". 
# Your task here is to write a function to check if a sentence is a 
# pangram or not.

# def is_pangram(s):
# 	alphabets = 'abcdefghijklmnopqrstuvwxyz'
# 	unique_chars = []
# 	for char in s:
# 		if char in alphabets and char not in unique_chars:
# 			unique_chars.append(char)
# 	return len(unique_chars) == 26

# print(is_pangram('abcdefghijklmnopqrstuvwxyz'))

######################################################################################################################

# Define a function overlapping() that takes two lists and returns True if they 
# have at least one member in common, False otherwise.

# def overlapping(one, two):
# 	for elem in one:
# 		if elem in two:
# 			return True
# 	return False

# print(overlapping([1,2,3],[3,4,5]))

#######################################################################################################################

# aababcacbbab => {'a':5,'b':5,'c':2}

# def character_frequency(s):
# 	final = {}
# 	for char in s:
# 		if char in final:
# 			final[char] += 1
# 		else:
# 			final[char] = 1
# 	return final

# print(character_frequency('aababcacbbab'))

#########################################################################################################################

# Implement the 'Guess the number' game in Python. You will first set a particular 
# integer as the final answer, and then ask the user to guess the number by taking 
# his input. If the guess of the user is less than the final answer, print 
# 'Your guess was less than the answer' and take input from the user again. 
# Similarly, do the same if the guess is greater than the answer. If the guess is 
# orrect, print 'your guess is correct' and stop the program. Your program should 
# keep on asking the user for his guess as long as he doesnt get the guess right

# ans = 50
# guess = int(input('Guess the answer:'))

# while guess != ans:
# 	if guess > ans:
# 		print('your guess is greater than the answer')
# 		guess = int(input('Guess the answer:'))
# 	elif guess < ans:
# 		print('your guess is less than the answer')
# 		guess = int(input('Guess the answer:'))
# print('you guess it correctly!')