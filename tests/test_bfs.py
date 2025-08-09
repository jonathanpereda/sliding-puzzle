from sliding_puzzle.solver_utils import goal_state, get_neighbors
from sliding_puzzle.solvers.bfs import bfs
from sliding_puzzle.board import Board

def apply_moves_to_board(b: Board, moves):
    for m in moves:
        assert b.do_move(m), f"Move {m} should be legal"

def test_bfs_on_small_scramble():

    b = Board(3)  #start solved
    for m in ["R","D","L"]:
        b.do_move(m)

    start = b.to_state()
    goal = goal_state(3)
    moves, stats = bfs(start, 3, goal)
    #replay solution
    b2 = Board(3, start_shuffled=False)

    tiles = [[None if x==0 else x for x in start[i:i+3]] for i in range(0, 9, 3)]
    b2.tiles = tiles
    apply_moves_to_board(b2, moves)
    assert b2.to_state() == goal
