from wordle_logic import WordleLogic, WordLengthError, NotRealWordError
from colorama import Fore
from simple_term_menu import TerminalMenu
import wordle_rules
import wordle_settings
import wordle_stats
import os
# import json

WORD_LENGTH_SETTING = 5
TOTAL_GUESSES_SETTING = 6

# Main game loop and Main Menu
def main_menu():
    """Main menu to navigate to the main game, rules, settings, stats or quit."""
    clear_screen()
    print(
        f"Welcome to {Fore.GREEN}PY{Fore.YELLOW}WORDLE{Fore.RESET}\n\n"
        "Use up and down arrow keys to navigate menu.\n"
        "Press ENTER to select an option.\n"
        )
    options = ["Play PyWordle", "Rules", "Game Settings", "Stats", "Quit"]
    main_menu_display = TerminalMenu(options)
    menu_entry_index = main_menu_display.show()
    clear_screen()
    if options[menu_entry_index] == "Play PyWordle":
        play_pywordle()
    elif options[menu_entry_index] == "Rules":
        wordle_rules.display_rules()
    elif options[menu_entry_index] == "Game Settings":
        wordle_settings.game_settings_menu()
    elif options[menu_entry_index] == "Stats":
        wordle_stats.display_stats()
    elif options[menu_entry_index] == "Quit":
        quit_messager()

def play_pywordle():
    """Main gameplay loop. Calls methods from instance of WordleLogic class."""
    wordle = WordleLogic(WORD_LENGTH_SETTING, TOTAL_GUESSES_SETTING)
    while wordle.play_wordle:
        try:
            user_guess = input(f"Enter a {WORD_LENGTH_SETTING} letter word: ").upper()
            wordle.validate_user_guess(user_guess)
        except (WordLengthError, NotRealWordError) as err:
            print(err)
        else:
            clear_screen()
            wordle.display_colored_guess(wordle.compare_user_guess())
            if wordle.user_wins or wordle.user_loses and wordle.is_default:
                wordle.add_game_stats()
            if wordle.user_wins:
                if wordle.guess_count == 1:
                    print(f"\nWOW! You guessed it in 1 attempt!\n")
                else:
                    print(f"\nYou won in {wordle.guess_count} guesses!\n")
                end_menu()
            if wordle.user_loses:
                print("You have used all your guesses. Game over!")
                print(f"The correct word was {wordle.secret_word}\n")
                end_menu()

# def display_rules():
#     """Displays the rules for the game"""
#     clear_screen()
#     print(
#         "~~ Rules ~~\n\n"
#         "Guess the word in 6 tries.\n"
#         "Each guess must be a valid 5-letter word.\n"
#         "Hit ENTER to submit your guess.\n"
#         "After each guess, the color of the letters will change\n"
#         "to show how close your guess was to the word.\n\n"
#         f"{Fore.GREEN}GREEN{Fore.RESET} letters are in the correct spot.\n"
#         f"{Fore.YELLOW}YELLOW{Fore.RESET} letters are in the word but in the wrong spot.\n"
#         "WHITE letters are not in the word anywhere.\n"
#         )

#     rules_options = ["Back to Main Menu"]
#     rules_menu_display = TerminalMenu(rules_options)
#     menu_entry_index = rules_menu_display.show()
#     print("Press ENTER to return to the main menu.")

#     if rules_options[menu_entry_index] == "Back to Main Menu":
#         main_menu()

# def display_stats():
#     """Displays statistics from JSON file."""
#     clear_screen()
#     with open("stats.json", "r") as stats:
#         data = json.load(stats)
#         overall_stats = data["Overall Stats"]
#         guess_distribution = data["Guess Distribution"]
#         print(f"~~ {Fore.GREEN}Your {Fore.YELLOW}Stats{Fore.RESET} ~~\n")
#         for key, value in overall_stats.items():
#             print("{:<24} {:<24}".format(Fore.BLUE + key + Fore.RESET, value) + "\n")
#         print("{:<8} {:<8}".format(Fore.GREEN + 'Guesses', Fore.YELLOW + 'Distribution' + Fore.RESET))
#         for key, value in guess_distribution.items():
#             print("{:<8} {:<8}".format(key, value))
#         print("")

#     print("**Statistics are only tracked for games played with default settings**\n")

#     stats_options = ["Back to Main Menu", "Exit to Desktop"]
#     stats_menu_display = TerminalMenu(stats_options)
#     menu_entry_index = stats_menu_display.show()
#     clear_screen()

#     if stats_options[menu_entry_index] == "Back to Main Menu":
#         main_menu()
#     elif stats_options[menu_entry_index] == "Exit to Desktop":
#         quit_messager()

def end_menu():
    """Displays menu upon game end."""
    end_options = ["Play Again", "Exit to Main Menu", "Exit to Desktop"]
    end_menu_display = TerminalMenu(end_options)
    menu_entry_index = end_menu_display.show()
    clear_screen()

    if end_options[menu_entry_index] == "Play Again":
        play_pywordle()
    elif end_options[menu_entry_index] == "Exit to Main Menu":
        main_menu()
    elif end_options[menu_entry_index] == "Exit to Desktop":
        quit_messager()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def quit_messager():
    print(f"Quitting {Fore.GREEN}PY{Fore.YELLOW}WORDLE{Fore.RESET}...\nSee you next time!")

if __name__ == '__main__':
    main_menu()
