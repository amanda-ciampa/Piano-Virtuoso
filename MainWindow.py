""" Created by Amanda Ciampa, 2017 - Senior Thesis Project, Endicott College
Piano Virtuoso - Educational video game to teach piano lessons.

MainWindow.py - Main file for game. - RUN THIS FILE TO PLAY GAME
    > Creates a GUI using Tkinter
    > Where most of the main game operates
        - Chapter texts
        - Chapter mini games
            ~ Uses SpellingGame.py, GuessTheNote.py, Scales.py, Chords.py, & Mashup.py
    > Imports PianoInput.py to read in MIDI controller input
    > Imports pygame for midi and sound support

THIS GAME MUST BE PLAYED USING A MIDI CONTROLLER!!!
    > Will NOT compile otherwise.

Enjoy! """

import os
import sys
import time
import pygame
import Tkinter
import tkMessageBox
from PIL import ImageTk, Image
from PianoInput import PianoInput
from SpellingGame import SpellingGame
from GuessTheNote import GuessTheNote
from Scales import Scales
from Chords import Chords

piano = PianoInput()
spelling = SpellingGame()
guess = GuessTheNote()
scale = Scales()
chord = Chords()

class MainWindow():
    def __init__(self):
        self.wrong = 0 #Keeps track of wrong answer. Resets at the finish of each mini game.

        #Score of each mini game. If == 10, mini game is completed.
        self.l1c1_score = 0 
        self.l1c2_score = 0
        self.l2c1_score = 0
        self.l2c2_score = 0
        self.l3c1_score = 0
        self.l3c2_score = 0
        self.l4c1_score = 0
        self.l4c1_score = 0
        self.l5_score = 0

        #If the chapters have been completed
        self.l1c1_complete = 0
        self.l1c2_complete = 0
        self.l2c1_complete = 0
        self.l2c2_complete = 0
        self.l3c1_complete = 0
        self.l3c2_complete = 0
        self.l4c1_complete = 0
        self.l4c2_complete = 0
        self.l5_complete = 0

        """ Constructor that creates GUI. """
        self.window = Tkinter.Tk()  # Creates instance of tkinter GUI
        self.window.wm_title("Piano Virtuoso")  # Displays a string in title bar
        self.window.iconbitmap("images/icon/PVicon.ico")  # Displays icon in title bar

        # Creates pull down menu under FILE - Has tabs About, Reset, & Exit.
        self.menubar = Tkinter.Menu(self.window)
        self.filemenu = Tkinter.Menu(self.menubar, tearoff=0, background="black", foreground="white")
        self.filemenu.add_command(label="About", command=self.about)
        self.filemenu.add_command(label="Reset", command=self.restart_game)
        self.filemenu.add_command(label="Exit", command=self.exit_game)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        # Creates pull down menu under LESSONS - Has tabs corresponding to each lesson.
        self.lessonmenu = Tkinter.Menu(self.menubar, tearoff=0, background="black")
        self.lessonmenu.add_command(label="Lesson 1 - Keys & Notes", command=self.main_menu, foreground="red")
        self.lessonmenu.add_command(label="Lesson 2 - C & Chromatic Scales", command=self.l2_main_menu, foreground="orange")
        self.lessonmenu.add_command(label="Lesson 3 - F, G, & Other Scales", command=self.l3_main_menu, foreground="yellow")
        self.lessonmenu.add_command(label="Lesson 4 - Major & Minor Chords", command=self.l4_main_menu, foreground="green")
        self.lessonmenu.add_command(label="Lesson 5 - Minigame Review", command=self.l5_main_menu, foreground="cyan")
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

#     __    ________________ ____  _   __   ___   __  ______    _____   __   __  __________   ____  __
#    / /   / ____/ ___/ ___// __ \/ | / /  <  /  /  |/  /   |  /  _/ | / /  /  |/  / ____/ | / / / / /
#   / /   / __/  \__ \\__ \/ / / /  |/ /   / /  / /|_/ / /| |  / //  |/ /  / /|_/ / __/ /  |/ / / / /
#  / /___/ /___ ___/ /__/ / /_/ / /|  /   / /  / /  / / ___ |_/ // /|  /  / /  / / /___/ /|  / /_/ /
# /_____/_____//____/____/\____/_/ |_/   /_/  /_/  /_/_/  |_/___/_/ |_/  /_/  /_/_____/_/ |_/\____/

    def main_menu(self):
        """ Closes title menu & displays the main menu of lesson 1. """
        self.titlePanel.destroy()
        self.start.destroy()
        self.exit.destroy()

        # Image variables
        self.lesson1_header = ImageTk.PhotoImage(Image.open("images/headers/lesson1.png"))
        self.lesson1_subhead = ImageTk.PhotoImage(Image.open("images/headers/lesson1a.png"))
        self.chapter1_text = ImageTk.PhotoImage(Image.open("images/buttons/l1c1.png"))
        self.chapter2_text = ImageTk.PhotoImage(Image.open("images/buttons/l1c2.png"))
        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))

        # Lesson 1 panel
        self.lesson1_panel = Tkinter.Label(self.window, bg="black", image=self.lesson1_header, height=410, width=410)
        self.lesson1_sub = Tkinter.Label(self.window, bg="black", image=self.lesson1_subhead, height=25, width=410)
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        # Lesson 1 Buttons Initialization
        self.chapter1 = Tkinter.Button(self.window, image=self.chapter1_text, command=self.l1_chapter1, bd=1, bg="black", height=25, width=120)
        self.chapter2 = Tkinter.Button(self.window, image=self.chapter2_text, command=self.l1_chapter2, bd=1, bg="black", height=25, width=120)
        # change command to command=self.l1_chapter2

        self.lesson1_panel.grid(row=0, column=0, columnspan=5, rowspan=11)
        self.lesson1_sub.grid(row=8, column=0)
        self.chapter1.grid(row=9, column=0)
        self.chapter2.grid(row=10, column=0)
        self.logo.grid(row=0, column=0)

    #     __    ________________ ____  _   __   ___            ________  _____    ____  ________________     ___
    #    / /   / ____/ ___/ ___// __ \/ | / /  <  /           / ____/ / / /   |  / __ \/_  __/ ____/ __ \   <  /
    #   / /   / __/  \__ \\__ \/ / / /  |/ /   / /  ______   / /   / /_/ / /| | / /_/ / / / / __/ / /_/ /   / /
    #  / /___/ /___ ___/ /__/ / /_/ / /|  /   / /  /_____/  / /___/ __  / ___ |/ ____/ / / / /___/ _, _/   / /
    # /_____/_____//____/____/\____/_/ |_/   /_/            \____/_/ /_/_/  |_/_/     /_/ /_____/_/ |_|   /_/

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
        self.spellingkee_bttn = Tkinter.Button(self.window, image=self.spellingkee_txt, bd=0, bg="black", height=25, width=120, command=self.spelling_func)

        self.text5.grid(row=13, column=1)
        self.spellingkee_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1)

    #    _____ ____  ________    __    _____   ________   _________    __  _________
    #   / ___// __ \/ ____/ /   / /   /  _/ | / / ____/  / ____/   |  /  |/  / ____/
    #   \__ \/ /_/ / __/ / /   / /    / //  |/ / / __   / / __/ /| | / /|_/ / __/
    #  ___/ / ____/ /___/ /___/ /____/ // /|  / /_/ /  / /_/ / ___ |/ /  / / /___
    # /____/_/   /_____/_____/_____/___/_/ |_/\____/   \____/_/  |_/_/  /_/_____/

    def spelling_func(self):
        """ Spelling Game
            MINI GAME that generates a random word & asks user to spell it out using piano keyboard.

            This first function is for the initial word. self.spelling_loop() refers to the loop for the rest of the words. """
        self.text5.destroy()
        self.spellingkee_bttn.destroy()
        self.logo.destroy()
        self.keyboard.destroy()

        # Generates random word from dict.
        spelling.random_word_gen()

        self.spelling_image = ImageTk.PhotoImage(Image.open('images/text/lesson1_chapter1/Spelling_Kee/' + spelling.word + '.png')) 
        self.spelling_word = Tkinter.Label(self.window, image=self.spelling_image, bg="black", height=410, width=410)

        self.stext = ImageTk.PhotoImage(Image.open('images/text/lesson1_chapter1/Spelling_Kee/spell_word.png'))
        self.spell_text = Tkinter.Label(self.window, image=self.stext, bg="black", height=25, width=410)

        self.back_txt = ImageTk.PhotoImage(Image.open("images/buttons/back.png"))
        self.back = Tkinter.Button(self.window, image=self.back_txt, command=self.main_menu, bd=0, bg="black", height=25, width=100)

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.spelling_word.grid(row=0, column=0, columnspan=4, rowspan=10)
        self.logo.grid(row=0, column=0)
        self.spell_text.grid(row=3, column=0)
        self.back.grid(row=9, column=0)
        
        self.spelling_loop()

    def spelling_loop(self):
        """ Spelling Game
        MINI GAME that generates a random word & asks user to spell it out using piano keyboard. 
        This function loops until the user receives 10 points. """

        piano.detect_key()
        if piano.piano_key == [] or piano.piano_key[0][0][0] == 128:
            pass
        else:
            print piano.display_note(piano.piano_key[0][0][1]) # Prints pressed note to console.
            piano.play_note(piano.piano_key[0][0][1])   # Plays sound when pressed.

            spelling.user_input = spelling.input_to_list(piano.piano_key[0][0][1])

            user_input_notes = []

            # Cycles through user input list & converts returned number to what key is pressed. Then adds to list.
            for item in spelling.user_input:
                temp_key = piano.display_note(item)

                parsed_note = piano.parse_key(temp_key)

                user_input_notes.append(parsed_note)

                i = 0  # Counter for list positions.

                # Converts both lists to strings for easy comparison
                user_str = ''.join(user_input_notes)
                gen_str = ''.join(spelling.generated_word)

                if self.l1c1_score >= 5:
                    self.l1c1_score = 0 #Sets score back to 0

                    self.spelling_word.destroy()
                    self.logo.destroy()
                    self.spell_text.destroy()
                    self.back.destroy()
                    if self.wrong > 0:
                        #pygame.midi.quit() #Quits out of midi
                        self.try_again.destroy()
                        self.wrong = 0

                    # Clears out all previous input
                    spelling.generated_word = []
                    spelling.user_input = []
                    user_input_notes = []
                    i = 0

                    self.l1c1_complete += 1 #Completed level is set to true

                    # If user completed both chapter 1 & chapter 2, goes to next lesson
                    if self.l1c1_complete > 0 and self.l1c2_complete > 0:
                        self.l2_main_menu()
                    # Otherwise, goes back to current lesson's main menu
                    else:
                        self.main_menu()
                    break

                # If notes are correct.
                if user_input_notes == spelling.generated_word:
                    self.l1c1_score = self.l1c1_score + 1
                    print self.l1c1_score

                    try: #Plays note correct sound effect.
                        sound = pygame.mixer.Sound("sound/sfx/S3K_A9.wav")
                        sound.play(loops = 0)
                    except pygame.error, message:
                            print "Cannot load sound: " + sound_name
                            raise SystemExit, message

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
                    self.spell_text = Tkinter.Label(self.window, image=self.stext, bg="black", height=25, width=410)

                    self.spelling_word.grid(row=0, column=0, columnspan=5, rowspan=15)
                    self.spell_text.grid(row=3, column = 0)

                # If user gets note wrong.
                elif (len(user_str) == len(gen_str)) and (user_str != gen_str):
                    self.wrong = self.wrong + 1

                    try: #Plays note wrong sound effect.
                        sound = pygame.mixer.Sound("sound/sfx/S3K_B2.wav")
                        sound.play(loops = 0)
                    except pygame.error, message:
                            print "Cannot load sound: " + sound_name
                            raise SystemExit, message

                    # Clears out all previous input
                    spelling.user_input = []
                    user_input_notes = []
                    i = 0

                    self.spelling_image = ImageTk.PhotoImage(Image.open('images/text/lesson1_chapter1/Spelling_Kee/' + spelling.word + '.png')) 
                    self.spelling_word = Tkinter.Label(self.window, image=self.spelling_image, bg="black", height=410, width=410)

                    self.try_text = ImageTk.PhotoImage(Image.open('images/text/lesson1_chapter1/Spelling_Kee/try_again.png'))
                    self.try_again = Tkinter.Label(self.window, image=self.try_text, bg="black", height=25, width=410)

                    self.spelling_word.grid(row=0, column=0, columnspan=2, rowspan=15)
                    self.try_again.grid(row=3, column=0)

                else:
                    i = i + 1
        self.window.after(1, self.spelling_loop)

    #     __    ________________ ____  _   __   ___            ________  _____    ____  ________________     ___
    #    / /   / ____/ ___/ ___// __ \/ | / /  <  /           / ____/ / / /   |  / __ \/_  __/ ____/ __ \   |__ \
    #   / /   / __/  \__ \\__ \/ / / /  |/ /   / /  ______   / /   / /_/ / /| | / /_/ / / / / __/ / /_/ /   __/ /
    #  / /___/ /___ ___/ /__/ / /_/ / /|  /   / /  /_____/  / /___/ __  / ___ |/ ____/ / / / /___/ _, _/   / __/
    # /_____/_____//____/____/\____/_/ |_/   /_/            \____/_/ /_/_/  |_/_/     /_/ /_____/_/ |_|   /____/

    def l1_chapter2(self):
        """ Lesson 1: Basic Sheet Music
			LESSON that teaches how to read basic sheet music on a Treble clef."""
        self.lesson1_panel.destroy()
        self.chapter1.destroy()
        self.chapter2.destroy()
        self.lesson1_sub.destroy()
        self.logo.destroy()

        self.sheet_music = ImageTk.PhotoImage(Image.open('images/notes/treble.png'))
        self.staff = Tkinter.Label(self.window, image=self.sheet_music, bg="black", height=410, width=520)

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img1 = ImageTk.PhotoImage(Image.open("images/text/lesson1_chapter2/txt1.png"))
        self.text1 = Tkinter.Label(self.window, bg="black", image=self.img1, height=25, width=250)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/next_sm.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=80, command=self.l1_chapter2_next1)

        self.staff.grid(row=0, column=0, columnspan=5, rowspan=10)
        self.next_bttn.grid(row=9, column=2)
        self.text1.grid(row=7, column=2)
        self.logo.grid(row=0, column=2)

    def l1_chapter2_next1(self):
        self.text1.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.img2 = ImageTk.PhotoImage(Image.open("images/text/lesson1_chapter2/txt2.png"))
        self.text2 = Tkinter.Label(self.window, bg="black", image=self.img2, height=50, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/next_sm.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=80, command=self.l1_chapter2_next2)

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.text2.grid(row=8, column=2)
        self.next_bttn.grid(row=9, column=2)
        self.logo.grid(row=0, column=2)

    def l1_chapter2_next2(self):
        self.text2.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.img3 = ImageTk.PhotoImage(Image.open("images/text/lesson1_chapter2/txt3.png"))
        self.text3 = Tkinter.Label(self.window, bg="black", image=self.img3, height=50, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/next_sm.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=80, command=self.l1_chapter2_next3)

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.text3.grid(row=8, column=2)
        self.next_bttn.grid(row=9, column=2)
        self.logo.grid(row=0, column=2)

    def l1_chapter2_next3(self):
        self.text3.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.img4 = ImageTk.PhotoImage(Image.open("images/text/lesson1_chapter2/txt4.png"))
        self.text4 = Tkinter.Label(self.window, bg="black", image=self.img4, height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/next_sm.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=80, command=self.l1_chapter2_next4)

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.text4.grid(row=8, column=2)
        self.next_bttn.grid(row=9, column=2)
        self.logo.grid(row=0, column=2)

    def l1_chapter2_next4(self):
        self.text4.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.img5 = ImageTk.PhotoImage(Image.open("images/text/lesson1_chapter2/txt5.png"))
        self.text5 = Tkinter.Label(self.window, bg="black", image=self.img5, height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/next_sm.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=80, command=self.l1_chapter2_next5)

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.text5.grid(row=8, column=2)
        self.next_bttn.grid(row=9, column=2)
        self.logo.grid(row=0, column=2)

    def l1_chapter2_next5(self):
        self.text5.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.img6 = ImageTk.PhotoImage(Image.open("images/text/lesson1_chapter2/txt6.png"))
        self.text6 = Tkinter.Label(self.window, bg="black", image=self.img6, height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/guess_the_note.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=150, command=self.guess_note_func)

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.text6.grid(row=8, column=2)
        self.next_bttn.grid(row=9, column=2)
        self.logo.grid(row=0, column=2)

    #    ________  __________________    ________  ________   _   ______  ____________
    #   / ____/ / / / ____/ ___/ ___/   /_  __/ / / / ____/  / | / / __ \/_  __/ ____/
    #  / / __/ / / / __/  \__ \\__ \     / / / /_/ / __/    /  |/ / / / / / / / __/
    # / /_/ / /_/ / /___ ___/ /__/ /    / / / __  / /___   / /|  / /_/ / / / / /___
    # \____/\____/_____//____/____/    /_/ /_/ /_/_____/  /_/ |_/\____/ /_/ /_____/

    def guess_note_func(self):
        """ Lesson 1: Guess The Note
			MINI GAME that shows a picture of note on sheet music. Then asks user to guess note
			by pressing the piano keyboard of the corresponding key. """
        self.lesson1_panel.destroy()
        self.logo.destroy()
        self.lesson1_sub.destroy()
        self.chapter1.destroy()
        self.chapter2.destroy()
        self.text6.destroy()
        self.staff.destroy()
        self.next_bttn.destroy()

        # Generates random note.
        self.rand_gen_note = guess.randomize_note()

        # Sets random note equal to its following image.
        self.rand_note_image = guess.display_image(self.rand_gen_note)
        self.note_image = ImageTk.PhotoImage(Image.open(self.rand_note_image))  # Reads in image file
        self.guess_note_label = Tkinter.Label(self.window, image=self.note_image, bg="black", height=410,
                                        width=410) 

        self.gtext = ImageTk.PhotoImage(Image.open('images/text/lesson1_chapter2/Guess_the_Note/this_note.png'))
        self.guess_text = Tkinter.Label(self.window, image=self.gtext, bg="black", height=25, width=410)

        self.back_txt = ImageTk.PhotoImage(Image.open("images/buttons/back.png"))
        self.back = Tkinter.Button(self.window, image=self.back_txt, command=self.main_menu, bd=0, bg="black", height=25, width=100)

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.guess_note_label.grid(row=0, column=0, columnspan=4, rowspan=10)
        self.logo.grid(row=0, column=0)
        self.guess_text.grid(row=3, column=0)
        self.back.grid(row=9, column=0)

        self.guess_note_loop()

    def guess_note_loop(self):
        piano.detect_key()
        if piano.piano_key == [] or piano.piano_key[0][0][0] == 128:
            pass
        else:
            # Puts user input into variable, then prints note with no numbers attached.
            temp_key = piano.display_note(piano.piano_key[0][0][1])
            piano.play_note(piano.piano_key[0][0][1])
            guess.note = piano.parse_key(temp_key)
            print guess.note
            print self.rand_gen_note

            # If the user received 10 points:
            if self.l1c2_score >= 10:
                self.l1c2_score = 0 #Sets score back to 0

                self.guess_note_label.destroy()
                self.guess_text.destroy()
                self.logo.destroy()
                self.back.destroy()
                if self.wrong > 0:
                    self.try_again.destroy()
                    self.wrong = 0

                self.l1c2_complete += 1 #Completed level is set to true

                # If user completed both chapter 1 & chapter 2, goes to next lesson
                if self.l1c1_complete > 0 and self.l1c2_complete > 0:
                    self.l2_main_menu()
                # Otherwise, goes back to current lesson's main menu
                else:
                    self.main_menu()

            # If the user input note is equal to randomized note
            if guess.note == self.rand_gen_note.lower():
                self.l1c2_score = self.l1c2_score + 1
                print self.l1c2_score

                try: #Plays note correct sound effect.
                    sound = pygame.mixer.Sound("sound/sfx/S3K_A9.wav")
                    sound.play(loops = 0)
                except pygame.error, message:
                    print "Cannot load sound: " + sound_name
                    raise SystemExit, message

                # Generates random note.
                self.rand_gen_note = guess.randomize_note()

                # Sets random note equal to its following image.
                self.rand_note_image = guess.display_image(self.rand_gen_note)
                self.note_image = ImageTk.PhotoImage(Image.open(self.rand_note_image))  # Reads in image file
                self.guess_note_label = Tkinter.Label(self.window, image=self.note_image, bg="black", height=410,
                                                width=410) 

                self.gtext = ImageTk.PhotoImage(Image.open('images/text/lesson1_chapter2/Guess_the_Note/this_note.png'))
                self.guess_text = Tkinter.Label(self.window, image=self.gtext, bg="black", height=25, width=410)

                self.guess_note_label.grid(row=0, column=0, columnspan=4, rowspan=10)
                self.guess_text.grid(row=3, column=0)

            # If note is wrong
            else:
                self.wrong = self.wrong + 1

                try: #Plays note wrong sound effect.
                    sound = pygame.mixer.Sound("sound/sfx/S3K_B2.wav")
                    sound.play(loops = 0)
                except pygame.error, message:
                        print "Cannot load sound: " + sound_name
                        raise SystemExit, message

                self.try_text = ImageTk.PhotoImage(Image.open('images/text/lesson1_chapter1/Spelling_Kee/try_again.png'))
                self.try_again = Tkinter.Label(self.window, image=self.try_text, bg="black", height=25, width=410)

                self.try_again.grid(row=3, column=0)
        self.window.after(1, self.guess_note_loop)

    #     __    ________________ ____  _   __   ___      __  ______    _____   __   __  __________   ____  __
    #    / /   / ____/ ___/ ___// __ \/ | / /  |__ \    /  |/  /   |  /  _/ | / /  /  |/  / ____/ | / / / / /
    #   / /   / __/  \__ \\__ \/ / / /  |/ /   __/ /   / /|_/ / /| |  / //  |/ /  / /|_/ / __/ /  |/ / / / /
    #  / /___/ /___ ___/ /__/ / /_/ / /|  /   / __/   / /  / / ___ |_/ // /|  /  / /  / / /___/ /|  / /_/ /
    # /_____/_____//____/____/\____/_/ |_/   /____/  /_/  /_/_/  |_/___/_/ |_/  /_/  /_/_____/_/ |_/\____/

    def l2_main_menu(self):
        """ Displays the main menu of lesson 2. """
        self.titlePanel.destroy()
        self.start.destroy()
        self.exit.destroy()

        # Image variables
        self.lesson2_header = ImageTk.PhotoImage(Image.open("images/headers/lesson2.png"))
        self.lesson2_subhead = ImageTk.PhotoImage(Image.open("images/headers/lesson2a.png"))
        self.chapter1_text = ImageTk.PhotoImage(Image.open("images/buttons/l2c1.png"))
        self.chapter2_text = ImageTk.PhotoImage(Image.open("images/buttons/l2c2.png"))
        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))

        # Lesson 2 panel
        self.lesson2_panel = Tkinter.Label(self.window, bg="black", image=self.lesson2_header, height=410, width=410)
        self.lesson2_sub = Tkinter.Label(self.window, bg="black", image=self.lesson2_subhead, height=25, width=410)
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)


        # Lesson 2 Buttons Initialization
        self.chapter1 = Tkinter.Button(self.window, image=self.chapter1_text, command=self.l2_chapter1, bd=1, bg="black", height=25, width=120)
        self.chapter2 = Tkinter.Button(self.window, image=self.chapter2_text, command=self.l2_chapter2, bd=1, bg="black", height=25, width=120)
        # change command to command=self.l1_chapter2

        self.lesson2_panel.grid(row=0, column=0, columnspan=5, rowspan=11)
        self.lesson2_sub.grid(row=8, column=0)
        self.chapter1.grid(row=9, column=0)
        self.chapter2.grid(row=10, column=0)
        self.logo.grid(row=0, column=0)

    #     __    ________________ ____  _   __   ___               ________  _____    ____  ________________     ___
    #    / /   / ____/ ___/ ___// __ \/ | / /  |__ \             / ____/ / / /   |  / __ \/_  __/ ____/ __ \   <  /
    #   / /   / __/  \__ \\__ \/ / / /  |/ /   __/ /   ______   / /   / /_/ / /| | / /_/ / / / / __/ / /_/ /   / /
    #  / /___/ /___ ___/ /__/ / /_/ / /|  /   / __/   /_____/  / /___/ __  / ___ |/ ____/ / / / /___/ _, _/   / /
    # /_____/_____//____/____/\____/_/ |_/   /____/            \____/_/ /_/_/  |_/_/     /_/ /_____/_/ |_|   /_/

    def l2_chapter1(self):
        """ Lesson 2: C Scale
            LESSON that teaches the C scale."""

        # Destorys other GUI modules
        self.lesson2_panel.destroy()
        self.lesson2_sub.destroy()
        self.chapter1.destroy()
        self.chapter2.destroy()
        self.logo.destroy()

        # C scale diagram
        self.c_image = ImageTk.PhotoImage(Image.open('images/notes/c_scale.png')) 
        self.cScaleImg = Tkinter.Label(self.window, image=self.c_image, bg="black", height=410, width=410) 

        # Text
        self.img1 = ImageTk.PhotoImage(Image.open('images/text/lesson2_chapter1/txt1.png'))
        self.text1 = Tkinter.Label(self.window, image=self.img1, bg="black", height=50, width=410)

        # Piano Virtuoso logo
        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        # Next button
        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nexto.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=80, command=self.l2_chapter1_next1)

        # Maps modules to GUI
        self.cScaleImg.grid(row=0, column=0, columnspan=5, rowspan=15)
        self.text1.grid(row=13, column=1)
        self.logo.grid(row=0, column=1)
        self.next_bttn.grid(row=14, column=1)

    def l2_chapter1_next1(self):
        self.text1.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson2_chapter1/txt2.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nexto.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=80, command=self.l2_chapter1_next2)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1)

    def l2_chapter1_next2(self):
        self.text1.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson2_chapter1/txt3.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nexto.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=80, command=self.l2_chapter1_next3)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1)      

    def l2_chapter1_next3(self):
        self.text1.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson2_chapter1/txt4.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nexto.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=80, command=self.l2_chapter1_next4)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1)      

    def l2_chapter1_next4(self):
        self.text1.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson2_chapter1/txt5.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/c_scale.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=120, command=self.c_scale)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1)   

    #    ______   _____ _________    __    ______
    #   / ____/  / ___// ____/   |  / /   / ____/
    #  / /       \__ \/ /   / /| | / /   / __/
    # / /___    ___/ / /___/ ___ |/ /___/ /___
    # \____/   /____/\____/_/  |_/_____/_____/
    def c_scale(self):
        """ Mini game - C scale
            Has the user play the C scale - C, D, E, F, G, A, B, C - 5 times to complete. """
        self.text2.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        piano.detect_key()
        if piano.piano_key == [] or piano.piano_key[0][0][0] == 128:
            pass
        else:
            print piano.display_note(piano.piano_key[0][0][1]) # Prints pressed note to console.
            piano.play_note(piano.piano_key[0][0][1])   # Plays sound when pressed.

            #Puts user input into list
            scale.user_input = scale.input_to_list(piano.piano_key[0][0][1]) 

            # Empty list to fill with user input once note is parsed.
            user_input_notes = []

            # Each note is parsed to only include the note pressed, no number - then put in a list
            for item in scale.user_input:
                temp_key = piano.display_note(item)
                parsed_note = piano.parse_key(temp_key) # Parses note to slice off the number at end.

                user_input_notes.append(parsed_note) # Adds parsed note to user_input_notes

                i = 0  # Counter for list positions.

                # Converts both lists to strings for easy comparison
                user_str = ''.join(user_input_notes)
                c = ''.join(scale.c_scale) # C D E F G A B C

                if self.l2c1_score >= 5:
                    self.l2c1_score = 0 #Sets score back to 0
                    self.cScaleImg.destroy()
                    self.logo.destroy()
                    self.correct.destroy()
                    if self.wrong > 0:
                        #pygame.midi.quit() #Quits out of midi
                        self.try_again.destroy()
                        self.wrong = 0

                    # Clears out previous input
                    scale.user_input = []
                    user_input_notes = []
                    i = 0

                    self.l2c1_complete += 1 #Completed level is set to true

                    # If user completed both chapter 1 & chapter 2, goes to next lesson
                    if self.l2c1_complete > 0 and self.l2c2_complete > 0:
                        self.l3_main_menu()
                    # Otherwise, goes back to current lesson's main menu
                    else:
                        self.l2_main_menu()
                    break

                # Correct input
                if user_input_notes == scale.c_scale:
                    self.l2c1_score = self.l2c1_score + 1
                    print self.l2c1_score

                    try: #Plays note correct sound effect.
                        sound = pygame.mixer.Sound("sound/sfx/S3K_A9.wav")
                        sound.play(loops = 0)
                    except pygame.error, message:
                            print "Cannot load sound: " + sound_name
                            raise SystemExit, message

                    scale.user_input = []
                    user_input_notes = []

                    str_score = str(self.l2c1_score)
                    self.correct_txt = ImageTk.PhotoImage(Image.open('images/text/lesson2_chapter1/C_Scale/good' + str_score + '.png'))
                    self.correct = Tkinter.Label(self.window, image=self.correct_txt, bg="black", height=25, width=410)

                    self.correct.grid(row=4, column=0, columnspan=5, rowspan=15)

                # Wrong input
                elif (len(user_str) == len(c)) and (user_str != c):
                    self.wrong = self.wrong + 1

                    try: #Plays note wrong sound effect.
                        sound = pygame.mixer.Sound("sound/sfx/S3K_B2.wav")
                        sound.play(loops = 0)
                    except pygame.error, message:
                        print "Cannot load sound: " + sound_name
                        raise SystemExit, message

                    scale.user_input = []
                    user_input_notes = []
                    i = 0

                    self.try_text = ImageTk.PhotoImage(Image.open('images/text/lesson2_chapter1/C_Scale/try_again.png'))
                    self.try_again = Tkinter.Label(self.window, image=self.try_text, bg="black", height=25, width=410)

                    self.try_again.grid(row=4, column=0, columnspan=2, rowspan=15)
                else:
                    i = i + 1
        self.window.after(1, self.c_scale)

    #     __    ________________ ____  _   __   ___               ________  _____    ____  ________________     ___
    #    / /   / ____/ ___/ ___// __ \/ | / /  |__ \             / ____/ / / /   |  / __ \/_  __/ ____/ __ \   |__ \
    #   / /   / __/  \__ \\__ \/ / / /  |/ /   __/ /   ______   / /   / /_/ / /| | / /_/ / / / / __/ / /_/ /   __/ /
    #  / /___/ /___ ___/ /__/ / /_/ / /|  /   / __/   /_____/  / /___/ __  / ___ |/ ____/ / / / /___/ _, _/   / __/
    # /_____/_____//____/____/\____/_/ |_/   /____/            \____/_/ /_/_/  |_/_/     /_/ /_____/_/ |_|   /____/

    def l2_chapter2(self):

        # Destorys other GUI modules
        self.lesson2_panel.destroy()
        self.lesson2_sub.destroy()
        self.chapter1.destroy()
        self.chapter2.destroy()
        self.logo.destroy()

        # Keyboard diagram
        self.chrom = ImageTk.PhotoImage(Image.open('images/notes/chromatic.png')) 
        self.chromaticImg = Tkinter.Label(self.window, image=self.chrom, bg="black", height=410, width=410) 

        # Text
        self.img1 = ImageTk.PhotoImage(Image.open('images/text/lesson2_chapter2/txt1.png'))
        self.text1 = Tkinter.Label(self.window, image=self.img1, bg="black", height=50, width=410)

        # Piano Virtuoso logo
        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        # Next button
        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nexto.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=80, command=self.l2_chapter2_next1)

        # Maps modules to GUI
        self.chromaticImg.grid(row=0, column=0, columnspan=5, rowspan=15)
        self.text1.grid(row=13, column=1)
        self.logo.grid(row=0, column=1)
        self.next_bttn.grid(row=14, column=1)

    def l2_chapter2_next1(self):
        self.text1.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson2_chapter2/txt2.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nexto.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=120, command=self.l2_chapter2_next2)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1)  

    def l2_chapter2_next2(self):
        self.text1.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson2_chapter2/txt3.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nexto.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=120, command=self.l2_chapter2_next3)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1)  

    def l2_chapter2_next3(self):
        self.text2.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson2_chapter2/txt4.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nexto.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=120, command=self.l2_chapter2_next4)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1) 

    def l2_chapter2_next4(self):
        self.text2.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson2_chapter2/txt5.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nexto.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=120, command=self.l2_chapter2_next5)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1) 

    def l2_chapter2_next5(self):
        self.text2.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson2_chapter2/txt6.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nexto.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=120, command=self.l2_chapter2_next6)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1) 

    def l2_chapter2_next6(self):
        self.text2.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson2_chapter2/txt7.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/chromatic.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=150, command=self.chromatic_scale)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1) 

    #    ________  ______  ____  __  ______  ________________   _____ _________    __    ______
    #   / ____/ / / / __ \/ __ \/  |/  /   |/_  __/  _/ ____/  / ___// ____/   |  / /   / ____/
    #  / /   / /_/ / /_/ / / / / /|_/ / /| | / /  / // /       \__ \/ /   / /| | / /   / __/
    # / /___/ __  / _, _/ /_/ / /  / / ___ |/ / _/ // /___    ___/ / /___/ ___ |/ /___/ /___
    # \____/_/ /_/_/ |_|\____/_/  /_/_/  |_/_/ /___/\____/   /____/\____/_/  |_/_____/_____/

    def chromatic_scale(self):
        """ Mini game - Chromatic scale
            Has the user play the Chromatic scale 5 times to complete. """
        self.text2.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        piano.detect_key()
        if piano.piano_key == [] or piano.piano_key[0][0][0] == 128:
            pass
        else:
            print piano.display_note(piano.piano_key[0][0][1]) # Prints pressed note to console.
            piano.play_note(piano.piano_key[0][0][1])   # Plays sound when pressed.

            #Puts user input into list
            scale.user_input = scale.input_to_list(piano.piano_key[0][0][1]) 

            # Empty list to fill with user input once note is parsed.
            user_input_notes = []

            # Each note is parsed to only include the note pressed, no number - then put in a list
            for item in scale.user_input:
                temp_key = piano.display_note(item)
                parsed_note = piano.parse_key(temp_key) # Parses note to slice off the number at end.

                user_input_notes.append(parsed_note) # Adds parsed note to user_input_notes

                i = 0  # Counter for list positions.

                # Converts both lists to strings for easy comparison
                user_str = ''.join(user_input_notes)
                chrom = ''.join(scale.chromatic) # c c# d d# e f f# g g# a a# b c

                if self.l2c2_score >= 5:
                    self.l2c2_score = 0 #Sets score back to 0
                    self.chromaticImg.destroy()
                    self.logo.destroy()
                    self.correct.destroy()
                    if self.wrong > 0:
                        #pygame.midi.quit() #Quits out of midi
                        self.try_again.destroy()
                        self.wrong = 0

                    # Clears out previous input
                    scale.user_input = []
                    user_input_notes = []
                    i = 0

                    self.l2c2_complete += 1 #Completed level is set to true

                    # If user completed both chapter 1 & chapter 2, goes to next lesson
                    if self.l2c1_complete > 0 and self.l2c2_complete > 0:
                        self.l3_main_menu()
                    # Otherwise, goes back to current lesson's main menu
                    else:
                        self.l2_main_menu()
                    break

                # Correct input
                if user_input_notes == scale.chromatic:
                    self.l2c2_score = self.l2c2_score + 1
                    print self.l2c2_score

                    try: #Plays note correct sound effect.
                        sound = pygame.mixer.Sound("sound/sfx/S3K_A9.wav")
                        sound.play(loops = 0)
                    except pygame.error, message:
                            print "Cannot load sound: " + sound_name
                            raise SystemExit, message

                    scale.user_input = []
                    user_input_notes = []

                    str_score = str(self.l2c2_score)
                    self.correct_txt = ImageTk.PhotoImage(Image.open('images/text/lesson2_chapter2/Chromatic_Scale/good' + str_score + '.png'))
                    self.correct = Tkinter.Label(self.window, image=self.correct_txt, bg="black", height=25, width=410)

                    self.correct.grid(row=4, column=0, columnspan=5, rowspan=15)

                # Wrong input
                elif (len(user_str) == len(chrom)) and (user_str != chrom):
                    self.wrong = self.wrong + 1

                    try: #Plays note wrong sound effect.
                        sound = pygame.mixer.Sound("sound/sfx/S3K_B2.wav")
                        sound.play(loops = 0)
                    except pygame.error, message:
                        print "Cannot load sound: " + sound_name
                        raise SystemExit, message

                    scale.user_input = []
                    user_input_notes = []
                    i = 0

                    self.try_text = ImageTk.PhotoImage(Image.open('images/text/lesson2_chapter2/Chromatic_Scale/try_again.png'))
                    self.try_again = Tkinter.Label(self.window, image=self.try_text, bg="black", height=25, width=410)

                    self.try_again.grid(row=4, column=0, columnspan=2, rowspan=15)
                else:
                    i = i + 1
        self.window.after(1, self.chromatic_scale)

    #     __    ________________ ____  _   __   _____    __  ______    _____   __   __  __________   ____  __
    #    / /   / ____/ ___/ ___// __ \/ | / /  |__  /   /  |/  /   |  /  _/ | / /  /  |/  / ____/ | / / / / /
    #   / /   / __/  \__ \\__ \/ / / /  |/ /    /_ <   / /|_/ / /| |  / //  |/ /  / /|_/ / __/ /  |/ / / / /
    #  / /___/ /___ ___/ /__/ / /_/ / /|  /   ___/ /  / /  / / ___ |_/ // /|  /  / /  / / /___/ /|  / /_/ /
    # /_____/_____//____/____/\____/_/ |_/   /____/  /_/  /_/_/  |_/___/_/ |_/  /_/  /_/_____/_/ |_/\____/

    def l3_main_menu(self):
        """ Displays the main menu of lesson 3. """
        self.titlePanel.destroy()
        self.start.destroy()
        self.exit.destroy()

        # Image variables
        self.lesson3_header = ImageTk.PhotoImage(Image.open("images/headers/lesson3.png"))
        self.lesson3_subhead = ImageTk.PhotoImage(Image.open("images/headers/lesson3a.png"))
        self.chapter1_text = ImageTk.PhotoImage(Image.open("images/buttons/l3c1.png"))
        self.chapter2_text = ImageTk.PhotoImage(Image.open("images/buttons/l3c2.png"))
        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))

        # Lesson 3 panel
        self.lesson3_panel = Tkinter.Label(self.window, bg="black", image=self.lesson3_header, height=410, width=410)
        self.lesson3_sub = Tkinter.Label(self.window, bg="black", image=self.lesson3_subhead, height=25, width=400)
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=115)

        # Lesson 3 Buttons Initialization
        self.chapter1 = Tkinter.Button(self.window, image=self.chapter1_text, command=self.l3_chapter1, bd=1, bg="black", height=25, width=115)
        self.chapter2 = Tkinter.Button(self.window, image=self.chapter2_text, command=self.l3_chapter2, bd=1, bg="black", height=25, width=115)
        # change command to command=self.l1_chapter2

        self.lesson3_panel.grid(row=0, column=0, columnspan=5, rowspan=11)
        self.lesson3_sub.grid(row=8, column=0)
        self.chapter1.grid(row=9, column=0)
        self.chapter2.grid(row=10, column=0)
        self.logo.grid(row=0, column=0)

    #     __    ________________ ____  _   __   _____             ________  _____    ____  ________________     ___
    #    / /   / ____/ ___/ ___// __ \/ | / /  |__  /            / ____/ / / /   |  / __ \/_  __/ ____/ __ \   <  /
    #   / /   / __/  \__ \\__ \/ / / /  |/ /    /_ <   ______   / /   / /_/ / /| | / /_/ / / / / __/ / /_/ /   / /
    #  / /___/ /___ ___/ /__/ / /_/ / /|  /   ___/ /  /_____/  / /___/ __  / ___ |/ ____/ / / / /___/ _, _/   / /
    # /_____/_____//____/____/\____/_/ |_/   /____/            \____/_/ /_/_/  |_/_/     /_/ /_____/_/ |_|   /_/

    def l3_chapter1(self):
        """ Lesson 3, Chapter 1: F & G Scales
            Teaches about the F and G scales, as well as what accidentals, sharps, and flats are."""

        # Destorys other GUI modules
        self.lesson3_panel.destroy()
        self.lesson3_sub.destroy()
        self.chapter1.destroy()
        self.chapter2.destroy()
        self.logo.destroy()

        # Keyboard diagram
        self.fg_img = ImageTk.PhotoImage(Image.open('images/notes/fg.png')) 
        self.fgImg = Tkinter.Label(self.window, image=self.fg_img, bg="black", height=450, width=410) 

        # Text
        self.img1 = ImageTk.PhotoImage(Image.open('images/text/lesson3_chapter1/txt1.png'))
        self.text1 = Tkinter.Label(self.window, image=self.img1, bg="black", height=50, width=410)

        # Piano Virtuoso logo
        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        # Next button
        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nexty.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=80, command=self.l3_chapter1_next1)

        # Maps modules to GUI
        self.fgImg.grid(row=0, column=0, columnspan=5, rowspan=15)
        self.text1.grid(row=13, column=1)
        self.logo.grid(row=0, column=1)
        self.next_bttn.grid(row=14, column=1)

    def l3_chapter1_next1(self):
        self.text1.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson3_chapter1/txt2.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nexty.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=80, command=self.l3_chapter1_next2)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1)

    def l3_chapter1_next2(self):
        self.text1.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson3_chapter1/txt3.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nexty.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=80, command=self.l3_chapter1_next3)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1)      

    def l3_chapter1_next3(self):
        self.text1.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson3_chapter1/txt4.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nexty.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=80, command=self.l3_chapter1_next4)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1)      

    def l3_chapter1_next4(self):
        self.text1.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson3_chapter1/txt5.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nexty.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=120, command=self.l3_chapter1_next5)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1) 

    def l3_chapter1_next5(self):
        self.text1.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson3_chapter1/txt6.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nexty.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=120, command=self.l3_chapter1_next6)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1) 

    def l3_chapter1_next6(self):
        self.text1.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson3_chapter1/txt7.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nexty.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=120, command=self.l3_chapter1_next7)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1) 

    def l3_chapter1_next7(self):
        self.text1.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson3_chapter1/txt8.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nexty.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=120, command=self.l3_chapter1_next8)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1) 

    def l3_chapter1_next8(self):
        self.text1.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson3_chapter1/txt9.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/fg_scale.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=170, command=self.fg_scale)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1) 

    #     ______   ___        ______   _____ _________    __    ___________
    #    / ____/  ( _ )      / ____/  / ___// ____/   |  / /   / ____/ ___/
    #   / /_     / __ \/|   / / __    \__ \/ /   / /| | / /   / __/  \__ \
    #  / __/    / /_/  <   / /_/ /   ___/ / /___/ ___ |/ /___/ /___ ___/ /
    # /_/       \____/\/   \____/   /____/\____/_/  |_/_____/_____//____/

    def fg_scale(self):
        """ Mini game - Chromatic scale
            Has the user play the F & G scales 5 times each to complete. """
        self.text2.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        piano.detect_key()

        if self.l3c1_score == 0:
            self.ftxt = ImageTk.PhotoImage(Image.open('images/text/lesson3_chapter1/Fg_Scale/f_scaletxt.png'))
            self.f_txt = Tkinter.Label(self.window, image=self.ftxt, bg="black", height=25, width=410)
            self.f_txt.grid(row=9, column=0, columnspan=5, rowspan=15)        

        if piano.piano_key == [] or piano.piano_key[0][0][0] == 128:
            pass
        else:
            print piano.display_note(piano.piano_key[0][0][1]) # Prints pressed note to console.
            piano.play_note(piano.piano_key[0][0][1])   # Plays sound when pressed.

            #Puts user input into list
            scale.user_input = scale.input_to_list(piano.piano_key[0][0][1]) 

            # Empty list to fill with user input once note is parsed.
            user_input_notes = []

            # Each note is parsed to only include the note pressed, no number - then put in a list
            for item in scale.user_input:
                temp_key = piano.display_note(item)
                parsed_note = piano.parse_key(temp_key) # Parses note to slice off the number at end.

                user_input_notes.append(parsed_note) # Adds parsed note to user_input_notes

                i = 0  # Counter for list positions.

                # Converts user input list to string for easy comparison
                user_str = ''.join(user_input_notes)

                # If current score is even, use F scale as comparison list & convert to string
                if self.l3c1_score % 2 == 0:
                    fg = ''.join(scale.f_scale) # F G A Bb C D E F
                    current_scale = scale.f_scale
                # Otherwise, use G scale
                else:
                    fg = ''.join(scale.g_scale) # G A B C D E F# G
                    current_scale = scale.g_scale

                if self.l3c1_score >= 10:
                    self.l3c1_score = 0 #Sets score back to 0
                    self.fgImg.destroy()
                    self.f_txt.destroy()
                    self.logo.destroy()
                    self.correct.destroy()
                    if self.wrong > 0:
                        #pygame.midi.quit() #Quits out of midi
                        self.try_again.destroy()
                        self.wrong = 0

                    # Clears out previous input
                    scale.user_input = []
                    user_input_notes = []
                    i = 0

                    self.l3c1_complete += 1 #Completed level is set to true

                    # If user completed both chapter 1 & chapter 2, goes to next lesson
                    if self.l3c1_complete > 0 and self.l3c2_complete > 0:
                        self.l4_main_menu()
                    # Otherwise, goes back to current lesson's main menu
                    else:
                        self.l3_main_menu()
                    break

                # Correct input
                if user_input_notes == current_scale:
                    self.l3c1_score = self.l3c1_score + 1
                    print self.l3c1_score

                    try: #Plays note correct sound effect.
                        sound = pygame.mixer.Sound("sound/sfx/S3K_A9.wav")
                        sound.play(loops = 0)
                    except pygame.error, message:
                        print "Cannot load sound: " + sound_name
                        raise SystemExit, message

                    scale.user_input = []
                    user_input_notes = []

                    str_score = str(self.l3c1_score)
                    self.correct_txt = ImageTk.PhotoImage(Image.open('images/text/lesson3_chapter1/Fg_Scale/good' + str_score + '.png'))
                    self.correct = Tkinter.Label(self.window, image=self.correct_txt, bg="black", height=25, width=410)

                    self.correct.grid(row=9, column=0, columnspan=5, rowspan=15)

                # Wrong input
                elif (len(user_str) == len(fg)) and (user_str != fg):
                    self.wrong = self.wrong + 1

                    try: #Plays note wrong sound effect.
                        sound = pygame.mixer.Sound("sound/sfx/S3K_B2.wav")
                        sound.play(loops = 0)
                    except pygame.error, message:
                        print "Cannot load sound: " + sound_name
                        raise SystemExit, message

                    scale.user_input = []
                    user_input_notes = []
                    i = 0

                    self.try_text = ImageTk.PhotoImage(Image.open('images/text/lesson3_chapter1/Fg_Scale/try_again.png'))
                    self.try_again = Tkinter.Label(self.window, image=self.try_text, bg="black", height=25, width=410)

                    self.try_again.grid(row=9, column=0, columnspan=2, rowspan=15)
                else:
                    i = i + 1
        self.window.after(1, self.fg_scale)


    #     __    ________________ ____  _   __   _____             ________  _____    ____  ________________     ___
    #    / /   / ____/ ___/ ___// __ \/ | / /  |__  /            / ____/ / / /   |  / __ \/_  __/ ____/ __ \   |__ \
    #   / /   / __/  \__ \\__ \/ / / /  |/ /    /_ <   ______   / /   / /_/ / /| | / /_/ / / / / __/ / /_/ /   __/ /
    #  / /___/ /___ ___/ /__/ / /_/ / /|  /   ___/ /  /_____/  / /___/ __  / ___ |/ ____/ / / / /___/ _, _/   / __/
    # /_____/_____//____/____/\____/_/ |_/   /____/            \____/_/ /_/_/  |_/_/     /_/ /_____/_/ |_|   /____/

    def l3_chapter2(self):
        """ Lesson 3, Chapter 2: Other Chords
            This chapter teaches about the D, A, E, and B scales. It also touches on the Circle of Fifths."""

        # Destorys other GUI modules
        self.lesson3_panel.destroy()
        self.lesson3_sub.destroy()
        self.chapter1.destroy()
        self.chapter2.destroy()
        self.logo.destroy()

        # Keyboard diagram
        self.cirof5 = ImageTk.PhotoImage(Image.open('images/notes/co5sm.png')) 
        self.circleoffifths = Tkinter.Label(self.window, image=self.cirof5, bg="black", height=500, width=410) 

        # Text
        self.img1 = ImageTk.PhotoImage(Image.open('images/text/lesson3_chapter2/txt1.png'))
        self.text1 = Tkinter.Label(self.window, image=self.img1, bg="black", height=50, width=410)

        # Piano Virtuoso logo
        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        # Next button
        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nexty.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=80, command=self.l3_chapter2_next1)

        # Maps modules to GUI
        self.circleoffifths.grid(row=0, column=0, columnspan=5, rowspan=15)
        self.text1.grid(row=13, column=1)
        self.logo.grid(row=0, column=1)
        self.next_bttn.grid(row=14, column=1)

    def l3_chapter2_next1(self):
        self.text1.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson3_chapter2/txt2.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nexty.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=80, command=self.l3_chapter2_next2)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1)

    def l3_chapter2_next2(self):
        self.text2.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson3_chapter2/txt3.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nexty.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=80, command=self.l3_chapter2_next3)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1)      

    def l3_chapter2_next3(self):
        self.text2.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson3_chapter2/txt4.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nexty.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=80, command=self.l3_chapter2_next4)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1)      

    def l3_chapter2_next4(self):
        self.text2.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()
        self.circleoffifths.destroy()

        self.scale_pic = ImageTk.PhotoImage(Image.open('images/notes/d_scale.png')) 
        self.scale = Tkinter.Label(self.window, image=self.scale_pic, bg="black", height=500, width=410)

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson3_chapter2/txt5.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nexty.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=120, command=self.l3_chapter2_next5)

        self.scale.grid(row=0, column=0, columnspan=5, rowspan=15)
        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1) 

    def l3_chapter2_next5(self):
        self.text2.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()
        self.scale.destroy()

        self.scale_pic = ImageTk.PhotoImage(Image.open('images/notes/a_scale.png')) 
        self.scale = Tkinter.Label(self.window, image=self.scale_pic, bg="black", height=500, width=410)

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson3_chapter2/txt6.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nexty.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=120, command=self.l3_chapter2_next6)

        self.scale.grid(row=0, column=0, columnspan=5, rowspan=15)
        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1) 

    def l3_chapter2_next6(self):
        self.text2.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()
        self.scale.destroy()

        self.scale_pic = ImageTk.PhotoImage(Image.open('images/notes/e_scale.png')) 
        self.scale = Tkinter.Label(self.window, image=self.scale_pic, bg="black", height=500, width=410)

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson3_chapter2/txt7.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nexty.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=120, command=self.l3_chapter2_next7)

        self.scale.grid(row=0, column=0, columnspan=5, rowspan=15)
        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1) 

    def l3_chapter2_next7(self):
        self.text2.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()
        self.scale.destroy()

        self.scale_pic = ImageTk.PhotoImage(Image.open('images/notes/b_scale.png')) 
        self.scale = Tkinter.Label(self.window, image=self.scale_pic, bg="black", height=500, width=410)

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson3_chapter2/txt8.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nexty.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=120, command=self.l3_chapter2_next8)

        self.scale.grid(row=0, column=0, columnspan=5, rowspan=15)
        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1) 

    def l3_chapter2_next8(self):
        self.text2.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson3_chapter2/txt9.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/scales.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=170, command=self.pre_other_scales)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1) 

    #    ____  ________  ____________     _____ _________    __    ___________
    #   / __ \/_  __/ / / / ____/ __ \   / ___// ____/   |  / /   / ____/ ___/
    #  / / / / / / / /_/ / __/ / /_/ /   \__ \/ /   / /| | / /   / __/  \__ \
    # / /_/ / / / / __  / /___/ _, _/   ___/ / /___/ ___ |/ /___/ /___ ___/ /
    # \____/ /_/ /_/ /_/_____/_/ |_|   /____/\____/_/  |_/_____/_____//____/

    def pre_other_scales(self):
        """ Mini game - Other scale
            Has the user play the scales D, E, A & B in a randomized order. """
        self.text2.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()
        self.scale.destroy()

        # Generates random word from dict.
        self.list_scale = scale.random_chord_deab()

        str_scale = ''.join(self.list_scale) 

        # Text that tells user which scale to play
        self.playscale = ImageTk.PhotoImage(Image.open('images/text/lesson3_chapter2/Other_Scales/' + str_scale + '.png')) 
        self.play_scale = Tkinter.Label(self.window, image=self.playscale, bg="black", height=25, width=400)

        # Displays corresponding chart to scale to be played
        self.scalechart = ImageTk.PhotoImage(Image.open('images/notes/l3c2/' + str_scale + '.png'))
        self.scale_chart = Tkinter.Label(self.window, image=self.scalechart, bg="black", height=410, width=410)

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.scale_chart.grid(row=0, column=0, columnspan=5, rowspan=15)
        self.play_scale.grid(row=7, column=0)
        self.logo.grid(row=0, column=0)
        
        self.other_scales()

    def other_scales(self):
        """ Mini game - Other scale
            Has the user play the scales D, E, A & B in a randomized order. """

        piano.detect_key()
        if piano.piano_key == [] or piano.piano_key[0][0][0] == 128:
            pass
        else:
            print piano.display_note(piano.piano_key[0][0][1]) # Prints pressed note to console.
            piano.play_note(piano.piano_key[0][0][1])   # Plays sound when pressed.

            #Puts user input into list
            scale.user_input = scale.input_to_list(piano.piano_key[0][0][1]) 

            # Empty list to fill with user input once note is parsed.
            user_input_notes = []

            # Each note is parsed to only include the note pressed, no number - then put in a list
            for item in scale.user_input:
                temp_key = piano.display_note(item)
                parsed_note = piano.parse_key(temp_key) # Parses note to slice off the number at end.

                user_input_notes.append(parsed_note) # Adds parsed note to user_input_notes

                i = 0  # Counter for list positions.

                #random_scale = scale.random_chord_deab()

                # Converts both lists to strings for easy comparison
                user_str = ''.join(user_input_notes)
                rand_scale = ''.join(self.list_scale)

                if self.l3c2_score >= 15:
                    self.l3c2_score = 0 #Sets score back to 0
                    self.scale_chart.destroy()
                    self.logo.destroy()
                    self.play_scale.destroy()
                    if self.wrong > 0:
                        #pygame.midi.quit() #Quits out of midi
                        self.try_again.destroy()
                        self.wrong = 0

                        # Clears out previous input
                        scale.user_input = []
                        scale.current_scale = []
                        user_input_notes = []
                        i = 0

                        self.l2c2_complete += 1 #Completed level is set to true

                    # If user completed both chapter 1 & chapter 2, goes to next lesson
                    if self.l3c2_complete > 0 and self.l3c2_complete > 0:
                        self.l4_main_menu()
                    # Otherwise, goes back to current lesson's main menu
                    else:
                        self.l3_main_menu()
                    break

                # Correct input
                if user_input_notes == self.list_scale:
                    self.l3c2_score = self.l3c2_score + 1
                    print self.l3c2_score

                    try: #Plays note correct sound effect.
                        sound = pygame.mixer.Sound("sound/sfx/S3K_A9.wav")
                        sound.play(loops = 0)
                    except pygame.error, message:
                            print "Cannot load sound: " + sound_name
                            raise SystemExit, message

                    scale.user_input = []
                    user_input_notes = []
                    self.scale_chart.destroy()
                    self.play_scale.destroy()

                    self.list_scale = scale.random_chord_deab()

                    str_scale = ''.join(self.list_scale) 

                    # Text that tells user which scale to play
                    self.playscale = ImageTk.PhotoImage(Image.open('images/text/lesson3_chapter2/Other_Scales/' + str_scale + '.png')) 
                    self.play_scale = Tkinter.Label(self.window, image=self.playscale, bg="black", height=25, width=400)

                    # Displays corresponding chart to scale to be played
                    self.scalechart = ImageTk.PhotoImage(Image.open('images/notes/l3c2/' + str_scale + '.png'))
                    self.scale_chart = Tkinter.Label(self.window, image=self.scalechart, bg="black", height=410, width=410)

                    self.scale_chart.grid(row=0, column=0, columnspan=5, rowspan=15)
                    self.play_scale.grid(row=7, column=0)

                # Wrong input
                elif (len(user_str) == len(rand_scale)) and (user_str != rand_scale):
                    self.wrong = self.wrong + 1

                    try: #Plays note wrong sound effect.
                        sound = pygame.mixer.Sound("sound/sfx/S3K_B2.wav")
                        sound.play(loops = 0)
                    except pygame.error, message:
                        print "Cannot load sound: " + sound_name
                        raise SystemExit, message

                    scale.user_input = []
                    user_input_notes = []
                    i = 0

                    self.try_text = ImageTk.PhotoImage(Image.open('images/text/lesson3_chapter2/Other_Scales/try_again.png'))
                    self.try_again = Tkinter.Label(self.window, image=self.try_text, bg="black", height=25, width=410)

                    self.try_again.grid(row=4, column=0, columnspan=2, rowspan=15)
                else:
                    i = i + 1
        self.window.after(1, self.other_scales)

    #     __    ________________ ____  _   __   __ __     __  ______    _____   __   __  __________   ____  __
    #    / /   / ____/ ___/ ___// __ \/ | / /  / // /    /  |/  /   |  /  _/ | / /  /  |/  / ____/ | / / / / /
    #   / /   / __/  \__ \\__ \/ / / /  |/ /  / // /_   / /|_/ / /| |  / //  |/ /  / /|_/ / __/ /  |/ / / / /
    #  / /___/ /___ ___/ /__/ / /_/ / /|  /  /__  __/  / /  / / ___ |_/ // /|  /  / /  / / /___/ /|  / /_/ /
    # /_____/_____//____/____/\____/_/ |_/     /_/    /_/  /_/_/  |_/___/_/ |_/  /_/  /_/_____/_/ |_/\____/

    def l4_main_menu(self):
        """ Displays the main menu of lesson 3. """
        self.titlePanel.destroy()
        self.start.destroy()
        self.exit.destroy()

        # Image variables
        self.lesson4_header = ImageTk.PhotoImage(Image.open("images/headers/lesson4.png"))
        self.lesson4_subhead = ImageTk.PhotoImage(Image.open("images/headers/lesson4a.png"))
        self.chapter1_text = ImageTk.PhotoImage(Image.open("images/buttons/l4c1.png"))
        self.chapter2_text = ImageTk.PhotoImage(Image.open("images/buttons/l4c2.png"))
        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))

        # Lesson 3 panel
        self.lesson4_panel = Tkinter.Label(self.window, bg="black", image=self.lesson4_header, height=410, width=410)
        self.lesson4_sub = Tkinter.Label(self.window, bg="black", image=self.lesson4_subhead, height=25, width=400)
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=115)

        # Lesson 3 Buttons Initialization
        self.chapter1 = Tkinter.Button(self.window, image=self.chapter1_text, command=self.l4_chapter1, bd=1, bg="black", height=25, width=115)
        self.chapter2 = Tkinter.Button(self.window, image=self.chapter2_text, command=self.l2_chapter2, bd=1, bg="black", height=25, width=115)
        # change command to command=self.l1_chapter2

        self.lesson4_panel.grid(row=0, column=0, columnspan=5, rowspan=11)
        self.lesson4_sub.grid(row=8, column=0)
        self.chapter1.grid(row=9, column=0)
        self.chapter2.grid(row=10, column=0)
        self.logo.grid(row=0, column=0)

    #     __    ________________ ____  _   __   __ __              ________  _____    ____  ________________     ___
    #    / /   / ____/ ___/ ___// __ \/ | / /  / // /             / ____/ / / /   |  / __ \/_  __/ ____/ __ \   <  /
    #   / /   / __/  \__ \\__ \/ / / /  |/ /  / // /_   ______   / /   / /_/ / /| | / /_/ / / / / __/ / /_/ /   / /
    #  / /___/ /___ ___/ /__/ / /_/ / /|  /  /__  __/  /_____/  / /___/ __  / ___ |/ ____/ / / / /___/ _, _/   / /
    # /_____/_____//____/____/\____/_/ |_/     /_/              \____/_/ /_/_/  |_/_/     /_/ /_____/_/ |_|   /_/

    def l4_chapter1(self):
        """ Lesson 1: Keys on Piano Keyboard
            LESSON that teaches what the keys on a keyboard are."""

        # Destorys other GUI modules
        self.lesson4_panel.destroy()
        self.lesson4_sub.destroy()
        self.chapter1.destroy()
        self.chapter2.destroy()
        self.logo.destroy()

        # Keyboard diagram
        self.key_loc = ImageTk.PhotoImage(Image.open('images/notes/fg.png')) 
        self.keyboard = Tkinter.Label(self.window, image=self.key_loc, bg="black", height=450, width=410) 

        # Text
        self.img1 = ImageTk.PhotoImage(Image.open('images/text/lesson4_chapter1/txt1.png'))
        self.text1 = Tkinter.Label(self.window, image=self.img1, bg="black", height=50, width=410)

        # Piano Virtuoso logo
        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        # Next button
        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nextg.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=80, command=self.l4_chapter1_next1)

        # Maps modules to GUI
        self.keyboard.grid(row=0, column=0, columnspan=5, rowspan=15)
        self.text1.grid(row=13, column=1)
        self.logo.grid(row=0, column=1)
        self.next_bttn.grid(row=14, column=1)

    def l4_chapter1_next1(self):
        self.text1.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson4_chapter1/txt2.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nextg.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=80, command=self.l4_chapter1_next2)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1)

    def l4_chapter1_next2(self):
        self.text1.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson4_chapter1/txt3.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nextg.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=80, command=self.l4_chapter1_next3)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1)      

    def l4_chapter1_next3(self):
        self.text1.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson4_chapter1/txt4.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nextg.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=80, command=self.l4_chapter1_next4)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1)      

    def l4_chapter1_next4(self):
        self.text1.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson4_chapter1/txt5.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nextg.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=120, command=self.l4_chapter1_next5)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1) 

    def l4_chapter1_next5(self):
        self.text1.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson4_chapter1/txt6.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nextg.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=120, command=self.l4_chapter1_next6)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1) 

    def l4_chapter1_next6(self):
        self.text1.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson4_chapter1/txt7.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nextg.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=120, command=self.l4_chapter1_next7)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1) 

    def l4_chapter1_next7(self):
        self.text1.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson4_chapter1/txt8.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nextg.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=120, command=self.l4_chapter1_next8)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1) 

    def l4_chapter1_next8(self):
        self.text1.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson4_chapter1/txt9.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/major_chords.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=170, command=self.l4_chapter1_next2)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1) 

    #     __    ________________ ____  _   __   __ __              ________  _____    ____  ________________     ___
    #    / /   / ____/ ___/ ___// __ \/ | / /  / // /             / ____/ / / /   |  / __ \/_  __/ ____/ __ \   |__ \
    #   / /   / __/  \__ \\__ \/ / / /  |/ /  / // /_   ______   / /   / /_/ / /| | / /_/ / / / / __/ / /_/ /   __/ /
    #  / /___/ /___ ___/ /__/ / /_/ / /|  /  /__  __/  /_____/  / /___/ __  / ___ |/ ____/ / / / /___/ _, _/   / __/
    # /_____/_____//____/____/\____/_/ |_/     /_/              \____/_/ /_/_/  |_/_/     /_/ /_____/_/ |_|   /____/

    def l4_chapter2(self):
        """ Lesson 1: Keys on Piano Keyboard
            LESSON that teaches what the keys on a keyboard are."""

        # Destorys other GUI modules
        self.lesson4_panel.destroy()
        self.lesson4_sub.destroy()
        self.chapter1.destroy()
        self.chapter2.destroy()
        self.logo.destroy()

        # Keyboard diagram
        self.key_loc = ImageTk.PhotoImage(Image.open('images/notes/fg.png')) 
        self.keyboard = Tkinter.Label(self.window, image=self.key_loc, bg="black", height=450, width=410) 

        # Text
        self.img1 = ImageTk.PhotoImage(Image.open('images/text/lesson4_chapter2/txt1.png'))
        self.text1 = Tkinter.Label(self.window, image=self.img1, bg="black", height=50, width=410)

        # Piano Virtuoso logo
        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        # Next button
        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nextg.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=80, command=self.l4_chapter2_next1)

        # Maps modules to GUI
        self.keyboard.grid(row=0, column=0, columnspan=5, rowspan=15)
        self.text1.grid(row=13, column=1)
        self.logo.grid(row=0, column=1)
        self.next_bttn.grid(row=14, column=1)

    def l4_chapter2_next1(self):
        self.text1.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson4_chapter2/txt2.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nextg.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=80, command=self.l4_chapter2_next2)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1)

    def l4_chapter2_next2(self):
        self.text1.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson4_chapter2/txt3.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nextg.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=80, command=self.l4_chapter2_next3)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1)      

    def l4_chapter2_next3(self):
        self.text1.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson4_chapter2/txt4.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nextg.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=80, command=self.l4_chapter2_next4)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1)      

    def l4_chapter2_next4(self):
        self.text1.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson4_chapter2/txt5.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nextg.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=120, command=self.l4_chapter2_next5)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1) 

    def l4_chapter2_next5(self):
        self.text1.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson4_chapter2/txt6.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nextg.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=120, command=self.l4_chapter2_next6)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1) 

    def l4_chapter2_next6(self):
        self.text1.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson4_chapter2/txt7.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nextg.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=120, command=self.l4_chapter2_next7)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1) 

    def l4_chapter2_next7(self):
        self.text1.destroy()
        self.next_bttn.destroy()
        self.logo.destroy()

        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        self.img2 = ImageTk.PhotoImage(Image.open('images/text/lesson4_chapter2/txt8.png'))
        self.text2 = Tkinter.Label(self.window, image=self.img2, bg="black", height=80, width=410)

        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/nextg.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=120, command=self.l4_chapter2_next1)

        self.text2.grid(row=13, column=1)
        self.next_bttn.grid(row=14, column=1)
        self.logo.grid(row=0, column=1) 

    #     __    ________________ ____  _   __   ______   __  ______    _____   __   __  __________   ____  __
    #    / /   / ____/ ___/ ___// __ \/ | / /  / ____/  /  |/  /   |  /  _/ | / /  /  |/  / ____/ | / / / / /
    #   / /   / __/  \__ \\__ \/ / / /  |/ /  /___ \   / /|_/ / /| |  / //  |/ /  / /|_/ / __/ /  |/ / / / /
    #  / /___/ /___ ___/ /__/ / /_/ / /|  /  ____/ /  / /  / / ___ |_/ // /|  /  / /  / / /___/ /|  / /_/ /
    # /_____/_____//____/____/\____/_/ |_/  /_____/  /_/  /_/_/  |_/___/_/ |_/  /_/  /_/_____/_/ |_/\____/

    def l5_main_menu(self):
        """ Displays the main menu of lesson 3. """
        self.titlePanel.destroy()
        self.start.destroy()
        self.exit.destroy()

        # Image variables
        self.lesson5_header = ImageTk.PhotoImage(Image.open("images/headers/lesson5.png"))
        self.lesson5_subhead = ImageTk.PhotoImage(Image.open("images/headers/lesson5a.png"))
        self.mashup_button = ImageTk.PhotoImage(Image.open("images/buttons/mashup.png"))
        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))

        # Lesson 3 panel
        self.lesson5_panel = Tkinter.Label(self.window, bg="black", image=self.lesson5_header, height=410, width=410)
        self.lesson5_sub = Tkinter.Label(self.window, bg="black", image=self.lesson5_subhead, height=25, width=410)
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=115)

        # Lesson 3 Buttons Initialization
        self.chapter1 = Tkinter.Button(self.window, image=self.mashup_button, command=self.l5, bd=1, bg="black", height=25, width=210)
        # change command to command=self.l1_chapter2

        self.lesson5_panel.grid(row=0, column=0, columnspan=10, rowspan=10)
        self.lesson5_sub.grid(row=6, column=1)
        self.chapter1.grid(row=7, column=1)
        self.logo.grid(row=0, column=1)

    def l5(self):
        """ Lesson 1: Keys on Piano Keyboard
            LESSON that teaches what the keys on a keyboard are."""

        # Destorys other GUI modules
        self.lesson5_panel.destroy()
        self.lesson5_sub.destroy()
        self.chapter1.destroy()
        self.logo.destroy()

        self.pic = ImageTk.PhotoImage(Image.open('images/notes/minigamemash.png'))
        self.window_panel = Tkinter.Label(self.window, image=self.pic, bg="black", height=450, width=410) 

        # Text
        self.img1 = ImageTk.PhotoImage(Image.open('images/text/lesson5/txt1.png'))
        self.text1 = Tkinter.Label(self.window, image=self.img1, bg="black", height=50, width=410)

        # Piano Virtuoso logo
        self.pv = ImageTk.PhotoImage(Image.open("images/title/pv.png"))
        self.logo = Tkinter.Label(self.window, bg="black", image=self.pv, height=25, width=150)

        # Next button
        self.next_txt = ImageTk.PhotoImage(Image.open('images/buttons/startb.png'))
        self.next_bttn = Tkinter.Button(self.window, image=self.next_txt, bd=0, bg="black", height=25, width=80, command=self.l4_chapter1_next1)

        # Maps modules to GUI
        self.window_panel.grid(row=0, column=0, columnspan=5, rowspan=15)
        self.text1.grid(row=13, column=1)
        self.logo.grid(row=0, column=1)
        self.next_bttn.grid(row=14, column=1)


if __name__ == '__main__':
    mw = MainWindow()
    mw.window.mainloop()
    pygame.midi.quit()