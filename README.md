# Sliding Puzzle Solver

## Overview
A Python-based sliding puzzle solver supporting configurable board sizes, manual play, and automated solving with BFS (Breadth-First Search). Includes benchmarking tools that log solver performance to CSV and generate Markdown summary tables.

## Features
- Supports any n×n board size
- Solvability checks for both odd and even board sizes  
- Manual play mode with `u/d/l/r` controls and reshuffle with `x` 
- BFS solver for 3×3 with path reconstruction and animated terminal playback  
- Benchmarking scripts to produce CSV data and Markdown summaries  
- Unit tests for board logic and BFS solver

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

## Benchmark Results (BFS 3×3)
The latest BFS benchmark summary is in [`docs/bfs_summary_<date>.md`](docs/bfs_summary_2025-08-10.md).

## Tests
Run all tests with:
```bash
pytest -q
```
Unit tests cover Board methods and BFS solver path reconstruction.

## Roadmap
- A* solver with Manhattan distance heuristic (3×3)  
- IDA* solver (4×4)  
- Pattern Database heuristic (maybe)  
- Combined benchmark tables for all solvers

## Version History
- **v1.0.0** — First solver release: BFS solver with CLI playback and benchmarking tools  
- v0.2 - Playable version with manual moves and terminal display
- v0.1 - Foundation: board generation, display, solvability check, shuffle with safeguards

## License
MIT License

## Author
**Jonathan Pereda**
[GitHub](https://github.com/jonathanpereda)