from simple_term_menu import TerminalMenu
import wordle_game

def game_settings_menu():
    wordle_game.clear_screen()
    print(
        "~~ Current Settings ~~\n\n"
        f"Word Length: {wordle_game.WORD_LENGTH_SETTING}\n"
        f"Attempts: {wordle_game.TOTAL_GUESSES_SETTING}\n\n"
        "**WARNING! Statistics are only tracked for\ngames played with default settings**\n"
        )
    setting_options = ["Set Word Length", "Set Max Guesses", "Reset To Default Settings", "Back To Main Menu"]
    setting_menu_display = TerminalMenu(setting_options)
    menu_entry_index = setting_menu_display.show()

    if setting_options[menu_entry_index] == "Set Word Length":
        wordle_game.clear_screen()
        wordle_game.WORD_LENGTH_SETTING = settings_user_input('word length', 5, 9)
        game_settings_menu()
    elif setting_options[menu_entry_index] == "Set Max Guesses":
        wordle_game.clear_screen()
        wordle_game.TOTAL_GUESSES_SETTING = settings_user_input('max guesses', 6, 10)
        game_settings_menu()
    elif setting_options[menu_entry_index] == "Reset To Default Settings":
        wordle_game.WORD_LENGTH_SETTING = 5
        wordle_game.TOTAL_GUESSES_SETTING = 6
        game_settings_menu()
    elif setting_options[menu_entry_index] == "Back To Main Menu":
        wordle_game.main_menu()

def settings_user_input(setting_description, start_range, end_range):
    print(
        f"Enter a number {start_range} - {end_range - 1} to set the games {setting_description} to that number.\n"
        f"{start_range} is the default {setting_description}.\n"
        "Type 'back' to cancel making any changes.\n"
        )
    user_setting = ''
    while user_setting != 'back':
        try:
            user_setting = input()
            if user_setting == 'back':
                game_settings_menu()
            user_setting = int(user_setting)
        except ValueError:
            print("That doesn't look like a real setting. Try again or type 'back' to exit.")
        else:
            try:
                if user_setting not in range(start_range, end_range):
                    raise RangeError(f"Oops! You can only enter {start_range}, {start_range + 1}, {start_range + 2} or {start_range + 3}. Type 'back' to exit.")
            except RangeError as err:
                print(err)
            else:
                return user_setting

class RangeError(Exception):
    pass
