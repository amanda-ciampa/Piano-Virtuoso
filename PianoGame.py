# from MainWindow import MainWindow
from PianoInput import PianoInput
from SpellingGame import SpellingGame
from GuessTheNote import GuessTheNote

import winsound

if __name__ == "__main__":
    piano = PianoInput()
    spelling = SpellingGame()

    isTrue = True
    isTrue2 = True

    # Generates random word from dict.
    spelling.random_word_gen()

    # Asks user to spell random word
    print "Please spell the word: " + spelling.word

    print spelling.generated_word

    while isTrue:

        piano.detect_key()

        if piano.piano_key == [] or piano.piano_key[0][0][0] == 128:
            pass
        else:
            # Prints the note pressed.
            print piano.display_note(piano.piano_key[0][0][1])

            spelling.user_input = spelling.input_to_list(piano.piano_key[0][0][1])

            user_input_notes = []

            # Cycles through user input list & converts returned number to what key is pressed. Then adds to list.
            for item in spelling.user_input:
                temp_key = piano.display_note(item)

                parsed_note = piano.parse_key(temp_key)

                user_input_notes.append(parsed_note)
                print "user input notes"
                print user_input_notes
                print "Generated word"
                print spelling.generated_word

                spelling.win_or_lose(user_input_notes)

                # i = 0  # Counter for list positions.

                # # If notes are correct.
                # if user_input_notes == spelling.generated_word:
                #     print 'CONGRATS!'
                #     winsound.PlaySound('OOT_Song_Correct.wav', winsound.SND_FILENAME)

                #     # Clears out all previous input & generated words
                #     spelling.generated_word = []
                #     spelling.user_input = []
                #     user_input_notes = []

                #     spelling.random_word_gen()

                #     # Asks user to spell random word
                #     print "Please spell the word: " + spelling.word

                #     continue

                # # Exits game if black key is pressed.
                # if '#' in user_input_notes[i]:
                #     spelling.generated_word = []
                #     spelling.user_input = []
                #     user_input_notes = []
                #     i = 0
                #     isTrue = False

                # # If user gets note wrong.
                # elif user_input_notes[i] != spelling.generated_word[i]:
                #     print 'WRONG!'
                #     winsound.PlaySound('OOT_Song_Error.wav', winsound.SND_FILENAME)

                #     # Clears out all previous input
                #     spelling.user_input = []
                #     user_input_notes = []
                #     i = 0

                #     print "Try again!"
                #     print "\n"
                #     print "Please spell the word: " + spelling.word

                # else:
                #     i += 1
