import random
import statistics
from colorama import Fore
import json
# All logic of game. Sends computed logic to wordle.game.


class WordleLogic:

    def __init__(self):
        self.secret_word = ''
        self.secret_word_list = []
        self.current_guess = ''
        self.guess_history = []
        self.colored_results = []
        self.total_guesses = 6
        self.count = 0
        self.word_length = 5
        self.pick_secret_word()

    @property
    def play_wordle(self):
        return not self.user_wins and not self.user_loses

    @property
    def user_wins(self):
        return self.current_guess == self.secret_word

    @property
    def user_loses(self):
        return len(self.guess_history) == self.total_guesses

    def pick_secret_word(self):
        with open('word_list_5.txt') as f:
            for word in f.readlines():
                self.secret_word_list.append(word.strip())
            self.secret_word = random.choice(self.secret_word_list)
        
    def validate_user_guess(self, user_guess):
        if len(user_guess) != self.word_length:
            raise WordLengthError(f"Your guess must be {self.word_length} letters long.\n")
        if user_guess not in self.secret_word_list:
            raise NotRealWordError(f"{user_guess} is not a valid word. Guess again.")
    
    def add_user_guess(self, user_guess):
        self.guess_history.append(user_guess)
        self.count += 1
        self.current_guess = user_guess

    def compare_user_guess(self):
        save_secret_word = self.secret_word
        guess_result = ["-"] * len(self.secret_word)
        for index, (guess_char, target_char) in enumerate(zip(self.current_guess, self.secret_word)):
            if guess_char == target_char:
                guess_result[index] = guess_char + "green"
                self.secret_word = self.secret_word.replace(guess_char, "-")
        
        for index, (guess_char, target_char) in enumerate(zip(self.current_guess, self.secret_word)):
            if guess_char in self.secret_word and guess_result[index] == "-":
                guess_result[index] = guess_char + "yellow"
                self.secret_word = self.secret_word.replace(guess_char, "-")

        for index, letter in enumerate(guess_result):
            if letter == "-":
                guess_result[index] = self.current_guess[index]

        self.secret_word = save_secret_word
        return guess_result

    def display_colored_guess(self, guess):
        colored_guess = []
        for letter in guess:
            if 'green' in letter:
                color = Fore.GREEN
            elif 'yellow' in letter:
                color = Fore.YELLOW
            else:
                color = Fore.WHITE
            colored_guess.append(color + "  " + letter[0] + Fore.RESET)

        colored_guess_str = "".join(colored_guess)
        self.colored_results.append(colored_guess_str)
        for i in self.colored_results:
            print(i)

    def add_game_stats(self):
        with open('stats.json', 'r') as stats:
            data = json.load(stats)
            print(data)

            data['Guess Distribution'][str(self.count)] += 1
            data["Overall Stats"]["Games Played"] += 1
            if self.user_wins:
                data["Overall Stats"]["Games Won"] += 1
            data["Overall Stats"]["Win %"] = round(data["Overall Stats"]["Games Won"] / data["Overall Stats"]["Games Played"] * 100)
            print(data)
             
        with open('stats.json', 'w') as stats:
            json.dump(data, stats, indent=4)



class WordLengthError(Exception):
    pass

class NotRealWordError(Exception):
    pass

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
