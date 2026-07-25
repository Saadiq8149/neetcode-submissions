class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        def recurse(i, j, curr, marked):
            print(curr)
            if min(i, j) < 0 or i >= ROWS or j >= COLS or len(curr) == len(word):
                if curr == word:
                    return True
                return False

            res = False

            if j < COLS-1 and not marked[i][j+1]:
                marked[i][j+1] = True
                res = res or recurse(i, j+1, curr+board[i][j+1], marked)
                marked[i][j+1] = False
            if j > 0 and not marked[i][j-1]:
                marked[i][j-1] = True
                res = res or recurse(i, j-1, curr+board[i][j-1], marked)
                marked[i][j-1] = False
            if i < ROWS-1 and not marked[i+1][j]:
                marked[i+1][j] = True
                res = res or recurse(i+1, j, curr+board[i+1][j], marked)
                marked[i+1][j] = False
            if i > 0 and not marked[i-1][j]:
                marked[i-1][j] = True
                res = res or recurse(i-1, j, curr+board[i-1][j], marked)
                marked[i-1][j] = False

            return res
            


        marked = [[False] * COLS for _ in range(ROWS)]
        for i in range(ROWS):
            for j in range(COLS):
                marked[i][j] = True
                if recurse(i, j, board[i][j], marked):
                    return True
                marked[i][j] = False

        return False
        
