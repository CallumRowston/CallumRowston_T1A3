import os
from simple_term_menu import TerminalMenu
# from wordle_game import main_menu, WORD_LENGTH_SETTING, TOTAL_GUESSES_SETTING
import wordle_game
from wordle_logic import WordleLogic

def game_settings_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(
        "~~ Current Settings ~~\n\n"
        "**WARNING! Statistics are only tracked for games played with default settings**\n\n"
        f"Word Length: {wordle_game.WORD_LENGTH_SETTING}\n"
        f"Attempts: {wordle_game.TOTAL_GUESSES_SETTING}\n"
        )
    setting_options = ["Set word length", "Set total guesses", "Reset To Default Settings", "Back to Main Menu"]
    setting_menu_display = TerminalMenu(setting_options)
    menu_entry_index = setting_menu_display.show()
    if setting_options[menu_entry_index] == "Set word length":
        set_word_length()
    elif setting_options[menu_entry_index] == "Set total guesses":
        set_total_guesses()
    elif setting_options[menu_entry_index] == "Reset To Default Settings":
        wordle_game.WORD_LENGTH_SETTING = 5
        wordle_game.TOTAL_GUESSES_SETTING = 6
        game_settings_menu()
    elif setting_options[menu_entry_index] == "Back to Main Menu":
        wordle_game.main_menu()

def set_word_length():
    os.system('cls' if os.name == 'nt' else 'clear')
    length_options = ["5 - Default", "6", "7", "8"]
    length_menu_display = TerminalMenu(length_options)
    menu_entry_index = length_menu_display.show()
    if length_options[menu_entry_index] == "5 - Default":
        wordle_game.WORD_LENGTH_SETTING = 5
    elif length_options[menu_entry_index] == "6":
        wordle_game.WORD_LENGTH_SETTING = 6
    elif length_options[menu_entry_index] == "7":
        wordle_game.WORD_LENGTH_SETTING = 7
    elif length_options[menu_entry_index] == "8":
        wordle_game.WORD_LENGTH_SETTING = 8
    game_settings_menu()

def set_total_guesses():
    os.system('cls' if os.name == 'nt' else 'clear')
    attempt_options = ["6 - Default", "7", "8", "9"]
    attempt_menu_display = TerminalMenu(attempt_options)
    menu_entry_index = attempt_menu_display.show()
    if attempt_options[menu_entry_index] == "6 - Default":
        wordle_game.TOTAL_GUESSES_SETTING = 6
    elif attempt_options[menu_entry_index] == "7":
        wordle_game.TOTAL_GUESSES_SETTING = 7
    elif attempt_options[menu_entry_index] == "8":
        wordle_game.TOTAL_GUESSES_SETTING = 8
    elif attempt_options[menu_entry_index] == "9":
        wordle_game.TOTAL_GUESSES_SETTING = 9
    game_settings_menu()