from wordle_logic import WordleLogic

# Interface between user and game. 

# TODO: Welcome user to game, options for quit, rules, stats, game options
def game_start():
    print("Welcome to PyWordle...")
    wordle = WordleLogic(secret_word='CRATE')
    while wordle.play_wordle:
        wordle.user_guess(input("Enter a 5 letter word.\n"))
        print(wordle.current_guess)
        print(wordle.secret_word)

# TODO: Ask user for guess


# TODO: Dispaly user guess as colored result 
def display_guess():
    pass

# TODO: Display end game win/loss. Play again? Quit? 
def end_menu():
    pass

# TODO: Display stats
def display_stats():
    pass

# TODO: Format game interface to look user friendly
# Spacing
# _ _ _ _ _ to signify a remaining attempt
# Border?

# Gameplay Loop

if __name__ == '__main__':
    game_start()
    
