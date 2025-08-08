from .board import Board

def start_game():
    board = Board(3)
    board.display()
    #flat = [4, 6, 8, 3, 1, 2, 7, 5]
    print(board.is_solvable())
