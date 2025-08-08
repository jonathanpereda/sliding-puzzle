import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "src"))
from src.sliding_puzzle.cli import start_game

def main():
    start_game()

if __name__ == "__main__":
    main()
