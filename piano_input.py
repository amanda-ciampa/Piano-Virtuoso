#     ____  _______    _   ______     _____   ______  __  ________
#    / __ \/  _/   |  / | / / __ \   /  _/ | / / __ \/ / / /_  __/
#   / /_/ // // /| | /  |/ / / / /   / //  |/ / /_/ / / / / / /
#  / ____// // ___ |/ /|  / /_/ /  _/ // /|  / ____/ /_/ / / /
# /_/   /___/_/  |_/_/ |_/\____/  /___/_/ |_/_/    \____/ /_/

import pygame.midi
import time
import random
import Image

class Piano_Input:
	def __init__(self):
		self.piano_key = ""
		self.random_key = ""

		pygame.init()
		pygame.midi.init()
		self.midi = pygame.midi.Input(1,0) # Input MIDI note
		self.player = pygame.midi.Output(0) # Output (plays) note
		# self.note = pygame.midi.

	def detect_key(self):
		""" Method to detect what piano key is pressed on MIDI controller & print out pressed note. """
		
		self.piano_key = self.midi.read(1)
		return self.piano_key

	def play_note(self):
		pass

	def display_note(self, note_number):
		""" Method that passes in 'number' of note pressed & converts it to what key was pressed. """

		note = { 36:'C 1', 37:'C# 1', 38:'D 1', 39:'D# 1', 40:'E 1', 41:'F 1', 42:'F# 1', 43:'G 1', 44:'G# 1', 45:'A 1', 46:'A# 1', 47:'B 1',
				 48:'C 2', 49:'C# 2', 50:'D 2', 51:'D# 2', 52:'E 2', 53:'F 2', 54:'F# 2', 55:'G 2', 56:'G# 2', 57:'A 2', 58:'A# 2', 59:'B 2',
				 60:'C 3', 61:'C# 3', 62:'D 3', 63:'D# 3', 64:'E 3', 65:'F 3', 66:'F# 3', 67:'G 3', 68:'G# 3', 69:'A 3', 70:'A# 3', 71:'B 3',
				 72:'C 4', 73:'C# 4', 74:'D 4', 75:'D# 4', 76:'E 4', 77:'F 4', 78:'F# 4', 79:'G 4', 80:'G# 4', 81:'A 4', 82:'A# 4', 83:'B 4',
				 84:'C 5'}
		
		return note[note_number] 

	def parse_key(self, key_pressed):
		parse_key, num = key_pressed.split(" ")
		return parse_key.lower()

	def random_note(self):
		self.random_key = random.randint(36, 84)
		return self.random_key

class Spelling_Game:
	def __init__(self):
		self.user_input = []
		self.generated_word = []
		self.word = ""

		#self.user_input.append(input)

		#key_press = Piano_Input()

	def word_split(self, word):
		pass

	def input_to_list(self, input):
		self.user_input.append(input)
		return self.user_input

	def random_word_gen(self):
		rand_int = random.randint(1, 33)
		word_gen = {
			1: 'acceded',
			2: 'ace',
			3: 'ad',
			4: 'added',
			5: 'bad',
			6: 'bag',
			7: 'baggage',
			8: 'bead',
			9: 'beaded',
			10: 'bee',
			11: 'beef',
			12: 'bed',
			13: 'bedded',
			14: 'begged',
			15: 'cab',
			16: 'cabbage',
			17: 'cage',
			18: 'caged',
			19: 'dad',
			20: 'dead',
			21: 'decade',
			22: 'deed',
			23: 'deface',
			24: 'edge',
			25: 'edged',
			26: 'efface',
			27: 'egg',
			28: 'egged',
			29: 'facade',
			30: 'face',
			31: 'feed',
			32: 'gag',
			33: 'gagged'
		}
		self.word = word_gen[rand_int]

		for letter in self.word:
			self.generated_word.append(letter)

		return self.word

class Guess_The_Note:
	def __init__(self):
		self.note = ""

	def display_image(self, image):
		image = Image.open(image)
		image.show()

if __name__ == '__main__':
	print "Hi"
	testing = Guess_The_Note()

	testing.display_image('dugtrio.png')