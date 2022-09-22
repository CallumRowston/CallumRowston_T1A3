from wordle_logic import WordleLogic, WordLengthError, NotRealWordError
from colorama import Fore
from simple_term_menu import TerminalMenu
import wordle_settings
import os
import json

WORD_LENGTH_SETTING = 5
TOTAL_GUESSES_SETTING = 6

# Main game loop and Menus
def main_menu():
    """Main menu to navigate to the main game, rules, stats or quit."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Welcome to {Fore.GREEN}PY{Fore.YELLOW}WORDLE{Fore.RESET}\nUse up and down arrow keys to navigate menu.\nPress ENTER to select an option.\n")
    print(WORD_LENGTH_SETTING) #debug
    print(TOTAL_GUESSES_SETTING) #debug
    options = ["Play PyWordle", "Rules", "Game Settings", "Stats", "Quit"]
    main_menu_display = TerminalMenu(options)
    menu_entry_index = main_menu_display.show()
    if options[menu_entry_index] == "Play PyWordle":
        play_pywordle()
    elif options[menu_entry_index] == "Rules":
        rules()
    elif options[menu_entry_index] == "Game Settings":
        wordle_settings.game_settings_menu()
    elif options[menu_entry_index] == "Stats":
        display_stats()
    elif options[menu_entry_index] == "Quit":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Quitting {Fore.GREEN}PY{Fore.YELLOW}WORDLE{Fore.RESET}...\nSee you next time!")

def play_pywordle():
    """Main gameplay loop. Calls methods from instance of WordleLogic class."""
    os.system('cls' if os.name == 'nt' else 'clear')
    wordle = WordleLogic(WORD_LENGTH_SETTING, TOTAL_GUESSES_SETTING)
    print(wordle.secret_word) # debug
    print(wordle.word_length)
    print(wordle.total_guesses)
    while wordle.play_wordle:
        try:
            user_guess = input("Enter a 5 letter word: ").upper()
            wordle.validate_user_guess(user_guess)
        except (WordLengthError, NotRealWordError) as err:
            print(err)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            wordle.display_colored_guess(wordle.compare_user_guess())
            if wordle.user_wins:
                if wordle.guess_count == 1:
                    print(f"\nWOW! You guessed it in 1 attempt!\n")
                else:
                    print(f"\nYou won in {wordle.guess_count} guesses!\n")
                wordle.add_game_stats()
                end_menu()
            if wordle.user_loses:
                print("You have used all your guesses. Game over!")
                print(f"The correct word was {wordle.secret_word}\n")
                wordle.add_game_stats()
                end_menu()

def rules():
    """Prints the rules for the game on a clear terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(
        "~~ Rules ~~\n\n"
        "Guess the word in 6 tries.\n"
        "Each guess must be a valid 5-letter word.\n"
        "Hit ENTER to submit your guess.\n"
        "After each guess, the color of the letters will change\n"
        "to show how close your guess was to the word.\n\n"
        f"{Fore.GREEN}GREEN{Fore.RESET} letters are in the correct spot.\n"
        f"{Fore.YELLOW}YELLOW{Fore.RESET} letters are in the word but in the wrong spot.\n"
        "WHITE letters are not in the word anywhere.\n"
        )

    rules_options = ["Back to Main Menu"]
    rules_menu_display = TerminalMenu(rules_options)
    menu_entry_index = rules_menu_display.show()
    print("Press ENTER to return to the main menu.")
    if rules_options[menu_entry_index] == "Back to Main Menu":
        main_menu()


def display_stats():
    """Displays statistics from JSON file."""
    os.system('cls' if os.name == 'nt' else 'clear')
    with open("stats.json", "r") as stats:
        data = json.load(stats)
        overall_stats = data["Overall Stats"]
        guess_distribution = data["Guess Distribution"]
        print(f"~~ {Fore.GREEN}Your {Fore.YELLOW}Stats{Fore.RESET} ~~\n")
        for key, value in overall_stats.items():
            print("{:<24} {:<24}".format(Fore.BLUE + key + Fore.RESET, value) + "\n")
        print("{:<8} {:<8}".format(Fore.GREEN + 'Guesses', Fore.YELLOW + 'Distribution' + Fore.RESET))
        for key, value in guess_distribution.items():
            print("{:<8} {:<8}".format(key, value))
        print("")

    stats_options = ["Back to Main Menu", "Exit to Desktop"]
    stats_menu_display = TerminalMenu(stats_options)
    menu_entry_index = stats_menu_display.show()
    os.system('cls' if os.name == 'nt' else 'clear')
    if stats_options[menu_entry_index] == "Back to Main Menu":
        main_menu()
    elif stats_options[menu_entry_index] == "Exit to Desktop":
        print(f"Quitting {Fore.GREEN}PY{Fore.YELLOW}WORDLE{Fore.RESET}...\nSee you next time!")

def end_menu():
    """Displays menu upon game end."""
    end_options = ["Play Again", "Exit to Main Menu", "Exit to Desktop"]
    end_menu_display = TerminalMenu(end_options)
    menu_entry_index = end_menu_display.show()
    os.system('cls' if os.name == 'nt' else 'clear')
    if end_options[menu_entry_index] == "Play Again":
        play_pywordle()
    elif end_options[menu_entry_index] == "Exit to Main Menu":
        main_menu()
    elif end_options[menu_entry_index] == "Exit to Desktop":
        print(f"Quitting {Fore.GREEN}PY{Fore.YELLOW}WORDLE{Fore.RESET}...\nSee you next time!")

if __name__ == '__main__':
    main_menu()
