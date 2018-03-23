import random

def get_random_word():
	words = ['apples', 'cheese', 'pizza', 'appointment']
	word = words[random.randint(0, len(words)-1)]
	return word

def show_word (word):
	for ch in word:
		print(ch,)
	print ('\n')

def get_guess ():
	print('---> ',)
	return input()
	
	
def process_letter(letter, secret_word, blanked_word):
	result = False
	for i in range(0, len(secret_word)):
		if secret_word[i] == letter:
			result = True
			blanked_word[i] = letter
			
	return result	

def print_strikes (number_of_strikes):
	for i in range(0, number_of_strikes):
		print('X ',)
	print("")
		
	
def play_game ():
	strikes = 0
	max_strikes = 3
	playing = True
	
	word = get_random_word()
	blanked_word = list( '_' * len(word))

	
	while playing:
		show_word(blanked_word)
		letter = get_guess()
		found = process_letter(letter,word, blanked_word)
		
		if not found:  ## result is taken from process_letter
			strikes += 1
			print_strikes(strikes)
		
		if strikes >= max_strikes:
			playing = False
			
		if not "_" in blanked_word:
			playing = False
	
	if strikes >= max_strikes:
		print('You lost')
		print("Answer is %s" %word)
	else:
		print('You win!!!')
		print("Answer is %s" %word)
		
		
print ('Start game')
play_game()
print ('Game Over')
