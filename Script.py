import random
dictionary = open('english3.txt')
line_number = 1
randomNum = random.randint(1,194000)
for word in dictionary:
	if line_number == randomNum:
		answer = word
		break
	else:
		line_number += 1
answer = answer[:-1]
list = ['_'] * (len(answer))
guesses = []
body = 8
s = ', '
while body > 0:
	repeat = False
	print s.join(list).replace(',','')
	guess = raw_input ("Enter a Letter or a guess: ")
	if guess in guesses:
		print 'you have already guessed ' + guess
		repeat = True
	else:
		guesses.append(guess)
		print s.join(guesses)
	if answer == guess:
		print '!congrats! you got the answer'
		break
	elif answer.find(guess) != -1:
		char_index = 0
		for _ in answer:
			if _ == guess:
				list[char_index] = guess
			char_index += 1
		if s.join(list).replace(', ','') == answer:
			print '!congrats! you got the answer'
			break
	elif guess not in answer:
		if repeat == False:
			body -= 1
			if body != 0:
				print ('you have ' + str(body) + ' limbs remaining')
			else:
				lastChance = raw_input('any last words ')
				if lastChance == answer:
					print '!congrats! you got the answer'
print answer
