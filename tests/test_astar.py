import pytest
from sliding_puzzle.solver_utils import goal_state
from sliding_puzzle.solvers.astar import astar
from sliding_puzzle.solvers.bfs import bfs


@pytest.mark.parametrize(
    "state,size,expected_len",
    [
        ((1,2,3,4,5,6,7,8,0), 3, 0),
        ((1,2,3,4,5,6,7,0,8), 3, 1),
        ((1,2,3,4,5,6,0,7,8), 3, 2),

        ((1,2,3,4,5,6,7,8,9,10,11,12,13,14,0,15), 4, 1),
    ],
)
def test_astar_expected_lengths(state, size, expected_len):
    goal = goal_state(size)
    path, stats = astar(state, size, goal)
    assert isinstance(path, list)
    assert isinstance(stats, dict)
    assert len(path) == expected_len


@pytest.mark.parametrize(
    "state,size",
    [
        ((1,2,3,4,5,6,7,0,8), 3),
        ((1,2,3,4,5,6,0,7,8), 3),
    ],
)
def test_astar_matches_bfs_length(state, size):
    goal = goal_state(size)
    a_path, _ = astar(state, size, goal)
    b_path, _ = bfs(state, size, goal)
    assert len(a_path) == len(b_path)
