import os
import sys
import Tkinter
import tkMessageBox
from PIL import ImageTk, Image
from PianoInput import PianoInput
#from L1KeysOnKeyboard import L1KeysOnKeyboard
from SpellingGame import SpellingGame
from GuessTheNote import GuessTheNote


class MainWindow():
    def __init__(self):
        """ Constructor that creates GUI. """
        self.window = Tkinter.Tk()  # Creates instance of tkinter GUI
        self.window.wm_title("Piano Virtuoso")  # Displays a string in title bar
        self.window.iconbitmap("PVicon.ico")  # Displays icon in title bar

        # Creates pull down menu under FILE
        self.menubar = Tkinter.Menu(self.window)
        self.filemenu = Tkinter.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="About", command=self.about)
        self.filemenu.add_command(label="Reset", command=self.restart_game)
        self.filemenu.add_command(label="Exit", command=self.exit_game)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.window.config(menu=self.menubar)  # Displays menu bar

        # Creates/reads in title image & buttons
        self.img = ImageTk.PhotoImage(Image.open("pixelpiano2.png"))  # Reads in image file
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

if __name__ == '__main__':
    mw = MainWindow()
    mw.window.mainloop()
