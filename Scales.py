""" Created by Amanda Ciampa, 2017 - Senior Thesis Project, Endicott College
Piano Virtuoso - Educational video game to teach piano lessons.

Scales.py - Used to play Scales mini game on MainWindow.py
    > Initializes lists for each major scale
    > Appends user input to list

THIS GAME MUST BE PLAYED USING A MIDI CONTROLLER!!!
    > Will NOT compile otherwise.
"""

from PianoInput import PianoInput
import pygame.midi
import winsound
import random

class Scales:
    def __init__(self):
        self.user_input = []
        self.current_scale = ""
        self.c_scale = ['c', 'd', 'e', 'f', 'g', 'a', 'b', 'c']
        self.d_scale = ['d', 'e', 'f#', 'g', 'a', 'b', 'c#', 'd']
        self.e_scale = ['e', 'f#', 'g#', 'a', 'b', 'c#', 'd#', 'e']
        self.f_scale = ['f', 'g', 'a', 'a#', 'c', 'd', 'e', 'f']
        self.g_scale = ['g', 'a', 'b', 'c', 'd', 'e', 'f#', 'g']
        self.a_scale = ['a', 'b', 'c#', 'd', 'e', 'f#', 'g#', 'a']
        self.b_scale = ['b', 'c#', 'd#', 'e', 'f#', 'g#', 'a#', 'b']
        self.chromatic = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b', 'c']

        self.isTrue = True

    def input_to_list(self, input):
        self.user_input.append(input)
        return self.user_input

    def random_chord(self):
        rand_int = random.randint(1, 8)

        scales = {1:c_scale, 2:d_scale, 3:e_scale, 4:f_scale, 5:g_scale, 6:a_scale, 7:b_scale, 8:chromatic}

        self.current_scale = scales[rand_int]
        return self.current_scale

    def random_chord_deab(self):
        rand_int = random.randint(1, 4)

        scales = {1:self.d_scale, 2:self.e_scale, 3:self.a_scale, 4:self.b_scale}

        self.current_scale = scales[rand_int]
        return scales[rand_int]

    def win_or_lose(self, user_input_notes, scale):
        i = 0  # Counter for list positions.

        user_str = ''.join(user_input_notes)
        c_str = ''.join(scale)

        # If notes are correct.
        if user_input_notes == scale:
            print 'CONGRATS!'
            winsound.PlaySound('sound/sfx/S3K_A9.wav', winsound.SND_FILENAME)

            # Breaks out of loop since done correctly.
            c.isTrue = False

        # If user gets note wrong.
        elif (len(user_str) == len(c_str)) and (user_str != c_str):
            print 'WRONG!'
            winsound.PlaySound('sound/sfx/S3K_B2.wav', winsound.SND_FILENAME)

            # Clears out all previous input
            self.user_input = []
            user_input_notes = []
            i = 0

            print "Try again!"
            print "\n"

        else:
            i += 1

if __name__ == '__main__':
    piano = PianoInput()
    c = Scales()

    while c.isTrue:

        piano.detect_key()

        if piano.piano_key == [] or piano.piano_key[0][0][0] == 128:
            pass
        else:
            user_input_notes = []
            print piano.display_note(piano.piano_key[0][0][1])

            c.user_input = c.input_to_list(piano.piano_key[0][0][1])

            for item in c.user_input:
                temp_key = piano.display_note(item)

                parsed_note = piano.parse_key(temp_key)

                user_input_notes.append(parsed_note)
                print "user input notes"
                print user_input_notes

                c.win_or_lose(user_input_notes, c.c_scale)

                continue
