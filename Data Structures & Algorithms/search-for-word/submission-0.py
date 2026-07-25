class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.exists = False
        rows, cols = len(board), len(board[0])

        def helper(r, c, idx):
            if self.exists:
                return

            if idx == len(word):
                self.exists = True
                return

            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != word[idx]
            ):
                return

            temp = board[r][c]
            board[r][c] = "#"

            helper(r - 1, c, idx + 1)  # top
            helper(r, c + 1, idx + 1)  # right
            helper(r + 1, c, idx + 1)  # bottom
            helper(r, c - 1, idx + 1)  # left

            board[r][c] = temp

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    helper(r, c, 0)
                    if self.exists:
                        return True

        return False
