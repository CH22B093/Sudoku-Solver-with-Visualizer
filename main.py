from src.solver import SudokuSolver
from src.scraper import fetch_nyt_sudoku
from src.visualiser import Visualiser
from src.auto_enter import auto_fill
import argparse
import os
import json


def main():
    parser = argparse.ArgumentParser(description='Sudoku solver and visualizer')
    parser.add_argument('--mode',choices=['backtracking','greedy'],default='backtracking',help='Solve mode: backtracking (default) or greedy')
    parser.add_argument('-f','--file',help='Path to a puzzle file (TXT 9x9 grid or JSON list of lists)')
    parser.add_argument('--no-visual',action='store_true',help='Skip visualization step')
    parser.add_argument('--auto-enter',action='store_true',help='Perform automatic entry via pyautogui')
    parser.add_argument('--delay',type=float,default=0.05,help='Delay between visualization steps')
    args = parser.parse_args()
    if args.file:
        path = args.file
        if not os.path.exists(path):
            print(f"Puzzle file not found: {path}")
            return
        ext = os.path.splitext(path)[1].lower()
        if ext == '.json':
            with open(path) as f:
                board = json.load(f)
        else:
            with open(path) as f:
                board = [list(map(int, line.split())) for line in f]
    else:
        board = fetch_nyt_sudoku()

    print("Initial board:")
    for row in board:
        print(row)

    # Solving puzzle
    solver = SudokuSolver(board)
    if args.mode == 'greedy':
        solved = solver.solve_greedy()
    else:
        solved = solver.solve_backtracking()

    print("Solved board:")
    for row in solved:
        print(row)

    # Visualise if enabled
    if not args.no_visual:
        vis = Visualiser(board,solved,delay=args.delay)
        vis.run()
        
    if args.auto_enter:
        auto_fill(solved)


if __name__ == '__main__':
    main()
