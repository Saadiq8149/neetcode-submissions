from typing import List
import copy

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        board = [["."] * n for _ in range(n)]

        def helper(board, row):
            if row == n:
                cleaned = []
                for r in board:
                    cleaned.append("".join("." if c == "x" else c for c in r))
                results.append(cleaned)
                return

            for c in range(n):
                if board[row][c] != ".":
                    continue

                new_board = copy.deepcopy(board)
                new_board[row][c] = "Q"

                for i in range(n):
                    if new_board[row][i] == ".":
                        new_board[row][i] = "x"
                    if new_board[i][c] == ".":
                        new_board[i][c] = "x"

                for dr, dc in [(-1,-1), (-1,1), (1,-1), (1,1)]:
                    i, j = row + dr, c + dc
                    while 0 <= i < n and 0 <= j < n:
                        if new_board[i][j] == ".":
                            new_board[i][j] = "x"
                        i += dr
                        j += dc

                helper(new_board, row + 1)

        helper(board, 0)
        return results
