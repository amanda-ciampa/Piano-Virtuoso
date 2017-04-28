# from MainWindow import MainWindow
from PianoInput import PianoInput
from SpellingGame import SpellingGame
from GuessTheNote import GuessTheNote

import winsound

if __name__ == "__main__":
    piano = PianoInput()
    spelling = SpellingGame()

    # # Generates random word from dict.
    # spelling.random_word_gen()

    # # Asks user to spell random word
    # print "Please spell the word: " + spelling.word

    # print spelling.generated_word

    while spelling.isTrue:

        piano.detect_key()

        if piano.piano_key == [] or piano.piano_key[0][0][0] == 128:
            pass
        else:
            # Prints the note pressed.
            print piano.display_note(piano.piano_key[0][0][1])
            piano.play_note(piano.piano_key[0][0][1])

            # spelling.user_input = spelling.input_to_list(piano.piano_key[0][

            # user_input_notes = []

            # # Cycles through user input list & converts returned number to what key is pressed. Then padds to list.
            # for item in spelling.user_input:
            #     temp_key = piano.display_note(item)

            #     parsed_note = piano.parse_key(temp_key)

            #     user_input_notes.append(parsed_note)
            #     print "user input notes"
            #     print user_input_notes
            #     print "Generated word"
            #     print spelling.generated_word

            #     spelling.win_or_lose(user_input_notes)

            #     continue