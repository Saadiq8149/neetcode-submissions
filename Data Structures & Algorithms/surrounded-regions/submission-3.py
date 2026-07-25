class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, region):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in visited or board[r][c] == "X":
                return 0

            visited.add((r, c))
            region.append((r, c))     

            border = 0
            if r == 0 or r == ROWS-1 or c == 0 or c == COLS - 1:
                border = 1

            border += (dfs(r+1, c, region) + dfs(r, c+1, region) + dfs(r-1, c, region) + dfs(r,  c-1, region))

            return border       
            
            
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in visited:
                    region = []
                    if dfs(r, c, region) == 0:
                        for rr, rc in region:
                            board[rr][rc] = "X"
