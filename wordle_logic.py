import random

# All logic of game. Sends computed logic to wordle.game.
class WordleLogic:

    def __init__(self):
        with open('word_list_5.txt') as f:
            self.secret_word = random.choice(f.readlines())
        self.current_guess = ''
        self.guess_history = []
        self.total_guesses = 6
        self.word_length = 5

    @property
    def play_wordle(self):
        return not self.user_wins and not self.game_over

    @property
    def user_wins(self):
        return self.current_guess == self.secret_word

    @property
    def game_over(self):
        return len(self.guess_history) == self.total_guesses

    def validate_user_guess(self, user_guess):
        if len(user_guess) != self.word_length:
            print(f"Your guess must be {self.word_length} letters long.\n")    

    def add_user_guess(self, user_guess):
        self.guess_history.append(user_guess)
        self.current_guess = user_guess

    def compare_user_guess(self):
        guess_result = []
        for char in range(5):
            if self.current_guess[char] == self.secret_word[char]:
                guess_result.append(self.current_guess[char] + 'green')
            elif self.current_guess[char] in self.secret_word:
                guess_result.append(self.current_guess[char] + 'yellow')
            else:
                guess_result.append(self.current_guess[char])
        return guess_result

# TODO: Randomly choose secret word from word_list
    # def pick_secret_word(self):
    #     # secret_word = random.choice(word_list) 
    #     ## hardcode word for testing while developing
    #     secret_word = 'crate'.upper()
    #     return secret_word


# TODO: Receive user guess from wordle_game
# Check guess is 5 letters, is in word_list
# Raise exception(s) if not 5 letters, not in word_list
# Add user guess to guess list


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
# # Provide stats to wordle_game if user requests
