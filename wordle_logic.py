import wordle_game
import random

# All logic of game. Sends computed logic to wordle.game. 

# TODO: Randomly choose secret word from word_list

# TODO: Receive user guess from wordle_game
# Check guess is 5 letters, is in word_list
# Raise exception(s) if not 5 letters, not in word_list

# TODO: Compare user guess against secret word
# Wrong letters = grey
# Correct letters, wrong spot = yellow
# Correct letters, correct spot = green
# Return colored string to wordle_game

# TODO: Track and loop attempts
# Increment attempts counter each time user input received
# Prompt user for guess while attempts < 6 and user guess != secret word
# If attempts = 6, check if user guess = secret word, else end game

# TODO: Game end scenarios
# If user guess = secret word, tell wordle_game user wins
# If user guess != secret word and attempts = 6, tell wordle_game user loses
# User quits

# TODO: Game stats and highscore
# Store game results when game ends 
# Fastest time to solve, streaks, least attempts, attempt distribution
# Provide stats to wordle_game if user requests