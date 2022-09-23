import wordle_game
from colorama import Fore
from simple_term_menu import TerminalMenu
import json

def display_stats():
    """Displays statistics from JSON file. Provides guess distribution in table format."""
    wordle_game.clear_screen()
    with open("data/stats.json", "r") as stats:
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

    print("**Statistics are only tracked for games played with default settings**\n")

    stats_options = ["Back to Main Menu", "Exit to Desktop"]
    stats_menu_display = TerminalMenu(stats_options)
    menu_entry_index = stats_menu_display.show()
    wordle_game.clear_screen()

    if stats_options[menu_entry_index] == "Back to Main Menu":
        wordle_game.main_menu()
    elif stats_options[menu_entry_index] == "Exit to Desktop":
        wordle_game.quit_messager()
