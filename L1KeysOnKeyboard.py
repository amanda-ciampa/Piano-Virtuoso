#     __    ________________ ____  _   __   ___   ____  _______    _   ______     __ __ ________  _______
#    / /   / ____/ ___/ ___// __ \/ | / /  <  /  / __ \/  _/   |  / | / / __ \   / //_// ____/\ \/ / ___/
#   / /   / __/  \__ \\__ \/ / / /  |/ /   / /  / /_/ // // /| | /  |/ / / / /  / ,<  / __/    \  /\__ \
#  / /___/ /___ ___/ /__/ / /_/ / /|  /   / /  / ____// // ___ |/ /|  / /_/ /  / /| |/ /___    / /___/ /
# /_____/_____//____/____/\____/_/ |_/   /_/  /_/   /___/_/  |_/_/ |_/\____/  /_/ |_/_____/   /_//____/

import Tkinter
import tkMessageBox
from PIL import ImageTk, Image
from MainWindow import MainWindow


class L1KeysOnKeyboard(MainWindow):
    #def __init__(self):
        

    def display_l1(self):
        MainWindow.__init__()
        # self.img2 = ImageTk.PhotoImage(Image.open("dugtrio.png"))
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
        self.key_keyboard_button.destroy()
        self.sheet_reading_button.destroy()
        self.spelling_button.destroy()
        self.guess_note_button.destroy()

    def guess_note_func(self):
        """ Lesson 1: Guess The Note
			MINI GAME that shows a picture of note on sheet music. Then asks user to guess note
			by pressing the piano keyboard of the corresponding key. """
        self.lesson1_panel.destroy()
        self.key_keyboard_button.destroy()
        self.sheet_reading_button.destroy()
        self.spelling_button.destroy()
        self.guess_note_button.destroy()
