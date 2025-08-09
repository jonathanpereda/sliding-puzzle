import os;
from .board import Board


def start_game():

    print("--------------------------------")
    print()
    print("Welcome: starting board tests...")
    print()
    print("--------------------------------")
    print()

    print()
    print("Testing 3x3")
    print()

    print("Generating solved board...")
    board = Board(3, False)
    board.display()
    print("Solvability: " + str(board.is_solvable()))
    print("Blank is at: " + str(board.find_blank()))
    print("Legal moves: " + str(board.legal_moves()))
    print("Is solved: " + str(board.is_solved()))
    print("Shuffling...")
    board.shuffle()
    board.display()
    print("Solvability: " + str(board.is_solvable()))
    print("Blank is at: " + str(board.find_blank()))
    print("Legal moves: " + str(board.legal_moves()))
    print("Is solved: " + str(board.is_solved()))
    print()
    print("Generating shuffled board...")
    board2 = Board(3, True)
    board2.display()
    print("Solvability: " + str(board2.is_solvable()))
    print("Blank is at: " + str(board2.find_blank()))
    print("Legal moves: " + str(board2.legal_moves()))
    print("Is solved: " + str(board2.is_solved()))
    print("Tring move U...")
    board2.do_move("U")
    board2.display()
    print("Is solved: " + str(board2.is_solved()))

    print()
    print("Testing 4x4")
    print()

    print("Generating solved board...")
    board3 = Board(4, False)
    board3.display()
    print("Solvability: " + str(board3.is_solvable()))
    print("Blank is at: " + str(board3.find_blank()))
    print("Legal moves: " + str(board3.legal_moves()))
    print("Is solved: " + str(board3.is_solved()))
    print("Shuffling...")
    board3.shuffle()
    board3.display()
    print("Solvability: " + str(board3.is_solvable()))
    print("Blank is at: " + str(board3.find_blank()))
    print("Legal moves: " + str(board3.legal_moves()))
    print("Is solved: " + str(board3.is_solved()))
    print()
    print("Generating shuffled board...")
    board4 = Board(4, True)
    board4.display()
    print("Solvability: " + str(board4.is_solvable()))
    print("Blank is at: " + str(board4.find_blank()))
    print("Legal moves: " + str(board4.legal_moves()))
    print("Is solved: " + str(board4.is_solved()))
    print("Tring move U...")
    board4.do_move("U")
    board4.display()
    print("Is solved: " + str(board4.is_solved()))

    print()
    print("Tests completed!")
    print()

    #''' GAME LOOP

    print("--------------------------------")
    print()
    print("Starting game loop...")
    print()
    print("--------------------------------")
    print()
    print("Wecome!")
    while True:
        grid_size = input(">- Select grid size: [3x3 = 3] [4x4 = 4] -<   ").strip().lower()
        match grid_size:
            case "3":
                game_board = Board(3, start_shuffled=True)
                break
            case "4":
                game_board = Board(4, start_shuffled=True)
                break
            case _:
                print("Not a valid input")
    #game_board = Board(3, start_shuffled=True)
    keymap = {"u":"U","d":"D","l":"L","r":"R"}
    status = "Make a move!"
    while True:
        os.system("cls" if os.name=="nt" else "clear")
        print()
        print(status)
        print()
        game_board.display()
        if game_board.is_solved() is True:
            print("You won!")
            print("Ending game...")
            break
        move = input(">- [Move (u/d/l/r)] [x = reshuffle] [q = quit] -<   ").strip().lower()
        match move:
            case "q":
                print("Ending game...")
                break
            case "x":
                game_board.shuffle()
                status = "Make a move!"
            case "u" | "d" | "l" | "r":
                valid_move = game_board.do_move(keymap.get(move))
                status = "Make a move!"
                if not valid_move:
                    #print("Illegal move. Current legal moves: ", game_board.legal_moves())
                    status = "Illegal move. Current legal moves: " + str(game_board.legal_moves())
            case _:
                status = "Invalid move, try again: "
                #print("Invalid move, try again: ")
                #print()
                
    #'''



