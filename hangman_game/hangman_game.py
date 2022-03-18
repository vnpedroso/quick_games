#Importing required modules:
import os
import platform
import time
import string
import unidecode

#Creating Instructions:
def instructions():
   print('Hey, hope you enjoy the game!')
   print('Step1: import the hangman_game module')
   print('Step2: create an instance of HangmanGame() class')
   print('Step3: call the start() method on your created instance to start the game')
   print('Step4: call the play_again() method on your created instance to allow replay')
   print('Have fun ^^')

#Creating Hangman Game:
class HangmanGame():

	def __init__ (self):
		self.tile = [' __ ']
		self.board = []
		self.lives = ['o']*5
		self.life_count = 4
		self.letter_list = []
		self.secret_word = ''

	def header(self):
		print('Welcome to Hangman Game!')
		print('Please do not use special characters, only letters!')

	def refresh_screen(self):
		if platform.system() == 'Windows':
			os.system('cls')
		else:
			os.system('clear')

	def get_word(self):
		#OBS - you may need to import different alphabets or even add special characters to this standard english alphabet
		alphabet = [x for x in string.ascii_lowercase]
		alphabet2 = alphabet+['-']
		while True:
			word = unidecode.unidecode(input('\nPlayer 1, please type your word to start the game: ').lower())
			letters = [x for x in word]
			if all(x in alphabet2 for x in letters):
				self.secret_word += word
				return word
				break
			else:
				self.refresh_screen()
				print('ERROR: only letters and the hyphen are accepted as valid inputs!')

	def create_board(self):
		size = len(self.get_word())
		self.board = self.tile*size

	def game_loop(self):
		alphabet = [x for x in string.ascii_lowercase]+['ç']
		while True:
			[print(i,end=' ') for i in self.board]
			print('\n'*2+'letter list: ')
			for i in self.letter_list:
				print(i, end=' ')
			print('\n'*2+'lives: ')
			for i in self.lives:
				print(i, end=' ')
			print('\n'*2)
			letter = input('Player 2, please type a letter a guess: ')
			if letter in alphabet:
				if letter in self.secret_word and letter not in self.letter_list:
					self.letter_list.append(letter)
					for i in range(len(self.secret_word)):
						if self.secret_word[i] == letter:
							self.board[i] = letter
					break
				elif letter in self.letter_list:
					self.refresh_screen()
					print('ERROR: This letter was already taken! \n')
				elif letter not in self.secret_word and letter not in self.letter_list:
					self.letter_list.append(letter)
					self.lives[self.life_count] = 'x'
					self.life_count = self.life_count - 1
					break		
			else:
				self.refresh_screen()
				print("ERROR: That's not a letter! \n")

	def end_conditions(self):
		if self.board != []:
			if ' __ ' not in self.board and self.life_count >= 0:
				return 2 
			elif ' __ ' in self.board and self.life_count < 0:
				return 1
			else:
				return 0
		else:
			return 0

	def start(self):
		self.header()
		time.sleep(0.4)
		self.create_board()
		while self.end_conditions() == 0:
			self.refresh_screen()
			self.game_loop()
			if self.end_conditions() == 1:
				self.refresh_screen()
				print('\nPlayer 1 wins!')
				break
			elif self.end_conditions() == 2:
				self.refresh_screen()
				print('\nPlayer 2 wins!')
				break

	def play_again(self):
		time.sleep(0.4)
		while True:
			replay = input('Do you want to play again? Y=Yes, N=No: ').upper()
			if replay not in ['Y','N']:
				self.refresh_screen()
				print('ERROR: Please answer with Y for yes and N for no')
			elif replay == 'Y':
				self.tile = [' __ ']
				self.board = []
				self.lives = ['o']*5
				self.life_count = 4
				self.letter_list = []
				self.secret_word = ''
				self.refresh_screen()
				self.start()
			else:
				self.refresh_screen()
				print('Goodbye!')
				break

#Enabling it as a module:
if __name__ == '__main__':
	#Playing Hangman Game:
	Game = HangmanGame()
	Game.start()
	Game.play_again()
