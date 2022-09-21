import random
from colorama import Fore
import json

class WordleLogic:
    """
    Contains all logical functionality behind the main gameplay loop and passes relevant data to wordle_game.py to be displayed when required
    """
    def __init__(self, total_guesses=6, word_length=5):
        self.secret_word_list = []
        self.secret_word = ''
        self.current_guess = ''
        self.total_guesses = total_guesses
        self.guess_count = 0
        self.word_length = word_length
        self.set_secret_word()

    @property
    def play_wordle(self):
        return not self.user_wins and not self.user_loses

    @property
    def user_wins(self):
        return self.current_guess == self.secret_word

    @property
    def user_loses(self):
        return self.guess_count == self.total_guesses

    def set_secret_word(self):
        """
        Uses word list in text file to randomly select a secret word to be guessed
        """
        with open('word_list_5.txt') as f:
            for word in f.readlines():
                self.secret_word_list.append(word.strip())
            self.secret_word = random.choice(self.secret_word_list)
        
    def validate_user_guess(self, user_guess):
        """
        Checks user guess is valid input before setting as instance variable
        Raises:
            WordLengthError: Checks user guess is 5 characters long
            NotRealWordError: Checks user guess is in the word list
        """
        
        if len(user_guess) != self.word_length:
            raise WordLengthError(f"Your guess must be {self.word_length} letters long. Guess again.")
        if user_guess not in self.secret_word_list:
            raise NotRealWordError(f"{user_guess} is not a valid word. Guess again.")
        else:
            self.current_guess = user_guess
            self.guess_count += 1
        return self.current_guess

    def compare_user_guess(self):
        """_summary_
        Checks user guess against the secret word and marks each letter as correct, wrong position or incorrect
        Returns:
            List: Letters of user guess marked if correct or not
        """
        save_secret_word = self.secret_word
        guess_result = ["-"] * self.word_length
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
        print(guess_result)
        return guess_result

    def display_colored_guess(self, guess_list):
        """
        Turns list from compare_user_guess into a list of colored letters depending on their state and prints them.
        """
        colored_guess = []
        colored_results = []
        for letter in guess_list:
            if 'green' in letter:
                color = Fore.GREEN
            elif 'yellow' in letter:
                color = Fore.YELLOW
            else:
                color = Fore.WHITE
            colored_guess.append(color + "  " + letter[0] + Fore.RESET)

        colored_guess_str = "".join(colored_guess)
        colored_results.append(colored_guess_str)
        for i in colored_results:
            print(i)

    def add_game_stats(self):
        """
        Adds results of the game to the JSON file statistics
        """
        with open('stats.json', 'r') as stats:
            data = json.load(stats)
            data['Guess Distribution'][str(self.guess_count)] += 1
            data["Overall Stats"]["Games Played"] += 1
            if self.user_wins:
                data["Overall Stats"]["Games Won"] += 1
            data["Overall Stats"]["Win %"] = round(data["Overall Stats"]["Games Won"] / data["Overall Stats"]["Games Played"] * 100)
             
        with open('stats.json', 'w') as stats:
            json.dump(data, stats, indent=4)

class WordLengthError(Exception):
    pass

class NotRealWordError(Exception):
    pass
