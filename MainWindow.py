import os
import sys
import time
import pygame
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
guess = GuessTheNote()

global l1

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

        # Creates pull down menu under LESSONS
        self.lessonmenu = Tkinter.Menu(self.menubar, tearoff=0)
        self.lessonmenu.add_command(label="Lesson 1 - Keys & Notes", command=self.main_menu)
        self.lessonmenu.add_command(label="Lesson 2 - C & Chromatic Scales", command=self.l2_main_menu)
        self.lessonmenu.add_command(label="Lesson 3", command=self.main_menu)
        self.lessonmenu.add_command(label="Lesson 4", command=self.main_menu)
        self.lessonmenu.add_command(label="Lesson 5", command=self.main_menu)
        self.menubar.add_cascade(label="Lessons", menu=self.lessonmenu)
        self.window.config(menu=self.menubar)  # Displays menu bar

        # Creates/reads in title images
        self.img = ImageTk.PhotoImage(Image.open("images/title/pixelpiano2.png"))  # Reads in image file
        self.start_text = ImageTk.PhotoImage(Image.open("images/buttons/start.png"))
        self.exit_text = ImageTk.PhotoImage(Image.open("images/buttons/exit.png"))

        # Creates buttons & title panel.
        self.titlePanel = Tkinter.Label(self.window, bg="black", image=self.img, height=410, width=410)  # Creates a new panel with image
        self.start = Tkinter.Button(self.window, image=self.start_text, command=self.main_menu, bd=0, height=25, bg = "black", width=80)
        self.exit = Tkinter.Button(self.window, image=self.exit_text, command=self.exit_game, bd=0, height=25, width=80, bg = "black")

        # Displays title image & buttons.
        self.titlePanel.grid(row = 0, column = 2, rowspan = 6, columnspan = 4)
        self.start.grid(row = 5, column = 5)
        self.exit.grid(row = 5, column = 2)

        # Creates text variable to use.
        self.text = Tkinter.Text(self.window, bg="black", fg="red", font="Helvetica", height=20, width=60)

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

    def main_menu(self):
        """ Closes title menu & displays the main menu of lesson 1. """
        self.titlePanel.destroy()
        self.start.destroy()
        self.exit.destroy()

        #l1 = L1KeysOnKeyboard.L1KeysOnKeyboard(self)

        # Image variables
        self.lesson1_header = ImageTk.PhotoImage(Image.open("images/headers/lesson1.png"))
        self.lesson1_subhead = ImageTk.PhotoImage(Image.open("images/headers/lesson1a.png"))
        self.chapter1_text = ImageTk.PhotoImage(Image.open("images/buttons/l1c1.png"))
        self.chapter2_text = ImageTk.PhotoImage(Image.open("images/buttons/l1c2.png"))
        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))

        # Lesson 1 panel
        self.lesson1_panel = Tkinter.Label(self.window, bg="black", image=self.lesson1_header, height=410, width=410)
        self.lesson1_sub = Tkinter.Label(self.window, bg="black", image=self.lesson1_subhead, height=25, width=150)
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        # Lesson 1 Buttons Initialization
        self.chapter1 = Tkinter.Button(self.window, image=self.chapter1_text, command=self.l1_chapter1, bd=0, bg="black", height=25, width=100)
        self.chapter2 = Tkinter.Button(self.window, image=self.chapter2_text, command=self.l1_chapter2, bd=0, bg="black", height=25, width=100)

        self.lesson1_panel.grid(row=0, column=0, columnspan=5, rowspan=10)
        self.lesson1_sub.grid(row=6, column=2)
        self.chapter1.grid(row=7, column=0)
        self.chapter2.grid(row=7, column=1)
        self.logo.grid(row=0, column=0)

    def l1_chapter1(self):
        """ Lesson 1: Keys on Piano Keyboard
			LESSON that teaches what the keys on a keyboard are."""

        # Destorys other GUI modules
        self.lesson1_panel.destroy()
        self.lesson1_sub.destroy()
        self.chapter1.destroy()
        self.chapter2.destroy()
        self.logo.destroy()

        # Keyboard diagram
        self.key_loc = ImageTk.PhotoImage(Image.open('images/keyboard/lettered_keyboard.png')) 
        self.keyboard = Tkinter.Label(self.window, image=self.key_loc, bg="black", height=410, width=410) 

        # Text
        self.img1 = ImageTk.PhotoImage(Image.open('images/text/lesson1_chapter1/txt1.png'))
        self.text1 = Tkinter.Label(self.window, image=self.img1, bg="black", height=50, width=410)

        # Piano Virtuoso logo
        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        # Next button
        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/next_sm.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=80, command=self.l1_chapter1_next1)

        # Maps modules to GUI
        self.keyboard.grid(row=0, column=0, columnspan=5, rowspan=15)
        self.text1.grid(row=13, column=1)
        self.logo.grid(row=0, column=1)
        self.next_bttn.grid(row=14, column=1)

    def l1_chapter1_next1(self):
        self.text1.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson1_chapter1/txt2.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/next_sm.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=80, command=self.l1_chapter1_next2)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1)

    def l1_chapter1_next2(self):
        self.text2.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img3 = ImageTk.PhotoImage(Image.open('images/text/lesson1_chapter1/txt3.png'))
        self.text3 = Tkinter.Label(self.window, image=self.img3, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/next_sm.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=80, command=self.l1_chapter1_next3)

        self.text3.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1)

    def l1_chapter1_next3(self):
        self.text3.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img4 = ImageTk.PhotoImage(Image.open('images/text/lesson1_chapter1/txt4.png'))
        self.text4 = Tkinter.Label(self.window, image=self.img4, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/next_sm.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=80, command=self.l1_chapter1_next4)

        self.text4.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1)

    def l1_chapter1_next4(self):
        self.text4.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img5 = ImageTk.PhotoImage(Image.open('images/text/lesson1_chapter1/txt5.png'))
        self.text5 = Tkinter.Label(self.window, image=self.img5, bg="black", height=80, width=410)

        self.spellingkee_txt = ImageTk.PhotoImage(Image.open('images/buttons/spelling_kee.png'))
        self.spellingkee_bttn = Tkinter.Button(self.window, image=self.spellingkee_txt, bd=0, bg="black", height=25, width=100, command=self.spelling_func)

        self.text5.grid(row=13, column=1)
        self.spellingkee_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1)

    def spelling_func(self):
        """ Lesson 1: Spelling Game
            MINI GAME that generates a random word & asks user to spell it out using piano keyboard."""
        self.text5.destroy()
        self.spellingkee_bttn.destroy()
        self.logo.destroy()
        self.keyboard.destroy()

        # Generates random word from dict.
        spelling.random_word_gen()

        self.spelling_image = ImageTk.PhotoImage(Image.open('images/text/lesson1_chapter1/Spelling_Kee/' + spelling.word + '.png')) 
        self.spelling_word = Tkinter.Label(self.window, image=self.spelling_image, bg="black", height=410, width=410)

        self.stext = ImageTk.PhotoImage(Image.open('images/text/lesson1_chapter1/Spelling_Kee/spell_word.png'))
        self.spell_text = Tkinter.Label(self.window, image=self.stext, bg="black", height=25, width=250)

        self.back_txt = ImageTk.PhotoImage(Image.open("images/buttons/back.png"))
        self.back = Tkinter.Button(self.window, image=self.back_txt, command=self.main_menu, bd=0, bg="black", height=25, width=100)

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.spelling_word.grid(row=0, column=0, columnspan=4, rowspan=10)
        self.logo.grid(row=0, column=1)
        self.spell_text.grid(row=3, column = 1)
        self.back.grid(row=9, column=0)
        
        self.spelling_loop()

    def spelling_loop(self):

        piano.detect_key()
        if piano.piano_key == [] or piano.piano_key[0][0][0] == 128:
            pass
        else:
            print piano.display_note(piano.piano_key[0][0][1])

            spelling.user_input = spelling.input_to_list(piano.piano_key[0][0][1])

            user_input_notes = []

            # Cycles through user input list & converts returned number to what key is pressed. Then adds to list.
            for item in spelling.user_input:
                temp_key = piano.display_note(item)

                parsed_note = piano.parse_key(temp_key)

                user_input_notes.append(parsed_note)
            
                #spelling.win_or_lose(user_input_notes)

                i = 0  # Counter for list positions.

                # Converts both lists to strings for easy comparison
                user_str = ''.join(user_input_notes)
                gen_str = ''.join(spelling.generated_word)

                # If notes are correct.
                if user_input_notes == spelling.generated_word:
                #if user_str == gen_str:
                    self.text.insert('insert', '\nCONGRATS!\n')
                    winsound.PlaySound('sound/sfx/OOT_Song_Correct.wav', winsound.SND_FILENAME)

                    # Clears out all previous input & generated words
                    spelling.generated_word = []
                    spelling.user_input = []
                    user_input_notes = []
                    self.spelling_word.destroy()
                    self.spell_text.destroy()

                    spelling.random_word_gen()

                    self.spelling_image = ImageTk.PhotoImage(Image.open('images/text/lesson1_chapter1/Spelling_Kee/' + spelling.word + '.png')) 
                    self.spelling_word = Tkinter.Label(self.window, image=self.spelling_image, bg="black", height=410, width=410)

                    self.stext = ImageTk.PhotoImage(Image.open('images/text/lesson1_chapter1/Spelling_Kee/spell_word.png'))
                    self.spell_text1 = Tkinter.Label(self.window, image=self.stext, bg="black", height=25, width=250)

                    self.spelling_word.grid(row=0, column=0, columnspan=5, rowspan=15)
                    self.spell_text1.grid(row=3, column = 1)

                # If user gets note wrong.
                elif (len(user_str) == len(gen_str)) and (user_str != gen_str):
                    self.text.insert('insert', '\nWRONG!')
                    winsound.PlaySound('sound/sfx/OOT_Song_Error.wav', winsound.SND_FILENAME)

                    # Clears out all previous input
                    spelling.user_input = []
                    user_input_notes = []
                    i = 0

                    self.spelling_image = ImageTk.PhotoImage(Image.open('images/text/lesson1_chapter1/Spelling_Kee/' + spelling.word + '.png')) 
                    self.spelling_word = Tkinter.Label(self.window, image=self.spelling_image, bg="black", height=410, width=410)

                    self.try_text = ImageTk.PhotoImage(Image.open('images/text/lesson1_chapter1/Spelling_Kee/try_again.png'))
                    self.try_again = Tkinter.Label(self.window, image=self.try_text, bg="black", height=25, width=100)

                    self.spelling_word.grid(row=0, column=0, columnspan=2, rowspan=15)
                    self.try_again.grid(row=3, column=1)

                else:
                    i = i + 1

        #self.text.grid(row=2, column=2)
        self.window.after(1, self.spelling_loop)

    def l1_chapter2(self):
        """ Lesson 1: Basic Sheet Music
			LESSON that teaches how to read basic sheet music on a Treble clef."""
        self.lesson1_panel.destroy()
        self.chapter1.destroy()
        self.chapter2.destroy()

        self.sheet_music = ImageTk.PhotoImage(Image.open('images/notes/treble.png'))
        self.staff = Tkinter.Label(self.window, image=self.sheet_music, bg="black", height=80, width=520)
        self.text.insert('insert', "This image here is of the treble clef. The treble clef is played by your RIGHT \nhand.\n\n"
            "The bass clef is played with your left hand, but let's just focus on the right for \nnow!\n\n"
            "An easy way to remember all the notes is by following this nifty trick:\n"
            "All the notes on the SPACES spell out FACE from the bottom up.\n"
            "All the notes on the LINES can be remembered by the sentence Every Good \nBoy Deserves Fudge. EGBDF\n\n"
            "The middle C note ALWAYS is the note with a line through the middle. This is \nthe middle of the piano.")

        self.staff.grid(row=1, column=1)
        self.text.grid(row=2, column=1)

    def guess_note_func(self):
        """ Lesson 1: Guess The Note
			MINI GAME that shows a picture of note on sheet music. Then asks user to guess note
			by pressing the piano keyboard of the corresponding key. """
        self.lesson1_panel.destroy()
        self.key_keyboard_button.destroy()
        self.sheet_reading_button.destroy()
        self.spelling_button.destroy()
        self.guess_note_button.destroy()
        self.main_menu_panel.destroy()

        # Generates random note.
        self.rand_gen_note = guess.randomize_note()

        # Sets random note equal to its following image.
        self.rand_note_image = guess.display_image(self.rand_gen_note)
        self.note_image = ImageTk.PhotoImage(Image.open(self.rand_note_image))  # Reads in image file
        self.guess_note_label = Tkinter.Label(self.window, image=self.note_image, bg="black", height=100,
                                        width=100)  # Creates a new panel with
        self.text.insert('insert', "Press what note this is on the piano keyboard.")

        self.guess_note_label.grid(row=1, column=1)
        self.text.grid()

        self.guess_note_loop()

    def guess_note_loop(self):
        piano.detect_key()
        if piano.piano_key == [] or piano.piano_key[0][0][0] == 128:
            pass
        else:
            # Puts user input into variable, then prints note with no numbers attached.
            temp_key = piano.display_note(piano.piano_key[0][0][1])
            guess.note = piano.parse_key(temp_key)
            print guess.note
            print self.rand_gen_note

            # If the user input note is equal to randomized note
            if guess.note == self.rand_gen_note.lower():
                self.text.insert('insert', '\nCORRECT!')
                winsound.PlaySound('sound/sfx/OOT_Song_Correct.wav', winsound.SND_FILENAME)

                # Generates random note.
                self.rand_gen_note = guess.randomize_note()

                # Sets random note equal to its following image.
                self.rand_note_image = guess.display_image(self.rand_gen_note)
                self.note_image = ImageTk.PhotoImage(Image.open(self.rand_note_image))  # Reads in image file
                self.guess_note_label = Tkinter.Label(self.window, image=self.note_image, bg="black", height=100,
                                                width=100)  # Creates a new panel with
                self.text.insert('insert', "Press what note this is on the piano keyboard.")
            # If note is wrong
            else:
                self.text.insert('insert', '\nWRONG!\n')
                winsound.PlaySound('sound/sfx/OOT_Song_Error.wav', winsound.SND_FILENAME)

                self.text.insert('insert', "Try again!\n")
        self.guess_note_label.grid(row=1, column=1)
        self.text.grid(row=2, column=2)
        self.window.after(1, self.guess_note_loop)

    def l2_main_menu(self):
        """ Displays the main menu of lesson 2. """
        self.titlePanel.destroy()
        self.start.destroy()
        self.exit.destroy()

        #l1 = L1KeysOnKeyboard.L1KeysOnKeyboard(self)

        # Image variables
        self.lesson2_header = ImageTk.PhotoImage(Image.open("images/headers/lesson2.png"))
        self.lesson2_subhead = ImageTk.PhotoImage(Image.open("images/headers/lesson2a.png"))
        self.chapter1_text = ImageTk.PhotoImage(Image.open("images/buttons/l1c1.png"))
        self.chapter2_text = ImageTk.PhotoImage(Image.open("images/buttons/l1c2.png"))
        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))

        # Lesson 2 panel
        self.lesson2_panel = Tkinter.Label(self.window, bg="black", image=self.lesson2_header, height=410, width=410)
        self.lesson2_sub = Tkinter.Label(self.window, bg="black", image=self.lesson2_subhead, height=25, width=255)
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        # Lesson 1 Buttons Initialization
        self.chapter1 = Tkinter.Button(self.window, image=self.chapter1_text, command=self.l1_chapter1, bd=0, bg="black", height=25, width=100)
        self.chapter2 = Tkinter.Button(self.window, image=self.chapter2_text, command=self.l1_chapter2, bd=0, bg="black", height=25, width=100)

        self.lesson2_panel.grid(row=0, column=0, columnspan=5, rowspan=10)
        self.lesson2_sub.grid(row=6, column=1)
        self.chapter1.grid(row=7, column=0)
        self.chapter2.grid(row=7, column=1)
        self.logo.grid(row=0, column=0)

if __name__ == '__main__':
    mw = MainWindow()
    mw.window.mainloop()