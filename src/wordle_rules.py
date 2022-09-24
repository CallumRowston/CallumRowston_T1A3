from wordle_game import clear_screen, main_menu
from colorama import Fore
from simple_term_menu import TerminalMenu

def display_rules():
    """Displays the rules for the game"""
    clear_screen()
    print(
        f"\n  ~~ {Fore.GREEN}Rules{Fore.RESET} ~~\n\n"
        "  Guess the word in 6 tries.\n"
        "  Each guess must be a valid 5-letter word.\n"
        "  Hit ENTER to submit your guess.\n"
        "  After each guess, the color of the letters will change\n"
        "  to show how close your guess was to the word.\n\n"
        f"  {Fore.GREEN}GREEN{Fore.RESET} letters are in the correct spot.\n"
        f"  {Fore.YELLOW}YELLOW{Fore.RESET} letters are in the word but in the wrong spot.\n"
        "  WHITE letters are not in the word anywhere.\n"
        )

    rules_options = ["Back to Main Menu"]
    rules_menu_display = TerminalMenu(rules_options)
    menu_entry_index = rules_menu_display.show()
    print("  Press ENTER to return to the main menu.")

    if rules_options[menu_entry_index] == "Back to Main Menu":
        main_menu()
