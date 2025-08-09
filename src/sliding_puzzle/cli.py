import os, time
from time import sleep
from .board import Board
from .solver_utils import goal_state
from .solvers.bfs import bfs


def playback_bfs_solution(size: int, delay: float=0.2):
    game_board = Board(3, start_shuffled=True)
    start = game_board.to_state()
    goal = goal_state(size)
    moves, stats = bfs(start, size, goal)

    os.system("cls" if os.name=="nt" else "clear")
    print()
    print("Starting board:")
    print()
    game_board.display()
    time.sleep(delay*10)


    for m in moves:
        os.system("cls" if os.name=="nt" else "clear")
        print()
        print("Running solution. Move: "+m)
        print()
        game_board.display()
        time.sleep(delay)
        game_board.do_move(m)

    os.system("cls" if os.name=="nt" else "clear")
    print()
    print("Final board:")
    print()
    game_board.display()
    print()
    print("Simulation complete")
    print("Solution length:", len(moves))
    print("Stats:", stats)





def start_game():


    playback_bfs_solution(3)



    '''BASIC BFS TEST

    b = Board(3, start_shuffled=True)
    start = b.to_state()
    goal = goal_state(3)
    moves, stats = bfs(start, 3, goal)
    print("Solution length:", len(moves))
    print("Stats:", stats)

    '''


    '''BASIC BOARD TESTS

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

    '''

    ''' GAME LOOP

    print("--------------------------------")
    print()
    print("Starting game loop...")
    print()
    print("--------------------------------")
    print()
    print("Wecome!")

    max_grid_size = 11
    while True:
        size_input = input(">- Select grid size # (e.g. [3x3 = 3], [4x4 = 4]...) -<   ").strip()
        if size_input.isdigit():
            grid_size = int(size_input)
            if grid_size > max_grid_size:
                print("Grid size must be less than "+str(max_grid_size + 1))
            elif grid_size < 2:
                print("Grid size must be at least 2")
            else:
                break
        else:
            print("Invalid input, try again")
    game_board = Board(grid_size, start_shuffled=True)
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
                    status = "Illegal move. Current legal moves: " + str(game_board.legal_moves())
            case _:
                status = "Invalid move, try again: "
                
    #'''



