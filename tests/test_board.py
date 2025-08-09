import pytest
from sliding_puzzle.board import Board

def test_find_blank_solved_3x3():
    b = Board(3)
    assert b.find_blank() == (2,2)

def test_legal_moves_solved_3x3():
    b = Board(3)
    assert set(b.legal_moves()) == {"D", "R"}

def test_do_move_and_is_solved():
    b = Board(3)
    move = b.do_move("R")
    assert move is True
    assert b.is_solved() is False
    move = b.do_move("L")
    assert move is True
    assert b.is_solved() is True