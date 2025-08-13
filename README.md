# Online Sudoku Solver and Visualiser

This project implements a Sudoku solver with both greedy (best-first search) and backtracking algorithms, along with web scraping to fetch Sudoku puzzles from the New York Times website. It also provides:

- **Automatic entry** using `pyautogui` to fill puzzles in other applications.
- **Visualization** of solving steps using `pygame`.

## Structure

```
/
├── src/
│   ├── solver.py        # Solver algorithms
│   ├── scraper.py       # Web scraper using requests & BeautifulSoup
│   ├── visualiser.py    # Visualization with pygame
│   └── auto_enter.py    # Auto-entering with pyautogui
├── tests/
│   └── test_solver.py   # Unit tests for solver
├── requirements.txt     # Project dependencies
└── main.py              # Entry point
```

## Installation

```bash
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Usage

```bash
# Solve with backtracking (default), visualize, no auto-enter
python main.py

# Solve with greedy algorithm, no visualization:
python main.py --mode greedy --no-visual

# Solve and auto-enter into active window:
python main.py --auto-enter

# Adjust visualization speed (seconds per cell):
python main.py --delay 0.1

# Load puzzle from file (json or txt):
python main.py --file puzzle.json
```

## Puzzle File Formats
- Plain text: Nine rows of nine space-separated integers
