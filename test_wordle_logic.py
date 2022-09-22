from wordle_logic import WordleLogic, WordLengthError, NotRealWordError
import pytest

def test_validate_user_guess_raises_word_length_exception():
    wordle_test = WordleLogic()
    with pytest.raises(WordLengthError):
        wordle_test.validate_user_guess("red")
    with pytest.raises(WordLengthError):
        wordle_test.validate_user_guess("antidisestablishmentarianism")
    with pytest.raises(WordLengthError):
        wordle_test.validate_user_guess("speedy")

def test_validate_user_guess_raises_not_real_word_exception():
    wordle_test = WordleLogic()
    with pytest.raises(NotRealWordError):
        wordle_test.validate_user_guess("eeeee")
    with pytest.raises(NotRealWordError):
        wordle_test.validate_user_guess("e$-/G")
    with pytest.raises(NotRealWordError):
        wordle_test.validate_user_guess("25000")

def test_validate_user_guess_paper():
    wordle = WordleLogic()
    wordle.validate_user_guess("PAPER")
    assert wordle.current_guess == "PAPER"
    assert wordle.guess_count == 1

def test_validate_user_guess_crate():
    wordle = WordleLogic()
    wordle.guess_count = 1
    wordle.validate_user_guess("CRATE")
    assert wordle.current_guess == "CRATE"
    assert wordle.guess_count == 2

def test_validate_user_guess_place():
    wordle = WordleLogic()
    wordle.guess_count = -2
    wordle.validate_user_guess("PLACE")
    assert wordle.current_guess == "PLACE"
    assert wordle.guess_count == -1
