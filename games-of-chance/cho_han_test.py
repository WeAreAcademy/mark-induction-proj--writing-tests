import cho_han
import utils

def test_find_outcome_even_guessed():
  assert cho_han.find_outcome("Even", 0) is utils.GAME_WIN
  assert cho_han.find_outcome("even", 0) is utils.GAME_WIN
  assert cho_han.find_outcome("Even", 10) is utils.GAME_WIN
  assert cho_han.find_outcome("Even", 1) is utils.GAME_LOSS
  assert cho_han.find_outcome("Even", 7) is utils.GAME_LOSS


def test_find_outcome_odd_guessed():
  assert cho_han.find_outcome("Odd", 0) is utils.GAME_LOSS
  assert cho_han.find_outcome("Odd", 10) is utils.GAME_LOSS
  assert cho_han.find_outcome("Odd", 1) is utils.GAME_WIN
  assert cho_han.find_outcome("odd", 1) is utils.GAME_WIN
  assert cho_han.find_outcome("Odd", 7) is utils.GAME_WIN
