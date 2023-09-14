# File: Wordle.py

"""
Wordle Game. 9/13/23 Team 4
"""
#Milestone 1 & 2 Finished -->

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS
from WordleGraphics import CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def Wordle():
    # Startup code
    gw = WordleGWindow()
    wordActual = random.choice(FIVE_LETTER_WORDS)

    #Write the enter_action function. This function will be called when the user presses ENTER
    def enter_action(s):
        rowCurrent = gw.get_current_row()
        wordCurrent = ""

        #Use a loop that runs from column 0 to N_COLS (which is 5) to fill each box with a letter from the selected word
        for letter in range(0, N_COLS):
            letterCurrent = gw.get_square_letter(rowCurrent, letter)
            wordCurrent += letterCurrent
        wordCurrent = wordCurrent.lower()

        #Inside enter_action, check if the typed word is a legitimate English word
        #need a way to validate words against a list of legitimate English words 
        if wordCurrent in FIVE_LETTER_WORDS:
            wordActual_list = list(wordActual)

            for i in range(N_COLS):
                guess_the_letter = wordCurrent[i]

                if guess_the_letter == wordActual[i]:
                    wordActual_list[i] = None

            if wordCurrent == wordActual:
                gw.show_message("Congratulations! It took you " + str(rowCurrent + 1) + " guess(es)!")
                gw.remove_enter_listener(enter_action)
                gw.window.set_key_enabled(False)

            else:

                if rowCurrent == N_ROWS - 1:
                    gw.show_message("Sorry, try again!")
                    gw.remove_enter_listener(enter_action)
                    gw.window.set_key_enabled(False)

                else:
                    gw.set_current_row(rowCurrent + 1)

        #If the typed word is not legitimate, display "Not in word list" using the show_message method
        else:
            gw.show_message("Not in wordlist")
        
    gw.show_message("The correct word is " + wordActual.upper())
    #Use the add_enter_listener method to respond to the ENTER key press event
    #Call gw.add_enter_listener(enter_action) to set up a function (enter_action) to be called when ENTER is pressed
    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
     Wordle()


