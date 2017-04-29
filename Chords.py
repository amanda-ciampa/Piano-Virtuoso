""" Created by Amanda Ciampa, 2017 - Senior Thesis Project, Endicott College
Piano Virtuoso - Educational video game to teach piano lessons.

Chords.py - Used to play Chords mini game on MainWindow.py
    > Initializes lists for each major & minor chord
    > Appends user input to list

THIS GAME MUST BE PLAYED USING A MIDI CONTROLLER!!!
    > Will NOT compile otherwise.
"""

from PianoInput import PianoInput
import pygame.midi
import winsound

class Chords:
    def __init__(self):
        self.user_input = []

        # Major chords
        self.c_chord = ['c', 'e', 'g']
        self.d_chord = ['d', 'f#', 'a']
        self.e_chord = ['e', 'g#', 'b']
        self.f_chord = ['f', 'a', 'b']
        self.g_chord = ['g', 'b', 'd']
        self.a_chord = ['a', 'c#', 'e']
        self.b_chord = ['b', 'd#', 'f#']

        # Minor chords
        self.cm_chord = ['c', 'd#', 'g']
        self.dm_chord = ['d', 'f', 'a']
        self.em_chord = ['e', 'g', 'b']
        self.fm_chord = ['f', 'g#', 'b']
        self.gm_chord = ['g', 'a#', 'd']
        self.am_chord = ['a', 'c', 'e']
        self.bm_chord = ['b', 'd', 'f#']

        self.isTrue = True

    def input_to_list(self, input):
        self.user_input.append(input)
        return self.user_input

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

if __name__ == '__main__':
    piano = PianoInput()
    ch = Chords()

    while ch.isTrue:

        piano.detect_key()

        if piano.piano_key == [] or piano.piano_key[0][0][0] == 128:
            pass
        else:
            user_input_notes = []
            print piano.display_note(piano.piano_key[0][0][1])

            ch.user_input = ch.input_to_list(piano.piano_key[0][0][1])

            for item in ch.user_input:
                temp_key = piano.display_note(item)

                parsed_note = piano.parse_key(temp_key)

                user_input_notes.append(parsed_note)
                print "user input notes"
                print user_input_notes

                ch.win_or_lose(user_input_notes, ch.c_chord)

                continue