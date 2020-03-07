'''
Implement the 'Guess the number' game in Python. You will first set a particular integer as the final answer, 
and then ask the user to guess the number by taking his input. If the guess of the user is less than the final
answer, print 'Your guess was less than the answer' and take input from the user again. Similarly, do the 
same if the guess is greater than the answer. If the guess is correct, print 'your guess is correct' and stop
the program. Your program should keep on asking the user for his guess as long as he doesnt get the guess right.
'''

answer = 50
guess = int(input('guess the answer:'))

while guess != answer:
	if guess > answer:
		print('your guess in greater than the answer')
	elif guess < answer:
		print('your guess is less than the answer')
	guess = int(input('guess the number again:'))

print('Congrats! Your guess is correct.')