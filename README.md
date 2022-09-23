# Welcome to PYWORDLE !

## R4 - Repo
[GitHub Repository](https://github.com/CallumRowston/CallumRowston_T1A3)

## Related Documents

Help File

Trello

## R3 and R5 - References

Terminal Application idea heavily influenced by Wordle, created by Josh Wardle. Play at https://www.nytimes.com/games/wordle/index.html

Style Guide: [PEP 8 - Style Guide For Python Code](https://peps.python.org/pep-0008/)

5 letter word list. Stanford University Computer Science Facility. Accessed: https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt

6 letter word list. TheFreeDictionary by Farlex. Accessed: https://www.thefreedictionary.com/6-letter-words.htm

7 letter word list. TheFreeDictionary by Farlex. Accessed: https://www.thefreedictionary.com/7-letter-words.htm

8 letter word list. TheFreeDictionary by Farlex. Accessed: https://www.thefreedictionary.com/8-letter-words.htm

## R6 - Features

### Default Mode

The default mode randomly selects a secret 5 letter word to be guessed by the user. The user then has 6 attempts to guess the word. After each guess their most recent guess and any previous guesses from the current game are displayed. Green letters indicate correct letter in the correct position, yellow letters indicate correct letter but in the wrong position, and white letters indicate the letter is not in the secret word at all.

### Custom Game Settings

They can set the secret word length to 5(default), 6, 7 or 8 and the length of the secret word and the length of the allowed users guess will change to that number. The user can also set the amount of guesses they are allowed per word to 6(default), 7, 8 or 9. The user then is allowed this many guesses at the secret word before the they lose. A menu option to reset these settings to default is provided in the game settings menu to easily revert any changes the user has made.

### Statistics

At the end of each game played with default settings, stats of the game are recorded. The user can then access these stats via the main menu to view their total games played, total games won, win percentage, and their guess distribution - how many times they have taken X amount of guesses to guess the secret word.

