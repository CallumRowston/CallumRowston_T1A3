from wordle_logic import WordleLogic, WordLengthError, NotRealWordError

def fake_input():
    return "CRATE"

class TestValidateUserGuess:
    def test_valid(self, monkeypatch):
        wordle_instance = WordleLogic()
        monkeypatch.setattr('builtins.input', fake_input)
        assert wordle_instance.validate_user_guess(fake_input) == None
        # assert wordle_instance.validate_user_guess("eee") == WordLengthError(f"Your guess must be {self.word_length} letters long.\n")
        # assert wordle_instance.validate_user_guess("eeeee") == NotRealWordError(f"{user_guess} is not a valid word. Guess again.")
