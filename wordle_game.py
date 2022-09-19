from wordle_logic import WordleLogic

# Interface between user and game. 

# TODO: Welcome user to game, options for quit, rules, stats, game options
def main():
    print("Welcome to PyWordle...")
    wordle = WordleLogic(secret_word='CRATE')
    while wordle.play_wordle:
        user_guess = input("Enter a 5 letter word.\n").upper()
        if len(user_guess) != wordle.word_length:
            print(f"Your guess must be {wordle.word_length} letters long.\n")
            continue
        
        wordle.validate_user_guess(user_guess)
        wordle.compare_user_guess()
        print("current guess = " + wordle.current_guess) # debug
        print("secret word = " + wordle.secret_word) # debug
        
    
    if wordle.user_wins:
        print("You win!")
    elif wordle.game_over:
        print("Game over!")

        

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
    main()
    
