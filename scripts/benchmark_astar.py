import sys, random, tracemalloc
from pathlib import Path
import csv
from datetime import datetime

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.sliding_puzzle.solver_utils import get_neighbors, goal_state
from src.sliding_puzzle.solvers.astar import astar 



DEFAULT_BUCKETS = [0,5,10,15,20,25,30,35,40,45,50,55,60]
DEFAULT_TRIALS = 30
DEFAULT_BASE_SEED = 1337
SOLVER_NAME = "astar_manhattan"

#Clear file before writing
RESET_CSV = True

DATA_DIR = Path("data")
DOCS_DIR = Path("docs")

CSV_FIELDS = [
    "timestamp",
    "board_size",
    "bucket_depth_n",
    "trial",
    "time_sec",
    "states_expanded",
    "peak_memory_use",
    "solution_length",
    "solver",
    "seed"
]


def ensure_csv_with_header(csv_path, headers):
    #Create data dir if needed
    csv_path.parent.mkdir(parents = True, exist_ok = True)

    needs_header = (not csv_path.exists()) or (csv_path.stat().st_size == 0)

    if needs_header:
        with csv_path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(headers)

def append_csv_row(csv_path, row_dict):
    with csv_path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        writer.writerow(row_dict)

def run_one_trial(size, depth, trial, base_seed):
    
    goal = goal_state(size)
    trial_seed = base_seed + depth * 1000 + trial
    rng = random.Random(trial_seed)
    tracemalloc.start()

    start = do_scramble(goal, depth, size, rng)

    moves, stats = astar(start, size, goal)
    #if solver fails return none
    if not isinstance(moves, list):
        return None
    
    current, peak = tracemalloc.get_traced_memory()
    peak_kb = peak / 1024
    tracemalloc.stop()

    #map stats to csv
    time_sec = stats["time_ms"] / 1000.0
    states_expanded = stats["nodes_expanded"]
    solution_length = stats["depth"]



    row = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "board_size": size,
        "bucket_depth_n": depth,
        "trial": trial,
        "time_sec": time_sec,
        "states_expanded": states_expanded,
        "peak_memory_use": peak_kb,
        "solution_length": solution_length,
        "solver": SOLVER_NAME,
        "seed": trial_seed,
    }
    return row


def do_scramble(goal_tuple, depth, size, rng):
    state = goal_tuple
    prev = None 
    for _ in range(depth):
        candidates = get_neighbors(state, size)
        if prev is not None:
            filtered = [pair for pair in candidates if pair[0] != prev]     #filter out backtracks
            if not filtered:  #if theres no other option than a backtrack
                filtered = candidates
        else:
            filtered = candidates
        next_state, _move = rng.choice(filtered)
        prev, state = state, next_state
    return state
            


if __name__ == "__main__":
    csv_path = DATA_DIR / "astar_runs[4x4].csv"

    #Clear file before writing
    if RESET_CSV and csv_path.exists():
        csv_path.unlink()

    ensure_csv_with_header(csv_path, CSV_FIELDS)

    size = 4
    for depth in DEFAULT_BUCKETS:
        for trial in range(1, DEFAULT_TRIALS + 1):
            row = run_one_trial(size=size, depth=depth, trial=trial, base_seed=DEFAULT_BASE_SEED)
            if row is None:
                #print("SIM FAILED")
                continue
            append_csv_row(csv_path, row)




