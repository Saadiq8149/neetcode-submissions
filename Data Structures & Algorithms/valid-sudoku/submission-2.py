class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        for i in range(n):
            row_seen = set()
            for j in range(n):
                num = board[i][j]
                if num == ".":
                    continue
                if num in row_seen:
                    return False
                row_seen.add(num)
            col_seen = set()
            for j in range(n):
                num = board[j][i]
                if num == ".":
                    continue
                if num in col_seen:
                    return False
                col_seen.add(num)
                    
        for s in range(n):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (s//3) * 3 + i
                    col = (s % 3) * 3 + j
                    num = board[row][col]
                    if num  == ".":
                        continue
                    if num in seen:
                        return False
                    seen.add(num)
        
        return True
            