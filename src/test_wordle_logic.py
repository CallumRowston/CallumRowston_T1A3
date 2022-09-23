import pytest
from wordle_logic import WordleLogic, WordLengthError, NotRealWordError

class TestValidateUserGuess:
    """Tests validate_user_guess method from WordleLogic class"""
    def test_raises_word_length_exception(self):
        """Tests that WordLengthError exception is raised when the length
            of the users guess does not equal the secret word length
        """
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
        """Tests that NotRealWordError exception is raised when the user
            gues is a valid length but not a word in the secret word list
        """
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
        """Tests that when a valid word is passed to validate_user_guess that 
            the current_guess is set to the valid word and the gueess_count
            is incremented by 1.
        """
        wordle = WordleLogic()
        wordle.validate_user_guess("PAPER")
        assert wordle.current_guess == "PAPER"
        assert wordle.guess_count == 1

    def test_validate_user_guess_crate(self):
        """Tests that when a valid word is passed to validate_user_guess that 
            the current_guess is set to the valid word and the gueess_count
            is incremented by 1.
        """
        wordle = WordleLogic()
        wordle.guess_count = 1
        wordle.validate_user_guess("CRATE")
        assert wordle.current_guess == "CRATE"
        assert wordle.guess_count == 2

    def test_validate_user_guess_place(self):
        """Tests that when a valid word is passed to validate_user_guess that 
            the current_guess is set to the valid word and the gueess_count
            is incremented by 1.
        """
        wordle = WordleLogic()
        wordle.guess_count = -1
        wordle.validate_user_guess("PLACE")
        assert wordle.current_guess == "PLACE"
        assert wordle.guess_count == 0

    def test_validate_user_guess_rhyme(self):
        """Tests that when a valid word is passed to validate_user_guess that 
            the current_guess is set to the valid word and the gueess_count
            is incremented by 1.
        """
        wordle = WordleLogic()
        wordle.guess_count = 999
        wordle.validate_user_guess("RHYME")
        assert wordle.current_guess == "RHYME"
        assert wordle.guess_count == 1000


class TestCompareUserGuess:
    """Tests compare_user_guess method from WordleLogic class"""
    def test_compare_user_guess_none_correct(self):
        """Tests when the user guesses zero letters correctly, no letters in
            the guess are marked.
        """
        wordle = WordleLogic()
        wordle.secret_word = "CLOUD"
        wordle.current_guess = "RHYME"
        assert wordle.compare_user_guess() == ['R', 'H', 'Y', 'M', 'E']
    
    def test_compare_user_guess_all_correct(self):
        """Tests when the user guesses all letters correctly, all letters in
            the guess are marked for correctedness.
        """
        wordle = WordleLogic()
        wordle.secret_word = "CRATE"
        wordle.current_guess = "CRATE"
        assert wordle.compare_user_guess() == ['Cgreen', 'Rgreen', 'Agreen', 'Tgreen', 'Egreen']

    def test_compare_user_guess_print(self):
        """Tests when the user guesses some letters correctly, only those letters
            are marked and that they are marked with the correct marker.
        """
        wordle = WordleLogic()
        wordle.secret_word = "PAPER"
        wordle.current_guess = "PRINT"
        assert wordle.compare_user_guess() == ['Pgreen', 'Ryellow', 'I', 'N', 'T']

    def test_compare_user_guess_paper(self):
        """Tests when the user guesses a word with 2 of the ssame letter and the secret word contains
            only 1 of those letters, that the second occurrence is not marked as correct and the
            first occurrence is marked correct.
        """
        wordle = WordleLogic()
        wordle.secret_word = "PRINT"
        wordle.current_guess = "PAPER"
        assert wordle.compare_user_guess() == ['Pgreen', 'A', 'P', 'E', 'Ryellow']
        assert wordle.compare_user_guess() != ['Pgreen', 'A', 'Pyellow', 'E', 'Ryellow']
