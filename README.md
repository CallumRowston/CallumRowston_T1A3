# Welcome to PYWORDLE !

## R4 - Repo
[GitHub Repository](https://github.com/CallumRowston/CallumRowston_T1A3)

## Table Of Contents

- [Related Documents]()
- [Features]()
- [Implementation Plan]()

## Related Documents

Help File

Trello

## R6 - Features

### Coloured Game Board

The main game board features colourised feedback that changes depending on the players guess each round. Just as in the original Wordle game, green letters indicate correct letter in the correct position, yellow letters indicate correct letter but in the wrong position, and white letters indicate the letter is not in the secret word at all. This makes the game visually and logically appealing, and easy to follow as the game progresses

### Default Mode

The default mode randomly selects a secret 5 letter word to be guessed by the player. The user then has 6 attempts to guess the word. After each guess their most recent guess and any previous guesses from the current game are displayed in colour according to the correctness of the players guess.

### Statistics

At the end of each game played with default settings, stats of the game are recorded. The user can then access these stats via the main menu to view their total games played, total games won, win percentage, and their guess distribution - how many times they have taken X amount of guesses to guess the secret word.

### Custom Game Settings

The player can set the secret word length to 5(default), 6, 7 or 8 and the length of the secret word will change to that number. The player can also set the amount of guesses they are allowed per word to 6(default), 7, 8 or 9. The user then is allowed this many guesses at the secret word before they lose. A menu option to reset these settings to default is provided in the game settings menu to easily revert any changes the user has made.

### Menus

Outside of the main gameplay loop, a menu system has been implemented to navigate to dfferent pages; a rules page to explain how to play, a stats page to display the players statistics, a game settings page with further menus to input settings, and a quit option to exit the application

## Implementation Plan - [Trello Board](https://trello.com/b/LimXSz09/wordle-app-t1a3)

Trello was used to track and manage the status of tasks required to develop this application. Each feature is listed below in order of development along with a checklist of requirements to implement it. 

### Default Mode

- Have the game select a random word from a list of words
- Take user input as a guess and check it is valid (is an actual word, is 5 letters)
- Handle any exceptions if the guess is not valid and prompt the user to guess again.
- Compare the user guess to the secret word and mark letters accordingly
- Print this output to the terminal
- Prompt the user to guess again
- If the user guessed it, say they won
- If the user ran out of guessses, say they lost
- Provide an option to play again

### Coloured Game Board

- Use the markings attached to each letter in the players guess to colour the output in the terminal
- Correct letters, correct position marked green
- Correct letters, wrong position marked yellow
- Incorrect letters not coloured
- Ensure letters that appear once in the secret word but twice in the users guess are only coloured once in the terminal output

###  Statistics 

- Create a JSON file formatted to accept the required statistics
- At game end, store the gueeses taken, if the game was won and add 1 to total games played
- Add these stats to the JSON file
- Create a way for the user to view the stats - print the JSON file formatted neatly

### Custom Game Settings

- Ensure the default mode works if the secret word length is longer or the total guesses allowed is longer
- Provide the user a way to enter input to change the word lenght or total guesses values
- Handle any exceptions relating to the user input
- Provide a way for the user to reset these values
- Display the changed values
- Inform the user the statistics feature is turned off if they are not playing with default settings

### Menus

- Allow navigation between different features
- Add menu option to play the main game
- Add rules menu option to link to a static page explaining rules
- Add stats menu option to link to a static page displaying the stats
- Add game settings menu option to go to custom game settings feature
- Add sub menu options to return to the mian menu
- Add menu option to quit the application

## R3 - References

Terminal Application idea heavily influenced by Wordle, created by Josh Wardle. Original game accessed at: https://www.nytimes.com/games/wordle/index.html

5 letter word list. Stanford University Computer Science Facility. Accessed: https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt

6 letter word list. TheFreeDictionary by Farlex. Accessed: https://www.thefreedictionary.com/6-letter-words.htm

7 letter word list. TheFreeDictionary by Farlex. Accessed: https://www.thefreedictionary.com/7-letter-words.htm

8 letter word list. TheFreeDictionary by Farlex. Accessed: https://www.thefreedictionary.com/8-letter-words.htm

## Style Guide

Style Guide: [PEP 8 - Style Guide For Python Code](https://peps.python.org/pep-0008/)