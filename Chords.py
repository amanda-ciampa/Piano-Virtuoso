""" Created by Amanda Ciampa, 2017 - Senior Thesis Project, Endicott College
Piano Virtuoso - Educational video game to teach piano lessons.

Chords.py - Used to play Chords mini game on MainWindow.py
    > Initializes lists for each major & minor chord
    > Appends user input to list
    > Generates a random major scale

THIS GAME MUST BE PLAYED USING A MIDI CONTROLLER!!!
    > Will NOT compile otherwise.
"""

from PianoInput import PianoInput
import pygame.midi
import winsound
import random

class Chords:
    def __init__(self):
        self.user_input = []
        self.current_chord = ""

        # Major chords
        self.c_major = ['c', 'e', 'g']
        self.d_major = ['d', 'f#', 'a']
        self.e_major = ['e', 'g#', 'b']
        self.f_major = ['f', 'a', 'c']
        self.g_major = ['g', 'b', 'd']
        self.a_major = ['a', 'c#', 'e']
        self.b_major = ['b', 'd#', 'f#']

        # Minor chords
        self.c_minor = ['c', 'd#', 'g']
        self.d_minor = ['d', 'f', 'a']
        self.e_minor = ['e', 'g', 'b']
        self.f_minor = ['f', 'g#', 'c']
        self.g_minor = ['g', 'a#', 'd']
        self.a_minor = ['a', 'c', 'e']
        self.b_minor = ['b', 'd', 'f#']
        self.isTrue = True

    def input_to_list(self, input):
        self.user_input.append(input)
        return self.user_input

    def random_major_chord(self):
        rand_int = random.randint(1, 7)

        chords = {1:self.c_major, 2:self.d_major, 3:self.e_major, 4:self.f_major, 5:self.g_major, 6:self.a_major, 7:self.b_major}

        self.current_chord = chords[rand_int]
        return self.current_chord

    def random_minor_chord(self):
        rand_int = random.randint(1, 7)

        chords = {1:self.c_minor, 2:self.d_minor, 3:self.e_minor, 4:self.f_minor, 5:self.g_minor, 6:self.a_minor, 7:self.b_minor}

        self.current_chord = chords[rand_int]
        return self.current_chord

    def random_chord(self):
        rand_int = random.randint(1, 14)

        chords = {1:self.c_major, 2:self.d_major, 3:self.e_major, 4:self.f_major, 5:self.g_major, 6:self.a_major, 7:self.b_major, 8:self.c_minor, 9:self.d_minor, 10:self.e_minor, 11:self.f_minor, 12:self.g_minor, 13:self.a_minor, 14:self.b_minor}

        self.current_chord = chords[rand_int]
        return self.current_chord

    def win_or_lose(self, user_input_notes, chord):
        i = 0  # Counter for list positions.

        user_str = ''.join(user_input_notes)
        c_str = ''.join(chord)

        # If notes are correct.
        if chord in user_input_notes:
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

# if __name__ == '__main__':
#     piano = PianoInput()
#     ch = Chords()

#     while ch.isTrue:

#         piano.detect_key()

#         if piano.piano_key == [] or piano.piano_key[0][0][0] == 128:
#             pass
#         else:
#             user_input_notes = []
#             print piano.display_note(piano.piano_key[0][0][1])

#             ch.user_input = ch.input_to_list(piano.piano_key[0][0][1])

#             for item in ch.user_input:
#                 temp_key = piano.display_note(item)

#                 parsed_note = piano.parse_key(temp_key)

#                 user_input_notes.append(parsed_note)
#                 print "user input notes"
#                 print user_input_notes

#                 ch.win_or_lose(user_input_notes, ch.c_chord)

#                 continue