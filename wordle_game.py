from wordle_logic import WordleLogic, WordLengthError, NotRealWordError
from colorama import Fore
from simple_term_menu import TerminalMenu
import os
# Interface between user and game.

# TODO: Welcome user to game, options for quit, rules, stats, game options
def main_menu():
    print("Welcome to " + Fore.GREEN + "PY" + Fore.YELLOW + "WORDLE" + Fore.RESET + "\nUse up and down arrow keys to navigate menu. \nPress ENTER to select.")
    options = ["Play PyWordle", "Game Settings", "Stats", "Quit"]
    main_menu = TerminalMenu(options)
    menu_entry_index = main_menu.show()
    if options[menu_entry_index] == "Play PyWordle":
        play_pywordle()
    elif options[menu_entry_index] == "Game Settings":
        game_settings()
    elif options[menu_entry_index] == "Stats":
        display_stats()
    elif options[menu_entry_index] == "Quit":
        print("Quitting application...")

# TODO: Dispaly user guess as colored result
def play_pywordle():
    os.system('cls' if os.name == 'nt' else 'clear')
    wordle = WordleLogic()
    
    print(wordle.secret_word) # debug
    while wordle.play_wordle:
        try:
            user_guess = input("Enter a 5 letter word: ").upper()
            wordle.validate_user_guess(user_guess)
        except WordLengthError as err:
            print(err)
        except NotRealWordError as err:
            print(err)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            wordle.add_user_guess(user_guess)
            wordle.display_colored_guess(wordle.compare_user_guess())
            for _ in range(wordle.total_guesses - len(wordle.guess_history)):
                print("  _  _  _  _  _")
            if wordle.user_wins:
                print("You win!")
                wordle.add_game_stats()
                end_menu()
            if wordle.user_loses:
                print("You have used all your guesses. Game over!")
                print(f"The correct word was {wordle.secret_word}")
                wordle.add_game_stats()
                end_menu()

        # print("current guess = " + wordle.current_guess) # debug
        # print("secret word = " + wordle.secret_word) # debug

def game_settings():
    pass

def display_stats():
    # with open("stats.json" "r") as stats:

# TODO: Display end game win/loss. Play again? Quit?
def end_menu():
    end_options = ["Play Again", "Exit to Main Menu", "Exit to Desktop"]
    end_menu_display = TerminalMenu(end_options)
    menu_entry_index = end_menu_display.show()
    os.system('cls' if os.name == 'nt' else 'clear')
    if end_options[menu_entry_index] == "Play Again":
        play_pywordle()
    elif end_options[menu_entry_index] == "Exit to Main Menu":
        main_menu()
    elif end_options[menu_entry_index] == "Exit to Desktop":
        print("Quitting application...")


# TODO: Format game interface to look user friendly
# Spacing
# _ _ _ _ _ to signify a remaining attempt
# Border?

# Gameplay Loop

if __name__ == '__main__':
    main_menu()
    
