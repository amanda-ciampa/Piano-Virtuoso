from PianoInput import PianoInput
import pygame.midi
import winsound

class Chords:
    def __init__(self):
        self.user_input = []
        self.c_chord = ['c', 'e', 'g']
        self.d_chord = ['d', 'f#', 'a']
        self.e_chord = ['e', 'g#', 'b']
        self.f_chord = ['f', 'a', 'b']
        self.g_chord = ['g', 'b', 'd']
        self.a_chord = ['a', 'c#', 'e']
        self.b_chord = ['b', 'd#', 'f#']

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
            winsound.PlaySound('sound/sfx/OOT_Song_Correct.wav', winsound.SND_FILENAME)

            # Breaks out of loop since done correctly.
            c.isTrue = False

        # If user gets note wrong.
        elif (len(user_str) == len(c_str)) and (user_str != c_str):
            print 'WRONG!'
            winsound.PlaySound('sound/sfx/OOT_Song_Error.wav', winsound.SND_FILENAME)

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