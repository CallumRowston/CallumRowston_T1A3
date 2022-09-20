from wordle_logic import WordleLogic, WordLengthError, NotRealWordError
from colorama import Fore
from simple_term_menu import TerminalMenu
# Interface between user and game.

# TODO: Welcome user to game, options for quit, rules, stats, game options
def main_menu():
    print("Welcome to " + Fore.GREEN + "Py" + Fore.YELLOW + "Wordle" + Fore.RESET)
    options = ["Play PyWordle", "Game Settings", "Stats", "Quit"]
    main_menu = TerminalMenu(options)
    menu_entry_index = main_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")
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
    wordle = WordleLogic()
    print(wordle.secret_word) # debug
    while wordle.play_wordle:
        try:
            user_guess = input("Enter a 5 letter word.\n").upper()
            wordle.validate_user_guess(user_guess)
        except WordLengthError as err:
            print(err)
        except NotRealWordError as err:
            print(err)
        else:
            wordle.add_user_guess(user_guess)
            display_colored_guess(wordle.compare_user_guess())
            for _ in range(wordle.total_guesses - len(wordle.guess_history)):
                print("  _  _  _  _  _")

            if wordle.user_wins:
                print("You win!")
                break
            if wordle.user_loses:
                print("You have used all your guesses. Game over!")
                print(f"The correct word was {wordle.secret_word}")
                break
        # print("current guess = " + wordle.current_guess) # debug
        # print("secret word = " + wordle.secret_word) # debug

def game_settings():
    pass

def display_stats():
    pass

colored_results = []
def display_colored_guess(guess):
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
    colored_results.append(colored_guess_str)
    for i in colored_results:
        print(i)
    

# TODO: Display end game win/loss. Play again? Quit? 
def end_menu():
    pass


# TODO: Format game interface to look user friendly
# Spacing
# _ _ _ _ _ to signify a remaining attempt
# Border?

# Gameplay Loop

if __name__ == '__main__':
    main_menu()
    
