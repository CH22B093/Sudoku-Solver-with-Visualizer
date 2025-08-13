class SudokuSolver:
    def __init__(self, board):
        self.board = board

    def solve_greedy(self):
        board = [row[:] for row in self.board]
        def find_empty(b):
            for i in range(9):
                for j in range(9):
                    if b[i][j] == 0:
                        return i,j
            return None
        def valid(b,num,pos):
            r,c = pos
            if any(b[r][j] == num for j in range(9)): return False
            if any(b[i][c] == num for i in range(9)): return False
            br,bc = (r//3)*3,(c//3)*3
            for i in range(br,br+3):
                for j in range(bc,bc+3):
                    if b[i][j] == num: return False
            return True
        progress = True
        while progress:
            progress = False
            for i in range(9):
                for j in range(9):
                    if board[i][j] == 0:
                        candidates = [n for n in range(1,10) if valid(board,n,(i,j))]
                        if len(candidates) == 1:
                            board[i][j] = candidates[0]
                            progress = True
        solver = SudokuSolver(board)
        return solver.solve_backtracking()

    def solve_backtracking(self):
        board = [row[:] for row in self.board]
        def find_empty(b):
            for i in range(9):
                for j in range(9):
                    if b[i][j] == 0:
                        return i,j
            return None
        def valid(b,num,pos):
            r,c = pos
            if any(b[r][j] == num for j in range(9)): return False
            if any(b[i][c] == num for i in range(9)): return False
            br,bc = (r//3)*3,(c//3)*3
            for i in range(br,br+3):
                for j in range(bc,bc+3):
                    if b[i][j] == num: return False
            return True
        def backtrack(b):
            loc = find_empty(b)
            if not loc:
                return True
            i,j = loc
            for num in range(1,10):
                if valid(b, num, (i,j)):
                    b[i][j] = num
                    if backtrack(b):
                        return True
                    b[i][j] = 0
            return False
        if backtrack(board):
            return board
        else:
            raise ValueError("No solution exists")
