from simple_term_menu import TerminalMenu
from wordle_logic import WordleLogic, WordLengthError, NotRealWordError
from colorama import Fore
import wordle_rules
import wordle_settings
import wordle_stats
import os

WORD_LENGTH_SETTING = 5
TOTAL_GUESSES_SETTING = 6

# Menus and main game loop
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
