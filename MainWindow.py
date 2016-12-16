import os
import sys
import time
import Tkinter
import winsound
import tkMessageBox
from PIL import ImageTk, Image
from PianoInput import PianoInput
#from L1KeysOnKeyboard import L1KeysOnKeyboard
from SpellingGame import SpellingGame
from GuessTheNote import GuessTheNote

piano = PianoInput()
spelling = SpellingGame()

class MainWindow():
    def __init__(self):
        """ Constructor that creates GUI. """
        self.window = Tkinter.Tk()  # Creates instance of tkinter GUI
        self.window.wm_title("Piano Virtuoso")  # Displays a string in title bar
        self.window.iconbitmap("images/icon/PVicon.ico")  # Displays icon in title bar

        # Creates pull down menu under FILE
        self.menubar = Tkinter.Menu(self.window)
        self.filemenu = Tkinter.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="About", command=self.about)
        self.filemenu.add_command(label="Reset", command=self.restart_game)
        self.filemenu.add_command(label="Exit", command=self.exit_game)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.window.config(menu=self.menubar)  # Displays menu bar

        # Creates/reads in title image & buttons
        self.img = ImageTk.PhotoImage(Image.open("images/title/pixelpiano2.png"))  # Reads in image file
        self.titlePanel = Tkinter.Label(self.window, image=self.img, height=410,
                                        width=410)  # Creates a new panel with image
        self.start = Tkinter.Button(self.window, text="Start", command=self.close_title_panel_and_display_main_menu,
                                    bd=5, height=1, fg="red", bg="black",
                                    width=8)  # Uses instance of Tkinter created. Creates a button with text 'hello'. When pressed, performs the close_title_panel func.
        self.exit = Tkinter.Button(self.window, text="Exit", command=self.exit_game, bd=5, fg="red", bg="black",
                                   height=1, width=8)

        # Displays title image & buttons.
        self.titlePanel.pack()
        self.start.pack(side="right", padx=30, pady=10)
        self.exit.pack(side="left", padx=30, pady=10)

        self.text = Tkinter.Text(self.window, bg="black", fg="red", font="Helvetica")

    def restart_game(self):
        """ Restarts Piano Virtuoso. """
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def exit_game(self):
        """ Exits out of program. """
        exit()

    def about(self):
        """ Displays information about Piano Virtuoso. """
        tkMessageBox.showinfo("About Piano Virtuoso", "Piano Virtuoso\n"
                                                      "Version 1.0\n\n"
                                                      "Created by Amanda Ciampa\n\n"
                                                      "An educational video game that helps how to learn \nto play piano and read music.")

    def close_title_panel_and_display_main_menu(self):
        """ Closes title menu & displays the main menu of lesson 1. """
        self.titlePanel.destroy()
        self.start.destroy()
        self.exit.destroy()

        #l1 = L1KeysOnKeyboard.L1KeysOnKeyboard(self)

        self.img2 = ImageTk.PhotoImage(Image.open("images/misc/dugtrio.png"))
        self.main_menu_panel = Tkinter.Label(self.window, bg="black", height=20, width=64)
        self.lesson1_panel = Tkinter.Label(self.window, bg="black", height=2, width=34, text="Lesson 1", fg="red",
                                           font=("Helvetica", 16, "bold"))
        self.spelling_button = Tkinter.Button(self.window, text="Spelling Game", command=self.spelling_func, bd=5,
                                              fg="red", bg="black", height=1, width=12)
        self.guess_note_button = Tkinter.Button(self.window, text="Guess The Note", command=self.guess_note_func,
                                                bd=5, fg="red", bg="black", height=1, width=12)
        self.key_keyboard_button = Tkinter.Button(self.window, text="Keys on Keyboard",
                                                  command=self.l1_key_on_keyboard_func, bd=5, fg="red", bg="black",
                                                  height=1, width=13)
        self.sheet_reading_button = Tkinter.Button(self.window, text="Sheet Reading",
                                                   command=self.l1_basic_sheet_reading_func, bd=5, fg="red", bg="black",
                                                   height=1, width=12)

        self.lesson1_panel.grid(row=1, column=0, columnspan=5)
        self.main_menu_panel.grid(row=1, column=0, columnspan=5, rowspan=4)

        self.key_keyboard_button.grid(row=2, column=1)
        self.sheet_reading_button.grid(row=3, column=1)

        self.spelling_button.grid(row=2, column=3)
        self.guess_note_button.grid(row=3, column=3)

    def l1_key_on_keyboard_func(self):
        """ Lesson 1: Keys on Piano Keyboard
			LESSON that teaches what the keys on a keyboard are."""
        self.lesson1_panel.destroy()
        self.key_keyboard_button.destroy()
        self.sheet_reading_button.destroy()
        self.spelling_button.destroy()
        self.guess_note_button.destroy()

        #self.text = Tkinter.Text(self.window.after(1), bg="black", fg="red", font="Helvetica")

        self.text.insert('insert', "Hello! Welcome to the Piano Virtuoso tutorial.\n\nIn this lesson, we will focus on the piano keyboard.")
        self.text.pack()

        self.next1_button = Tkinter.Button(self.window, text="Next",
                                                bd=5, fg="red", bg="black", height=1, width=6)
        self.next1_button.pack()

    def l1_basic_sheet_reading_func(self):
        """ Lesson 1: Basic Sheet Music
			LESSON that teaches how to read basic sheet music on a Treble clef."""
        self.lesson1_panel.destroy()
        self.key_keyboard_button.destroy()
        self.sheet_reading_button.destroy()
        self.spelling_button.destroy()
        self.guess_note_button.destroy()

    def spelling_func(self):
        """ Lesson 1: Spelling Game
			MINI GAME that generates a random word & asks user to spell it out using piano keyboard."""
        self.lesson1_panel.destroy()
        self.main_menu_panel.destroy()
        self.key_keyboard_button.destroy()
        self.sheet_reading_button.destroy()
        self.spelling_button.destroy()
        self.guess_note_button.destroy()

        # Generates random word from dict.
        spelling.random_word_gen()

        # Asks user to spell random word
        self.text.insert('insert', "Please spell the word: " + spelling.word + "\n")
        self.text.pack()

        self.spelling_loop()

    def spelling_loop(self):

        piano.detect_key()
        if piano.piano_key == [] or piano.piano_key[0][0][0] == 128:
            pass
        else:
            #Prints the note pressed.
            #self.text.insert('insert', piano.display_note(piano.piano_key[0][0][1]))
            # self.text.insert('insert', spelling.generated_word)
            # self.text.grid(row=2, column=2)

            print piano.display_note(piano.piano_key[0][0][1])

            spelling.user_input = spelling.input_to_list(piano.piano_key[0][0][1])

            user_input_notes = []

            # Cycles through user input list & converts returned number to what key is pressed. Then adds to list.
            for item in spelling.user_input:
                temp_key = piano.display_note(item)

                parsed_note = piano.parse_key(temp_key)

                user_input_notes.append(parsed_note)
                #print "user input notes"
            
                #spelling.win_or_lose(user_input_notes)

                i = 0  # Counter for list positions.
                #user_str = ''.join(user_input_notes)
                self.text.insert('insert', parsed_note)

                # If notes are correct.
                if user_input_notes == spelling.generated_word:
                    self.text.insert('insert', '\nCONGRATS!\n')
                    winsound.PlaySound('sound/sfx/OOT_Song_Correct.wav', winsound.SND_FILENAME)

                    # Clears out all previous input & generated words
                    spelling.generated_word = []
                    spelling.user_input = []
                    user_input_notes = []

                    spelling.random_word_gen()

                    # Asks user to spell random word
                    # text.insert('insert', "Please spell the word: " + self.word)
                    # text.pack()
                    self.text.insert('insert', "Please spell the word: " + spelling.word + '\n')

                # # Exits game if black key is pressed.
                # if '#' in user_input_notes[i]:
                #     self.generated_word = []
                #     self.user_input = []
                #     user_input_notes = []
                #     i = 0
                #     isTrue = False

                # If user gets note wrong.
                elif user_input_notes[i] != spelling.generated_word[i]:
                    self.text.insert('insert', '\nWRONG!')
                    winsound.PlaySound('sound/sfx/OOT_Song_Error.wav', winsound.SND_FILENAME)

                    # Clears out all previous input
                    spelling.user_input = []
                    user_input_notes = []
                    i = 0

                    self.text.insert('insert', "\nTry again!\n")
                    self.text.insert('insert', "Please spell the word: " + spelling.word + '\n')

                else:
                    i = i + 1
                    

        self.text.grid(row=2, column=2)
        self.window.after(1, self.spelling_loop)

    def guess_note_func(self):
        """ Lesson 1: Guess The Note
			MINI GAME that shows a picture of note on sheet music. Then asks user to guess note
			by pressing the piano keyboard of the corresponding key. """
        self.lesson1_panel.destroy()
        self.key_keyboard_button.destroy()
        self.sheet_reading_button.destroy()
        self.spelling_button.destroy()
        self.guess_note_button.destroy()

if __name__ == '__main__':
    mw = MainWindow()
   # mw.window.after(0, mw.spelling_func)
    mw.window.mainloop()
