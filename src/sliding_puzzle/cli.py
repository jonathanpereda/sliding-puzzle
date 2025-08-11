import os, time
from time import sleep
from .board import Board
from .solver_utils import goal_state, gen_goal_map
from .solvers.bfs import bfs
from .solvers.astar import astar


def playback_solution(size: int, solver_type="bfs", delay: float=0.15):
    game_board = Board(size, start_shuffled=True)
    start = game_board.to_state()
    os.system("cls" if os.name=="nt" else "clear")
    print("Generating solution...")

    match solver_type:
        case "bfs":
            moves, stats = bfs(start, size)
        case "astar":
            moves, stats = astar(start, size)

    os.system("cls" if os.name=="nt" else "clear")
    print("\nStarting board:\n")
    game_board.display()
    #time.sleep(delay*10)
    while True:
        choice = input("\nPress [Enter] to begin demo: ")
        if choice == "":
            break
        else:
            print("Invalid input")

    for m in moves:
        os.system("cls" if os.name=="nt" else "clear")
        print("\nRunning solution. Move: "+m)
        print()
        game_board.display()
        time.sleep(delay)
        game_board.do_move(m)

    os.system("cls" if os.name=="nt" else "clear")
    print("\nFinal board:\n")
    game_board.display()
    print("\nSimulation complete\n")
    print("Solution length:", len(moves))
    print("Stats:", stats)
    print()


def manual_play():
 
    os.system("cls" if os.name=="nt" else "clear")
    print("Welcome!\n")

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
        print(status)
        print()
        game_board.display()
        if game_board.is_solved() is True:
            print("\nYou won!")
            print("Ending game...\n")
            break
        move = input("\n- [Move (u/d/l/r)] [x = reshuffle] [q = quit] -   >").strip().lower()
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


def test_mode():

    b = Board(3, start_shuffled=True)
    print("BFS")
    print(bfs(b.to_state(),3))
    print("\nA* [3x3]")
    print(astar(b.to_state(),3))
    b2 = Board(4, start_shuffled=True)
    print("\nA* [4x4]")
    print(astar(b2.to_state(),4))

    



def start_game(mode: str = "", size: int = 3):

    match mode:
        case "manual":
            manual_play()
        case "bfs":
            playback_solution(3)
        case _:
            os.system("cls" if os.name=="nt" else "clear")
            while True:
                print("Choose mode: \n1) Manual play\n2) BFS demo (3x3)\n3) A* demo (3x3)\n4) A* demo (4x4)\n9) Quit")
                choice = input(">")
                match choice:
                    case "1":
                        manual_play()
                    case "2":
                        playback_solution(3,"bfs")
                    case "3":
                        playback_solution(3,"astar")
                    case "4":
                        playback_solution(4,"astar")
                    case "9" | "q":
                        break
                    case "t":
                        test_mode()
                    case _:
                        os.system("cls" if os.name=="nt" else "clear")
                        print("Invalid selection. Try again:")
                




