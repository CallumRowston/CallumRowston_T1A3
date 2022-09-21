from wordle_logic import WordleLogic, WordLengthError, NotRealWordError
from colorama import Fore
from simple_term_menu import TerminalMenu
import os
import json

# Main game loop and Menus

def main_menu():
    """
    Main menu to navigate to the main game, rules, stats or quit.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to " + Fore.GREEN + "PY" + Fore.YELLOW + "WORDLE" + Fore.RESET + "\nUse up and down arrow keys to navigate menu.\nPress ENTER to select an option.\n")
    options = ["Play PyWordle", "Rules", "Stats", "Quit"]
    main_menu = TerminalMenu(options)
    menu_entry_index = main_menu.show()
    if options[menu_entry_index] == "Play PyWordle":
        play_pywordle()
    elif options[menu_entry_index] == "Rules":
        rules()
    elif options[menu_entry_index] == "Stats":
        display_stats()
    elif options[menu_entry_index] == "Quit":
        print("Quitting application...")

def play_pywordle():
    """
    Main gameplay loop. Calls methods from WordleLogic class.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    wordle = WordleLogic()  
    print(wordle.secret_word) # debug
    while wordle.play_wordle:
        try:
            # user_guess = input("Enter a 5 letter word: ").upper()
            wordle.validate_user_guess()
        except (WordLengthError, NotRealWordError) as err:
            print(err)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            # wordle.add_user_guess(user_guess)
            wordle.display_colored_guess(wordle.compare_user_guess())
            for _ in range(wordle.total_guesses - wordle.guess_count):
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

def rules():
    """
    Prints the rules for the game.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print("~~ Rules ~~\n")
    print("Guess the word in 6 tries.")
    print("Each guess must be a valid 5-letter word.")
    print("Hit ENTER to submit your guess.")
    print("After each guess, the color of the letters will change\nto show how close your guess was to the word.\n")
    print(f"{Fore.GREEN}GREEN{Fore.RESET} letters are in the correct spot.")
    print(f"{Fore.YELLOW}YELLOW{Fore.RESET} letters are in the word but in the wrong spot.")
    print("WHITE letters are not in the word anywhere.\n")
    
    rules_options = ["Back to Main Menu"]
    rules_menu_display = TerminalMenu(rules_options)
    menu_entry_index = rules_menu_display.show()
    print("Press ENTER to return to the main menu.")
    if rules_options[menu_entry_index] == "Back to Main Menu":
        main_menu()

def display_stats():
    """
    Displays statistics from JSON file.
    """
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
            print("Quitting application...")

def end_menu():
    """
    Displays menu upon game end.
    """
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

if __name__ == '__main__':
    main_menu()
