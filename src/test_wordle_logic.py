from wordle_logic import WordleLogic, WordLengthError, NotRealWordError
import pytest

class TestValidateUserGuess:
    """Tests validate_user_guess method from WordleLogic class"""
    def test_raises_word_length_exception(self):
        wordle = WordleLogic()
        with pytest.raises(WordLengthError):
            wordle.validate_user_guess("A")
        with pytest.raises(WordLengthError):
            wordle.validate_user_guess("red")
        with pytest.raises(WordLengthError):
            wordle.validate_user_guess("antidisestablishmentarianism")
        with pytest.raises(WordLengthError):
            wordle.validate_user_guess("speedy")

    def test_raises_not_real_word_exception(self):
        wordle = WordleLogic()
        with pytest.raises(NotRealWordError):
            wordle.validate_user_guess("eeeee")
        with pytest.raises(NotRealWordError):
            wordle.validate_user_guess("pytho")
        with pytest.raises(NotRealWordError):
            wordle.validate_user_guess("e$-/G")
        with pytest.raises(NotRealWordError):
            wordle.validate_user_guess("25000")

    def test_validate_user_guess_paper(self):
        wordle = WordleLogic()
        wordle.validate_user_guess("PAPER")
        assert wordle.current_guess == "PAPER"
        assert wordle.guess_count == 1

    def test_validate_user_guess_crate(self):
        wordle = WordleLogic()
        wordle.guess_count = 1
        wordle.validate_user_guess("CRATE")
        assert wordle.current_guess == "CRATE"
        assert wordle.guess_count == 2

    def test_validate_user_guess_place(self):
        wordle = WordleLogic()
        wordle.guess_count = -1
        wordle.validate_user_guess("PLACE")
        assert wordle.current_guess == "PLACE"
        assert wordle.guess_count == 0

    def test_validate_user_guess_rhyme(self):
        wordle = WordleLogic()
        wordle.guess_count = 999
        wordle.validate_user_guess("RHYME")
        assert wordle.current_guess == "RHYME"
        assert wordle.guess_count == 1000


class TestCompareUserGuess:
    """Tests compare_user_guess method from WordleLogic class"""
    def test_compare_user_guess_none_correct(self):
        wordle = WordleLogic()
        wordle.secret_word = "CLOUD"
        wordle.current_guess = "RHYME"
        assert wordle.compare_user_guess() == ['R', 'H', 'Y', 'M', 'E']
    
    def test_compare_user_guess_all_correct(self):
        wordle = WordleLogic()
        wordle.secret_word = "CRATE"
        wordle.current_guess = "CRATE"
        assert wordle.compare_user_guess() == ['Cgreen', 'Rgreen', 'Agreen', 'Tgreen', 'Egreen']

    def test_compare_user_guess_print(self):
        wordle = WordleLogic()
        wordle.secret_word = "PAPER"
        wordle.current_guess = "PRINT"
        assert wordle.compare_user_guess() == ['Pgreen', 'Ryellow', 'I', 'N', 'T']

    def test_compare_user_guess_paper(self):
        wordle = WordleLogic()
        wordle.secret_word = "PRINT"
        wordle.current_guess = "PAPER"
        assert wordle.compare_user_guess() == ['Pgreen', 'A', 'P', 'E', 'Ryellow']
        assert wordle.compare_user_guess() != ['Pgreen', 'A', 'Pyellow', 'E', 'Ryellow']
