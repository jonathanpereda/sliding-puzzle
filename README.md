# Sliding Puzzle Solver

## Overview
A Python-based sliding puzzle solver supporting configurable board sizes, manual play, and automated solving with BFS (Breadth-First Search) and A* (Manhattan). Includes benchmarking tools that log solver performance to CSV and generate Markdown summary tables.

## Features
- Supports any n×n board size
- Solvability checks for both odd and even board sizes  
- Manual play mode with `u/d/l/r` controls and reshuffle with `x` 
- BFS solver for 3×3 with path reconstruction  
- Benchmarking scripts to produce CSV data and Markdown summaries  
- Unit tests for board logic and BFS solver
- A* (Manhattan) solver for 3×3 and 4×4 with optimal path reconstruction
- Animated terminal playback: run bfs or astar_manhattan in the same demo
- Benchmarking scripts for A* (3×3 and 4×4) with CSV outputs and summary tables
- Unit tests for A* path length and parity with BFS on small cases

## Results at a Glance

**3×3 — BFS vs A\***  
A* finds the same optimal paths but with far fewer expansions.

| Depth | Avg States (BFS) | Avg States (A\*) | Speedup (≈) |
|------:|------------------:|------------------:|------------:|
| 0     | 0                 | 0                 | —           |
| 30    | 74,540            | 550               | 136× fewer  |
| 60    | 66,760            | 387               | 173× fewer  |

> Full tables: [BFS 3×3](docs/bfs[3x3]_summary_<date>.md) · [A\* 3×3](docs/astar[3x3]_summary_<date>.md)

**4×4 — A\* (Manhattan)**

| Depth | Avg States (A\*) | Avg Time (ms) |
|------:|------------------:|--------------:|
| 0     | 0                 | 0.000         |
| 30    | 2,140             | 12.849        |
| 60    | 221,565           | 1,659.342     |

> Full table: [A\* 4×4](docs/astar[4x4]_summary_<date>.md)

## How to Run

**Manual Play**
```bash
python main.py
# Choose "1" at the prompt
```

**BFS Demo**
```bash
python main.py
# Choose "2" at the prompt
```

**A\* Demo**
```bash
python main.py
# Choose "3" for 3×3 or "4" for 4×4 at the prompt
```

## Benchmarking BFS
Run the benchmark and generate the summary:
```bash
python scripts/benchmark_bfs.py
python scripts/generate_summary.py
```
The summary table will be written to:
```
docs/bfs_summary_<date>.md
```

## Benchmarking A*
Run the benchmark and generate the summary:
```bash
python scripts/benchmark_astar.py
python scripts/generate_summary.py
```
The summary table will be written to:
```
docs/astar[n×n]_summary_<date>.md
```

## Benchmark Results (BFS 3×3)
- BFS 3×3 results: see [`docs/bfs[3x3]_summary_<date>.md`](docs/bfs[3x3]_summary_2025-08-11.md).
- A* 3×3 results: see [`docs/astar[3x3]_summary_<date>.md`](docs/astar[3x3]_summary_2025-08-11.md).
- A* 4×4 results: see [`docs/astar[4x4]_summary_<date>.md`](docs/astar[4x4]_summary_2025-08-11.md).

## Tests
Run all tests with:
```bash
pytest -q
```
Unit tests cover Board methods, BFS path reconstruction, and A* (expected lengths on trivials and parity with BFS on small solvable cases).

## Roadmap
- ~~A* solver with Manhattan distance heuristic (3×3)~~ - Done: v1.1.0
- IDA* solver (4×4)  
- Linear Conflict heuristic (A*), then Pattern Database (PDB)  
- Combined benchmark tables for all solvers

## Version History
- **v1.1.0** - A* (Manhattan) solver, unified playback, A* 3×3 & 4×4 benchmarks
- v1.0.0 — First solver release: BFS solver with CLI playback and benchmarking tools  
- v0.2 - Playable version with manual moves and terminal display
- v0.1 - Foundation: board generation, display, solvability check, shuffle with safeguards

## License
MIT License

## Author
**Jonathan Pereda**
[GitHub](https://github.com/jonathanpereda)