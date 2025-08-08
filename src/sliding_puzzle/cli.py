from .board import Board

def start_game():
    print("Generating solved board...")
    board = Board(3, False)
    board.display()
    print("Solvability: " + str(board.is_solvable()))
    print("Shuffling...")
    board.shuffle()
    board.display()
    print("Solvability: " + str(board.is_solvable()))
    print()
    print("Generating shuffled board...")
    board2 = Board(3, True)
    board2.display()
    print("Solvability: " + str(board.is_solvable()))
