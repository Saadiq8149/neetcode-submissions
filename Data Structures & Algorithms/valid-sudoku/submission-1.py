class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_sets = [set() for x in range(len(board))]
        col_sets = [set() for x in range(len(board[0]))]
        square_sets = [set() for x in range(len(board))]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                number = board[i][j]
                if number == ".":
                    continue 
                if number in row_sets[i]:
                    return False
                else:
                    row_sets[i].add(number)
                if number in col_sets[j]:
                    return False
                else:
                    col_sets[j].add(number)
                if number in square_sets[(i//3)*3 + j//3]:
                    return False
                else:
                    square_sets[(i//3)*3 + j//3].add(number)
        return True
