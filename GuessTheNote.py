#    ________  __________________    ________  ________   _   ______  ____________
#   / ____/ / / / ____/ ___/ ___/   /_  __/ / / / ____/  / | / / __ \/_  __/ ____/
#  / / __/ / / / __/  \__ \\__ \     / / / /_/ / __/    /  |/ / / / / / / / __/
# / /_/ / /_/ / /___ ___/ /__/ /    / / / __  / /___   / /|  / /_/ / / / / /___
# \____/\____/_____//____/____/    /_/ /_/ /_/_____/  /_/ |_/\____/ /_/ /_____/

import random

class GuessTheNote:
    def __init__(self):
        self.note = ""

    def randomize_note(self):
        self.note_num = random.randint(1, 7)

        note_rand = {
            1: 'C',
            2: 'D',
            3: 'E',
            4: 'F',
            5: 'G',
            6: 'A',
            7: 'B'
        }

        return note_rand[self.note_num]

    @staticmethod
    def display_image(note):
        picture = {
            'C': 'C.png',
            'D': 'D.png',
            'E': 'E.png',
            'F': 'F.png',
            'G': 'G.png',
            'A': 'A.png',
            'B': 'B.png'
        }

        return picture[note]