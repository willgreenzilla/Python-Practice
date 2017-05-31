# hangman.py
Simple hangman script modified from The Self Taught Programmer by Cory Althoff.

This is a very simple Python script hangman game modified from The Self Taught Programmer to add some extra functionality while I am learning Python.

Added the following above what was in the original script:

1) Pulls a random 7 letter or less word from /usr/share/dict/words (Linux) and strips 's from the end of any word.
2) Keeps track of incorrectly guessed letters and displays this list to the player.
3) Error checks selection and only allows selection of a letter (no numbers and symbols).

Issues:

Currently only works on Linux... I need to fix random word selection in Windows still.
