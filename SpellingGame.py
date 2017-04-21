#    _____ ____  ________    __    _____   ________   _________    __  _________
#   / ___// __ \/ ____/ /   / /   /  _/ | / / ____/  / ____/   |  /  |/  / ____/
#   \__ \/ /_/ / __/ / /   / /    / //  |/ / / __   / / __/ /| | / /|_/ / __/
#  ___/ / ____/ /___/ /___/ /____/ // /|  / /_/ /  / /_/ / ___ |/ /  / / /___
# /____/_/   /_____/_____/_____/___/_/ |_/\____/   \____/_/  |_/_/  /_/_____/

import pygame.midi
import winsound
import Tkinter
import random

class SpellingGame:
    def __init__(self):
        self.user_input = []
        self.generated_word = []
        self.word = ""

        self.isTrue = True

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

    def win_or_lose(self, user_input_notes):
        #text = Tkinter.Text(self.window, bg="black", fg="red", font="Helvetica")

        i = 0  # Counter for list positions.

        # If notes are correct.
        if user_input_notes == self.generated_word:
            print 'CONGRATS!'
            winsound.PlaySound('sound/sfx/S3K_A9.wav', winsound.SND_FILENAME)

            # Clears out all previous input & generated words
            self.generated_word = []
            self.user_input = []
            user_input_notes = []

            self.random_word_gen()

            # Asks user to spell random word
            # text.insert('insert', "Please spell the word: " + self.word)
            # text.pack()
            print "Please spell the word: " + self.word

        # # Exits game if black key is pressed.
        # if '#' in user_input_notes[i]:
        #     self.generated_word = []
        #     self.user_input = []
        #     user_input_notes = []
        #     i = 0
        #     isTrue = False

        # If user gets note wrong.
        elif user_input_notes[i] != self.generated_word[i]:
            print 'WRONG!'
            winsound.PlaySound('sound/sfx/S3K_B2.wav', winsound.SND_FILENAME)

            # Clears out all previous input
            self.user_input = []
            user_input_notes = []
            i = 0

            print "Try again!"
            print "\n"
            print "Please spell the word: " + self.word

        else:
            i += 1