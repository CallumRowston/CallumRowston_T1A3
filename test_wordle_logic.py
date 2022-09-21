from wordle_logic import WordleLogic, WordLengthError, NotRealWordError
import pytest

wordle_test = WordleLogic()

def test_validate_user_guess_raises_word_length_exception():
    with pytest.raises(WordLengthError):
        wordle_test.validate_user_guess("red")
    with pytest.raises(WordLengthError):
        wordle_test.validate_user_guess("antidisestablishmentarianism")
    with pytest.raises(WordLengthError):
        wordle_test.validate_user_guess("speedy")

def test_validate_user_guess_raises_not_real_word_exception():
    with pytest.raises(NotRealWordError):
        wordle_test.validate_user_guess("eeeee")
    with pytest.raises(NotRealWordError):
        wordle_test.validate_user_guess("e$-/G")
    with pytest.raises(NotRealWordError):
        wordle_test.validate_user_guess("25000")

