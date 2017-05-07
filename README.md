# Piano Virtuoso

Piano Virtuoso is an education video game that teaches its players how to play piano and read music. Using lessons that increase in difficulty, the player is both challenged and engaged at all times. Each lesson features several mini games that cohere with a particular lesson to create a fun aspect while learning.

Piano Virtuoso is designed for all ages; anyone who wishes to learn how to play piano can! All that is needed is a MIDI controller to start a musical journey.

This current version features 5 different lessons. With the exception of lesson 5, all lessons have 2 chapters which include a related mini game to help learn the concept within the chapter. Lesson 5 is a recap of what has been learned through lessons 1 - 4.

## Getting Started

These instructions will help install and run this program. 

### Prerequisites

[Python 2.7](https://www.python.org/downloads/) is required.

### Hardware

A MIDI controller (USB piano keyboard) is needed to control and play the game. If no MIDI controller is available, this game CANNOT work. If on Windows, the MIDI controller driver must be installed. The driver varies depending on which brand MIDI controller is being used. 

If needed, an affordable MIDI controller is the [midiplus AKM320 (32 keys)](http://a.co/8TdnfLH) at $35.

A better quality MIDI controller, [Akai Professional MPK Mini (25 keys)](http://a.co/6og8L8X) is available for $99.

The same MIDI controller used to program this project is the [Novation Impulse (49 keys)](http://a.co/cFtrm0i).

### Installing & Running

Download the ZIP file and extract it. Navigate to the extracted file. To run program, open a terminal and enter:
```
python MainWindow.py
```

## Built With

* [Python 2.7](https://www.python.org/) - Language used to code program

* [pygame](http://www.pygame.org/hifi.html) & [Tkinter](https://wiki.python.org/moin/TkInter) - Libraries used for MIDI controller, sound & GUI support

* [Sublime Text 3](https://www.sublimetext.com/) - Text editor & compiler used to test/run code

## Known Bugs

* If user hits two keys at the same time, input runs indefinietly rather than stopping when correct/incorrect input is entered.

* On some lessons, certain graphics are coded to be hidden, however they are still visible. This happens randomly, but it is fixed once another mini game starts.

* The first text on lesson 3 chapter 1's mini game blinks rapidly. This quickly goes away once the lesson is complete, however.

* After completing lesson 3 chapter 2, the game immediately goes to the Lesson 4 main menu, instead of going to the 'Lesson complete' page. 

* Lesson 5's mini game freezes whole program. FIXED 5/7/2017

## Authors

* **Amanda Ciampa** - *All work* - [amanda-ciampa](https://github.com/amanda-ciampa)

## Acknowledgments

All those who approached me saying they wish they knew how to play an instrument - where my idea for this project originally came from