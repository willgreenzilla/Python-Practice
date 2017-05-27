# hangman.py
# will green
# 5/26/2017
# expanded on from the hangman example in The Self-taught Programmer by Cory Althoff

import random
from string import ascii_lowercase

def hangman(word):
    wrong = 0
    wronglist = []
    stages = ["",
            "__________        ",
            "|        |        ",
            "|        0        ",
            "|       /|\       ",
            "|       / \       ",
            "|                 ",
             ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    checkset = tuple(ascii_lowercase)

    print("\nWelcome to Hangman")

    while wrong < len(stages) - 1:
        print("\nWrong Letter List: {}".format(wronglist))
        msg = "\nGuess a letter: "
        char = raw_input(msg).lower()
        print("")

        if char not in checkset:

            while char not in checkset:
                print("You must only choose a LETTER. No numbers and symbols please...")
                char = raw_input(msg).lower()

        if char in rletters:
            lettercount = rletters.count(char)
            
            while lettercount > 0:
                cind = rletters.index(char)
                board[cind] = char
                rletters[cind] = '$'
                lettercount -= 1
        
        else:
            wrong += 1
            if char not in wronglist:
                wronglist.append(char)
        
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))

        if "__" not in board:
            print("\nYOU WIN!! The word was >> {} <<\n".format(word))
            win = True
            break

    if not win:
        print("\n".join(stages[0: wrong]))
        print("\nYOU LOSE!! the word was >> {} <<\n".format(word))

def randomPicker():
    dictlist = "/usr/share/dict/words"
    randomlist = open(dictlist).read().splitlines()
    randomword = "xxxxxxxx"
    
    while len(randomword) > 7:
        randomword = (random.choice(randomlist)).lower()

    if randomword[-2:] == "'s":
        randomword = randomword[0:-2]
    
    print(randomword)
    return randomword

def main():
    hangman(randomPicker())

main()