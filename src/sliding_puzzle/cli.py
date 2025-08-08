from .board import Board

def start_game():
    board = Board(3)
    board.display()
    print(board.is_solvable())
    print("Shuffling...")
    board.shuffle()
    board.display()
    print(board.is_solvable())
