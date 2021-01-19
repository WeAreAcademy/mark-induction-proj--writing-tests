import coin_flip
import utils

def test_find_outcome_win_on_two_heads():
  assert coin_flip.find_outcome("H", "H") is utils.GAME_WIN
  assert coin_flip.find_outcome("H", "h") is utils.GAME_WIN
  assert coin_flip.find_outcome("heads", "H") is utils.GAME_WIN
  assert coin_flip.find_outcome("Heads", "heads") is utils.GAME_WIN

def test_find_outcome_win_on_two_tails():
  assert coin_flip.find_outcome("T", "T") is utils.GAME_WIN
  assert coin_flip.find_outcome("T", "t") is utils.GAME_WIN
  assert coin_flip.find_outcome("tails", "T") is utils.GAME_WIN
  assert coin_flip.find_outcome("Tails", "tails") is utils.GAME_WIN

def test_find_outcome_lose_on_mismatch_pair():
  assert coin_flip.find_outcome("H", "T") is utils.GAME_LOSS
  assert coin_flip.find_outcome("T", "h") is utils.GAME_LOSS
  assert coin_flip.find_outcome("heads", "T") is utils.GAME_LOSS
  assert coin_flip.find_outcome("Tails", "heads") is utils.GAME_LOSS